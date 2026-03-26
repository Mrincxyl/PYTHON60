from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify
from .models import Blog, Category
import uuid

# Create your views here.
def Blogs(request):
    return render(request, 'allblogs.html')

@login_required(login_url='login')
def Create(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        if 'add_category' in request.POST:
            category = request.POST.get('category')

            if (category):
                Category.objects.get_or_create(name = category)
                messages.success(request, f'{category} Category Created.')
            else:
                messages.error(request, "Category Field is Required.")

            return redirect('create')

        # handle create blog
        if 'add_blog' in request.POST:
            title = request.POST.get('title')
            slug = request.POST.get('slug')
            author = request.user
            category_id = request.POST.get('category')
            image = request.FILES.get('thumbnail')
            content = request.POST.get('content')
            visibility = request.POST.get('visibility')

            if not title or not content:
                messages.error(request, "Title and Content are required!")
                return redirect('create')

            category = None
            if category_id:
                try:
                    category = Category.objects.get(id=category_id)
                except Category.DoesNotExist:
                    messages.error(request, "Invalid category selected!")
                    return redirect('create')

            if not slug:
                slug = slugify(title) + "-" + str(uuid.uuid4())[:4]


            if Blog.objects.filter(slug=slug).exists():
                slug = slug + "-" + str(uuid.uuid4())[:3]

            Blog.objects.create(
                title=title,
                slug=slug,
                author=author,
                category=category,
                image=image,
                content=content,
                visibility=visibility
            )

            messages.success(request, "Blog created successfully! 🎉")
            return redirect('create')


        if 'delete_category' in request.POST:
            id = request.POST.get('delete_category')
            c = Category.objects.get(id=id)
            c.delete()
            messages.success(request, 'Category Deleted.')
            return redirect('create')

            

            


    return render(request, 'create.html', {'data': categories})