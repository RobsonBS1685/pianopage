import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render

from .forms import ContactMessageForm

logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'inicio/index.html')


def sobre_mi(request):
    return render(request, 'inicio/sobre_mi.html')


def contacto(request):
    form = ContactMessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        notification_sent = False
        if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD and settings.CONTACT_EMAIL:
            data = form.cleaned_data
            body = (
                f"Nombre: {data['name']}\n"
                f"Correo: {data['email']}\n"
                f"Asunto: {data['subject']}\n\n"
                f"Mensaje:\n{data['message']}"
            )
            try:
                sent_count = EmailMessage(
                    subject=f"Nuevo mensaje desde tu sitio: {data['subject']}",
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.CONTACT_EMAIL],
                    reply_to=[data['email']],
                ).send(fail_silently=False)
                notification_sent = sent_count == 1
                if not notification_sent:
                    logger.error("El servidor de correo no aceptó el mensaje de contacto.")
            except Exception:
                logger.exception("No se pudo enviar la notificación del formulario de contacto")
        else:
            logger.error(
                "No se envió el mensaje de contacto: falta EMAIL_HOST_USER, "
                "EMAIL_HOST_PASSWORD o CONTACT_EMAIL."
            )

        if notification_sent:
            messages.success(request, "Tu mensaje fue enviado. Gracias por escribirme.")
        else:
            messages.error(
                request,
                "No se pudo enviar el mensaje. Revisa la configuración de correo e inténtalo nuevamente.",
            )
        form = ContactMessageForm()
    return render(request, 'inicio/contacto.html', {"form": form})
