from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroForm


def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
    else:
        form = CadastroForm()

    return render(request, 'accounts/cadastro.html', {
        'form': form
    })
