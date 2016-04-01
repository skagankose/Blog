from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaulttags import register

# Combine query sets
from itertools import chain

# Get time
from django.utils import timezone

# Ours'
from .forms import PostForm, GeneralTextForm, GeneralFileForm, CategoryForm, EditGeneralTextForm, EditGeneralFileForm, EditPostForm
from .models import Post, GeneralText, GeneralFile, Category
import random


@register.filter
def cut_category(post):
	returnString = str()
	for category in post.category.all():
		returnString +=  str(category) + " "
	return returnString

@register.filter
def cut_date(date):
	# splitted = str(date).split()[0].split("-")
	# return splitted[0][2:5] + splitted[1] + splitted[2]
	return str(date.strftime('%B')) + " " + str(date.day) + ",  " + str(date.year)

@register.filter
def cut_doc(doc):
	return str(doc).split("/")[1]

@register.filter
def cut_img(img):
	img = str(img).split("/")
	if len(img) > 1:
		return img[1]
	else:
		return False

@register.filter
def cut_link(cut_link):
	returnString = str()
	items = str(cut_link).split("//")[1].split(".")
	for i in range(len(items)):
		returnString = returnString + "." + items[i]
	return returnString[1:]

# Homepage
def homepage(request):

	categories = Category.objects.all()
	posts =  Post.objects.all()
	randNumber = (int(random.random() * len(posts))) + 1
	context = {'posts':posts,'categories':categories,'randNumber':randNumber}

	return render(request, 'precious/home.html', context)

# Search
def search(request):

    categories = Category.objects.all()
    posts =  Post.objects.all()
    context = {'posts':posts,'categories':categories,}
    return render(request, 'precious/search.html', context)

# Tags
def tags(request):

    categories = Category.objects.all()
    posts =  Post.objects.all()
    context = {'posts':posts,'categories':categories,}
    return render(request, 'precious/tags.html', context)


# Create Post
def new_post(request):

    if request.method == 'POST':
        form  = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thumbnail = request.FILES.get('thumbnail', None)
            post.save()
            form.save_m2m()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(status=204)
    else:
        form  = PostForm()

    context = {'form': form,}
    return render(request,'precious/new_post.html', context)

# Create Post
def new_category(request):

	if request.method == 'POST':
		form  = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/new_post/')
		else:
			return HttpResponse(status=204)
	else:
		category_form = CategoryForm()

	context = {'category_form': category_form,}
	return render(request,'precious/new_category.html', context)

# Create GeneralText
def new_general_text(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form  = GeneralTextForm(request.POST)
        item_type = request.POST.get('item_type')
        if form.is_valid():
            post.item_position += 10
            post.save()
            general_text = form.save(commit=False)
            general_text.post = post

            if item_type == 'code':
                general_text.code = True
            elif item_type == 'paragraph':
                general_text.paragraph = True
            elif item_type == 'heading':
                general_text.heading = True
            elif item_type == 'subheading':
                general_text.subheading = True
            elif item_type == 'subsubheading':
                general_text.subsubheading = True
            elif item_type == 'list_item':
                general_text.list_item = True
            elif item_type == 'inline_block':
                general_text.inline_block = True
            elif item_type == 'table':
                general_text.table = True
            elif item_type == 'link':
                general_text.link = True
            elif item_type == 'youtube':
                general_text.youtube = True
            elif item_type == 'is_safe':
                general_text.is_safe = True

            general_text.position = post.item_position
            general_text.save()
            return HttpResponseRedirect('/newPost/' + pk)
        else:
            return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)

