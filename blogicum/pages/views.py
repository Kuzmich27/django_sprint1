from django.http import HttpResponse

from django.template import loader


def about(request):
    template = loader.get_template('pages/about.html')
    context = {}
    return HttpResponse(template.render(context, request))


def rules(request):
    template = loader.get_template('pages/rules.html')
    context = {}
    return HttpResponse(template.render(context, request))
