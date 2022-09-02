from django.contrib import admin
from .models import Category,Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display=('image_tag', 'title' ,'add_date')
	list_filter=("title",)
	search_fields=("add_date",)


class PostAdmin(admin.ModelAdmin):
	list_display=( 'title' ,'url')
	per_page=40


admin.site.register(Category ,CategoryAdmin)
admin.site.register(Post ,PostAdmin)