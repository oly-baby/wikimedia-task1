from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse
from .models import Bug
from .forms import BugForm

# Create your views here.


def index(request):
    bugs = Bug.objects.all()
    return render(request, 'index.html', {'all_bug': bugs})


def create_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            HttpResponse("Error")
    else:
        form = BugForm()
        # HttpResponse("Error")
    return render(request, 'add_bug.html', {'form': form})


def view_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    return render(request, 'view_bug.html', {'bug': bug})



