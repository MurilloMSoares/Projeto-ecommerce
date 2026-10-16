from django.shortcuts import render
from .models import Produto


def home_view(request):
    produtos = Produto.objects.all()
    return render(request, 'products/home.html', {'produtos': produtos})