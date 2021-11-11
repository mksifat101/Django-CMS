from django.contrib import admin
from blog.models import Category, SubCategory, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug', 'create_date')
    prepopulated_fields = {'slug': ('category_name',)}


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sub_category_name',
                    'slug', 'category', 'create_date')
    prepopulated_fields = {'slug': ('sub_category_name',)}


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',
                    'slug', 'category', 'sub_category', 'create_date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Post, PostAdmin)
