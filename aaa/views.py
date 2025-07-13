from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {"pag_titulo": "Home"} )

def aaa(request):
    return render(request, 'aaa.html', {"pag_titulo": "aaa"} )

def bbb(request):
    return render(request, 'bbb.html', {"pag_titulo": "bbb"} )

def ccc(request):
    return render(request, 'ccc.html', {"pag_titulo": "ccc"} )