# Create GeneralFile
def new_general_file(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form  = GeneralFileForm(request.POST)
        file_type = request.POST.get('file_type')
        post.item_position += 10
        post.save()
        general_file = form.save(commit=False)
        general_file.post = post

        if file_type == 'image':
            general_file.image = True
        elif file_type == 'video':
            general_file.video = True
        else:
            general_file.other = True

        general_file.position = post.item_position
        general_file.file_item = request.FILES.get('file_item', None)

        if general_file.file_item  != None:
            general_file.save()
            return HttpResponseRedirect('/newPost/' + pk)
        else:
            return HttpResponse(status=204)
    else:
        return HttpResponse(status=204)

# Look Post in details
def newPost(request, pk):

    post = get_object_or_404(Post, pk=pk)
    general_text_form  = GeneralTextForm()
    general_file_form = GeneralFileForm()
    general_texts = post.general_texts.all()
    general_files = post.general_files.all()
    all_items = sorted(
                chain(general_texts, general_files),
                key=lambda instance: instance.position)

    context = {'post': post,
               'general_texts': general_texts,
               'general_files': general_files,
               'all_items': all_items,
               'general_text_form': general_text_form,
               'general_file_form': general_file_form,}

    return render(request, 'precious/newPost.html', context)

# Delete GeneralText
def delete_general_text(request, pk, ppk):
    general_text = get_object_or_404(GeneralText, pk=pk)
    general_text.delete()
    return HttpResponseRedirect('/newPost/' + ppk)

# Delete GeneralText
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect('/')

# Delete GeneralFile
def delete_general_file(request, pk, ppk):
    general_file = get_object_or_404(GeneralFile, pk=pk)
    general_file.delete()
    return HttpResponseRedirect('/newPost/' + ppk)

# AJAX search
def post_search(request):
    if request.method == 'POST':
        text_search = request.POST['text_search']
        if text_search == '':
            text_search = '✗'
    else:
        text_search = None
    posts = Post.objects.filter(title__icontains=text_search)
    context = {'posts': posts,}
    return render(request, 'precious/ajax_search.html', context)

# AJAX Category text search
def category_text_search(request):
    if request.method == 'POST':
        category_text_search = request.POST['category-text-search']
        if category_text_search == '':
            category_text_search = '✗'
    else:
        category_text_search = None

    try:
        category = Category.objects.get(text=category_text_search)
        posts = category.posts.all()
    except:
        posts = False
    context = {'posts': posts,}
    return render(request, 'precious/ajax_search.html', context)

# Edit existing GeneralText
def edit_general_text(request, pk, pks):
    post = get_object_or_404(Post, pk=pk)
    general_text = get_object_or_404(GeneralText, pk=pks)
    if request.method == 'POST':
        form = EditGeneralTextForm(request.POST, instance=general_text)
        if form.is_valid():
            edited_general_text = form.save(commit=False)
            edited_general_text.edited = True
            edited_general_text.save()
            return HttpResponseRedirect('/newPost/' + pk)
    else:
        form = EditGeneralTextForm(instance=general_text)

    context = {'post':post,'form': form, 'general_text': general_text}
    return render(request,'precious/edit_general_text.html', context)

# Edit existing GeneralFile
def edit_general_file(request, pk, pks):
    post = get_object_or_404(Post, pk=pk)
    general_file = get_object_or_404(GeneralFile, pk=pks)
    if request.method == 'POST':
        form = EditGeneralFileForm(request.POST, instance=general_file)
        if form.is_valid():
            edited_general_file = form.save(commit=False)
            edited_general_file.edited = True
            edited_general_file.save()
            return HttpResponseRedirect('/newPost/' + pk)
    else:
        form = EditGeneralFileForm(instance=general_file)

    context = {'post':post,'form': form, 'general_file': general_file}
    return render(request,'precious/edit_general_file.html', context)

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.edited = True
            edited_post.updated_date = timezone.now()
            edited_post.save()
            form.save_m2m()
            edited_post.thumbnail = request.FILES.get('thumbnail', None)
            if edited_post.thumbnail != None:
                    edited_post.save()
            return HttpResponseRedirect('/newPost/' + pk)
    else:
            form = EditPostForm(instance=post)
    context = {'form': form, 'post': post}
    return render(request,'precious/update_post.html', context)

def editor_on(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_editor = True
    post.save()
    return HttpResponseRedirect('/newPost/' + str(pk) + '/')

def editor_off(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_editor = False
    post.save()
    return HttpResponseRedirect('/newPost/' + str(pk) + '/')

def new_base(request):
    return render(request,'precious/newBase.html', {})

# Look Post in details
def newPost(request, pk):

    post = get_object_or_404(Post, pk=pk)
    general_text_form  = GeneralTextForm()
    general_file_form = GeneralFileForm()
    general_texts = post.general_texts.all()
    general_files = post.general_files.all()
    all_items = sorted(
                chain(general_texts, general_files),
                key=lambda instance: instance.position)

    context = {'post': post,
               'general_texts': general_texts,
               'general_files': general_files,
               'all_items': all_items,
               'general_text_form': general_text_form,
               'general_file_form': general_file_form,}

    return render(request, 'precious/newPost.html', context)
