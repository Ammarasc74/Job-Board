from django.shortcuts import render
from .models import job

# Create your views here.

def job_list(request):
    job_list = job.objects.all()
    print(job_list)
    context = {'jobs': job_list } #template name 
    return render(request,'job/job_list.html',context)




def job_detail(request, id):
    job_detail = job.objects.get(id=id)
    context = {'job':job_detail}
    return render(request,'job/job_detail.html',context)