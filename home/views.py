from django.shortcuts import render, redirect
from confession.models import Confession, Comment
from django.contrib.auth.decorators import login_required

def about(request):
    return render(request, "home/about.html")

def privacy(request):
    return render(request, "home/privacy.html")

def tos(request):
    return render(request, "home/tos.html")

def cg(request):
    return render(request, "home/cg.html")

def contact(request):
    return render(request, "home/contact.html")


def home(request):
    confessions = Confession.objects.all().order_by("-id")
    return render(request,"home/home.html",{"confessions":confessions})

@login_required
def toggle_heart(request, confession_id):
    confession = Confession.objects.filter(id=confession_id).first()
    if confession:
        if request.user in confession.hearts.all():
            confession.hearts.remove(request.user)
        else:
            confession.hearts.add(request.user)
    return redirect('home')

@login_required
def add_comment(request, confession_id):
    if request.method == 'POST':
        confession = Confession.objects.get(id=confession_id)
        content = request.POST.get('content')
        if content:
            Comment.objects.create(confession=confession, user=request.user, content=content)
    return redirect('home')