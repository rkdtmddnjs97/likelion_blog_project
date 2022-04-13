from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

# # Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')

def create(request):
    new_blog = Blog()
    new_blog.title =  request.POST['title']
    new_blog.contents = request.POST['contents']
    new_blog.save() #필수 
    return redirect('detail',new_blog.id)

def edit(request,id):
    edit_blog = get_object_or_404(Blog,pk = id)
    return render(request,'edit.html',{'blog':edit_blog})

def update(request,id):
    update_blog = get_object_or_404(Blog,pk=id)
    update_blog.title = request.POST['title']
    update_blog.contents = request.POST['contents']
    update_blog.save()
    return redirect('detail',update_blog.id)

def delete(request,id):
    delete_blog  = get_object_or_404(Blog,pk = id)
    delete_blog.delete()
    return redirect('home')




