from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobForm

def index(request):
    jobs = JobApplication.objects.all().order_by('-applied_on')
    return render(request, 'tracker/index.html', {'jobs': jobs})

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'tracker/add.html', {'form': form})
