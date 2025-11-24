from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedManager, self)
            .get_queryset()
            .filter(status="publicado")
        )


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
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ],
        )
