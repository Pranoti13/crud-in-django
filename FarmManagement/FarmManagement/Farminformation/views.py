from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Farminformation
from .models import Workerspayment


# Create your views here.

def index(request):
    myWorkers = Farminformation.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'myWorkers': myWorkers,
    }
    return HttpResponse(template.render(context, request))


# Workerdetails #
def index1(request):
    myWorkers = Farminformation.objects.all().values()
    template = loader.get_template('index1.html')
    context = {
        'myWorkers': myWorkers,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    worker = Farminformation(firstname=x, lastname=y)
    worker.save()
    return HttpResponseRedirect(reverse('index1'))


def delete(request, id):
    worker = Farminformation.objects.get(id=id)
    worker.delete()
    return HttpResponseRedirect(reverse('index1'))


def update(request, id):
    myWorkers = Farminformation.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'myWorkers': myWorkers,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    worker = Farminformation.objects.get(id=id)
    worker.firstname = first
    worker.lastname = last
    worker.save()
    return HttpResponseRedirect(reverse('index1'))


# Workers Payment History #
def workerspayhistory(request):
    myWorkers = Workerspayment.objects.all().values()
    template = loader.get_template('workerspayhistory.html')
    context = {
        'myWorkers': myWorkers,
    }
    return HttpResponse(template.render(context, request))


def addworkerpay(request):
    template = loader.get_template('addworkerpay.html')
    return HttpResponse(template.render({}, request))


def addnewrecord(request):
    a = request.POST['name']
    b = request.POST['datetime']
    c = request.POST['amount']
    d = request.POST['payment type']
    e = request.POST['mobile number']
    worker = Workerspayment(Name=a, DateTime=b, Amount=c, PaymentType=d, MobileNumber=e)
    worker.save()
    return HttpResponseRedirect(reverse('workerspayhistory'))


def deleteworkerpayhistory(request, id):
    worker = Workerspayment.objects.get(id=id)
    worker.delete()
    return HttpResponseRedirect(reverse('workerspayhistory'))


def updateworkerpayhistory(request, id):
    myWorkers = Workerspayment.objects.get(id=id)
    template = loader.get_template('updateworkerpayhistory.html')
    context = {
        'myWorkers': myWorkers,
    }
    return HttpResponse(template.render(context, request))


def updatepayrecord(request, id):
    Name = request.POST['name']
    DateTime = request.POST['datetime']
    Amount = request.POST['amount']
    PaymentType = request.POST['payment type']
    MobileNumber = request.POST['mobile number']

    worker = Workerspayment.objects.get(id=id)
    worker.Name = Name
    worker.DateTime = DateTime
    worker.Amount = Amount
    worker.PaymentType = PaymentType
    worker.MobileNumber = MobileNumber
    worker.save()
    return HttpResponseRedirect(reverse('workerspayhistory'))

# return HttpResponseRedirect(template.render(context, request))

# output = ""
# for x in myWorkers:
#
#     output += x["firstname"]
#     output += x["lastname"]


#    return HttpResponse(output)


# template=loader.get_template('myfirst.html')
# logging.info('Hello')
#
# return HttpResponse(template.render())
