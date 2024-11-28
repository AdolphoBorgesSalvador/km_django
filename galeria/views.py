from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import subprocess

def index(request):
        return render(request, 'galeria/index.html')

def run_script(request):
    # Execute o script Python desejado
    result = subprocess.check_output(['python', 'run_script.py'], universal_newlines=True)
    return HttpResponse(f'O script foi executado. Resultado: {result}')
def outra_pagina(request):
    return render(request, 'galeria/outra_pagina.html')