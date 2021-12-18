from django.contrib import admin
from .models import Post
 
# habilitando models no dashboard admin do django.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', '_author')
    exclude = ['author',]

    # cada author é um usuario no sistema
    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

    # apresenta somente os dados do author que esta logado
    def get_queryset(self, request):
        qs = super(Post, self).get_queryset(request)
        return qs.filter(author=request.user)

    # alterar o metodo de salvar
    # informar o author que esta salvando
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
