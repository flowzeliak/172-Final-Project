from django.shortcuts import render, get_object_or_404
from .models import ExerType, Exerlog
from .forms import TypeForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'fitapp/index.html')

def exertype (request):
    type_list=ExerType.objects.all()
    return render(request, 'fitapp/types.html', {'type_list': type_list})

def exerlog (request):
    log_list=Exerlog.objects.all()
    return render(request, 'fitapp/log.html', {'log_list': log_list})

def detlog (request, id):
    detail=get_object_or_404(Exerlog, pk=id)
    context = { 'detail': detail }
    return render(request, 'fitapp/detail.html', context=context )

#form view
@login_required
def newType(request):
    form=TypeForm
    if request.method=='POST':
        form=TypeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TypeForm()
    else:
        form=TypeForm()
    return render(request, 'fitapp/newtype.html', {'form': form})

def loginmessage(request):
    return render(request, 'fitapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'fitapp/logoutmessage.html')