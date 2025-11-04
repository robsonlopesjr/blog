from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ("rascunho", "Rascunho"),
        ("publicado", "Publicado"),
    )
    title = models.CharField(max_length=250, verbose_name="Título")
    slug = models.SlugField(
        max_length=250, unique_for_date="publish", verbose_name="Slug"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        verbose_name="Autor",
    )
    body = models.TextField(verbose_name="Texto da Postagem")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="Data da Publicação"
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Criação"
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Data da Atualização"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="rascunho",
        verbose_name="Status da Postagem",
    )

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title
