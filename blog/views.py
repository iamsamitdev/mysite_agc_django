from django.shortcuts import render, get_object_or_404
# Import Model
from .models import Post

# สร้างฟังก์ชันอ่านโพสต์ทั้งหมด
def post_list(request):

    # สร้างตัวแปร posts เก็บโพสต์ทั้งหมด
    posts = Post.published.all() # ใช้ Manager ที่สร้างขึ้นเอง 

    # ส่งค่าไปยัง template ผ่านตัวแปร posts
    return render(request, 'blog/post/list.html', {'posts': posts})


# แสดงหน้ารายละเอียดโพสต์
def post_detail(request, id):
    # สร้างตัวแปร post เก็บโพสต์ที่ต้องการ
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    # ส่งค่าไปยัง template ผ่านตัวแปร post
    return render(request, 'blog/post/detail.html', {'post': post})
