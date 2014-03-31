from django.shortcuts import render, render_to_response
from tags.models import Tag

def index(request):
    tags = Tag.objects.all().order_by('-name')
    return render(request, 'tags/index.html', {'tags': tags})

def detail(request, pk):
    tag = Tag.objects.get(pk=pk)
    return render(request, 'tags/detail.html', {'tag': tag})

def edit(request, pk):
    tag = Tag.objects.get(pk=pk)
    if request.method == 'POST':
        tag.name = request.POST['name']
        tag.save()
        return render_to_response('tags/detail.html', {'tag': tag})
    else:
        return render(request, 'tags/edit.html', {'tag': tag})

def create(request):
    valid = True
    if request.method == 'POST':
        if request.POST['name'] == "":
            valid = False
    if request.method == 'POST' and valid:
        tag = Tag(name=request.POST['name'])
        tag.save()
        return render_to_response('tags/detail.html', {'tag': tag})
    else:
        return render(request, 'tags/create.html', {'valid': valid})
