from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Os campos que serão exibidos na listagem das postagens
    list_display = ("title", "slug", "author", "publish", "status")
    # Irá criar uma coluna de filtros no canto direito que permite
    # filtrar os resultados
    list_filter = ("status", "created", "publish", "author")
    # Uma caixa de pesquisa quer permite buscar nos campos definidos
    search_fields = ("title", "body")
    # Fará com que ao digitar o título o campo slug será preenchido
    # automaticamente.
    prepopulated_fields = {"slug": ("title",)}
    # Fará com que o author será exibido como um widget de pesquisa
    # no cadastro da postagem.
    raw_id_fields = ("author",)
    # Criará abaixo do campo de pesquisa links para navegar por uma
    # hierarquia de datas
    date_hierarchy = "publish"
    # Os critérios de ordenação padrão
    ordering = ("status", "publish")
