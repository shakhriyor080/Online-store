from django.shortcuts import render
from .forms import *
# Create your views here.
from .models import *
# Create your views here.



def index(request):
    post = Post.objects.all()   
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST'and form.is_valid():
        form.save()
        form= ApplicationForm()
    return render(request, 'post.html', {'form': form,'post':post})

   
def product_detail(request,slug):
    now = Post.objects.get(slug__iexact = slug)  
    return render(request, 'product_detail.html' ,{'now':now})

