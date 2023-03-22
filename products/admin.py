from django.contrib import admin
from .models import Category, Author, Product, Photo, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [CommentInline, PhotoInline]
    
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Product, ProductAdmin)
# admin.site.register(Photo)
# admin.site.register(Comment)

