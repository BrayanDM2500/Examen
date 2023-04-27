from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def login(request):

    doc_externo=loader.get_template('index.html')

    documento=doc_externo.render()

    return HttpResponse(documento)

def main(request):

    doc_externo=loader.get_template('main.html')

    documento=doc_externo.render()

    return HttpResponse(documento)
