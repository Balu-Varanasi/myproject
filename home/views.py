from django.shortcuts import render

from home.models import Subject


def index(request):
    subjects = Subject.objects.all()

    get_parameters = request.GET
    return render(
        request,
        'home.html',
        {'subjects': subjects}
    )

    def hello():
        print "hello"
