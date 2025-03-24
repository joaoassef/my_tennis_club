from re import template

from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Member
from django.urls import reverse
from plans.models import Plan
from django.db.models import Q
from django.core.paginator import Paginator

#members é a requisição /members que esta configurado no arquivo urls.py
def members(request):
    vetor     = Member.objects.all()
    template  = loader.get_template('all_members.html')

    paginator = Paginator(vetor, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context   = {
        'mymembers': vetor,
        'page_obj': page_obj,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template  = loader.get_template('details.html')
    context   = {
        'mymember': mymembers
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    myplans = Plan.objects.all().values()
    template = loader.get_template('add.html')
    context = {
        'myplans': myplans,
    }
    return HttpResponse(template.render(context, request))

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    z = Plan.objects.filter(id=request.POST['plan']).first()
    foto = None

    if 'foto' in request.FILES:
        foto = request.FILES['foto']

    if 'documento' in request.FILES:
        documento = request.FILES['documento']

    member = Member(firstname=x, lastname=y, plan=z, foto=foto, documento=documento)

    member.save()

    return HttpResponseRedirect(reverse('members'))

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    mymember = Member.objects.get(id=id)
    myplans = Plan.objects.all().values()
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
        'myplans': myplans,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    first =  request.POST['first']
    last = request.POST['last']
    plan = request.POST['plan']
    member = Member.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.plan = Plan.objects.get(id=plan)
    if 'foto' in request.FILES:
        foto = request.FILES['foto']
        member.foto = foto

    if 'documento' in request.FILES:
        documento = request.FILES['documento']
        member.documento = documento

    member.save()
    return HttpResponseRedirect(reverse('members'))

def busca(request):
    texto_busca = request.POST['busca']
    dados = Member.objects.filter(
            Q(firstname__icontains=texto_busca) | Q(lastname__icontains=texto_busca)
    ).values()
    t = loader.get_template('all_members.html')
    context = {
        'mymembers': dados,
        'texto_busca': texto_busca,
        'qtd': len(dados),
    }
    return HttpResponse(t.render(context, request))