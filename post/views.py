from django.shortcuts import redirect, render , get_object_or_404
from .models import Post
from django.contrib import messages
from .forms import PostCreate , UpdatePostForm
from django.http import HttpResponse
# Create your views here.

#home
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

# add
def add(request):
    upload = PostCreate
    if request.method=='POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            messages.success(request,'Data has been added')
            return redirect('/admin')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/admin'}}">reload</a>""")
    else:
        return render(request, 'add.html', {'upload_form':upload})


# delete

def delete(request, id):
    id = int(id)
    try:
        post_sel = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return redirect('/admin')
    post_sel.delete()
    return redirect('/admin')

# update

def update(request, id):
	context = {}
	post = get_object_or_404(Post, id=id)
	if request.POST:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			post = obj
	form = UpdatePostForm(
			initial = {
					"title": post.title,
					"detail": post.detail,
					"logo": post.logo,
                    "state": post.state ,
                    "category": post.category
			}
		)
	context['form'] = form
	return render(request, 'update.html', context)