from django.db import models


class ContactMessage(models.Model):
    name = models.CharField("nombre", max_length=120)
    email = models.EmailField("correo electrónico")
    subject = models.CharField("asunto", max_length=160)
    message = models.TextField("mensaje")
    created_at = models.DateTimeField("fecha de envío", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "mensaje de contacto"
        verbose_name_plural = "mensajes de contacto"

    def __str__(self):
        return f"{self.subject} — {self.name}"

# Create your models here.
