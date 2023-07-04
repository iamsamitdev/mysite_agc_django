from django.db import models
from django.utils import timezone # เพิ่ม datetime
from django.contrib.auth.models import User # เพิ่มความสัมพันธ์กับ User

class PublishedManager(models.Manager): # สร้าง Manager สำหรับโมเดล Post
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

# สร้างโมเดล Post
class Post(models.Model):

    # Enum สำหรับฟิลด์ status ไว้ใช้ในการเลือกค่า
    class Status(models.TextChoices): # เพิ่มฟิลด์ status
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, 
                                on_delete=models.CASCADE, 
                                related_name='blog_posts') # เพิ่มความสัมพันธ์กับ User
    publish = models.DateTimeField(default=timezone.now) # เพิ่ม datetime
    created = models.DateTimeField(auto_now_add=True) # เพิ่ม datetime
    updated = models.DateTimeField(auto_now=True) # เพิ่ม datetime
    status = models.CharField(max_length=2, 
                                choices=Status.choices, 
                                default=Status.DRAFT) # เพิ่มฟิลด์ status

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta: # การกำหนดการเรียงข้อมูลในโมเดล Post
        ordering = ['-publish'] # เรียงลำดับโพสต์จากวันที่ล่าสุดไปยังเก่าสุด
        indexes = [
            models.Index(fields=['-publish']), # เพิ่ม index
        ]

    def __str__(self):
        return self.title
