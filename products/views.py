from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Produto


@login_required(login_url='login')
def home_view(request):
    produtos = Produto.objects.all()

    return render(request, 'products/home.html', {
        'produtos': produtos
    })
