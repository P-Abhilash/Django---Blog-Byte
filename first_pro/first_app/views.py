from django.contrib.admin.views.decorators import staff_member_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


from .models import BlogPost
from .con_forms import ContactForm
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    context = {'object_list': qs}
    template_name = 'blog/list.html'
    return render(request, template_name, context)

# @login_required
@staff_member_required 
def blog_post_create_view(request):

    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # obj = BlogPost.objects.create(**form.cleaned_data) #this will save the post
        messages.success(request, 'New Blog Successfully Created!')
        return HttpResponseRedirect('/blog')
    template_name = 'blog/create.html'
    context = {'form': form, "title": "Creare a new blog"}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.info(request, 'Blog Successfully Updated!')
        return HttpResponseRedirect("/blog/{slug}".format(slug=obj.slug))
    template_name = 'blog/update.html'
    context = {'form': form, "title": f"Update - {obj.title}"}
    
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        messages.error(request, 'Blog Successfully Deleted!')
        return HttpResponseRedirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)





def start(request):
    return HttpResponse("GO TO BLOG/")

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    if request.method == "POST":
        return redirect("/blog")
    context = {
        "title" : "Contact us", "form": form
    }
    return render(request, 'contact.html', context)
