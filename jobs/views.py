from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader


from jobs.models import Job
from jobs.models import Cities, JobTypes


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('joblist.html')
    context = {'joblist': job_list}

    for job in job_list:
        print(type(job))
        print(job.job_type)
        job.city_name = Cities[job.job_city][1]
        job.job_type = JobTypes[job.job_type][1]
    print(job_list)


    return HttpResponse(template.render(context))


def detail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        job.city_name = Cities[job.job_city]
        print(job)
        print(type(job))
        print(123)
    except Job.DoesNotExist:
        raise Http404('Job does not exit.')
    return render(request, 'job.html', {'job': job})