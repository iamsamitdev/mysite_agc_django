from django.contrib import admin
from .models import Post


# Customizing the way models are displayed
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # เพิ่มฟิลด์
    list_filter = ['status', 'created', 'publish', 'author'] # เพิ่มฟิลเตอร์
    search_fields = ['title', 'body'] # เพิ่มฟิลด์
    ordering = ['status', 'publish'] # เพิ่มการเรียงลำดับ
    raw_id_fields = ['author'] # เพิ่มฟิลด์
