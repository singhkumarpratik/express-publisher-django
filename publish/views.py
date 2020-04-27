from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView
from .models import *
from .forms import *
def index(request):
    print(express_publish)
    all_publish=express_publish.objects.all()
    form=express_publishForm()
    if request.method=="POST":
        form=express_publishForm(request.POST)
        if form.is_valid():
            form.save()
        # sl=form.cleaned_data['slug']
        the_post=express_publish.objects.last()
        return redirect(reverse('post_detail', args=[the_post.slug]))
    context={'all_publish':all_publish,'form':form}
    return render(request,'publish/index.html',context)

class PostDetail(generic.DetailView):
    model = express_publish
    template_name = 'publish/post_detail.html'
