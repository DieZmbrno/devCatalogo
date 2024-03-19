from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'catalogoApp/index.html')

def accesorios(request):
    datos = {
        "TITULO":"Accesorios",
        "producto1":"Guante",
        "producto2":"Mascarilla",
        "producto3":"Gorro"
    }
    return render(request, 'catalogoApp/productos.html',datos)

def papeles(request):
    datos = {
        "TITULO":"Papeleria",
        "producto1":"Confort",
        "producto2":"Nova",
        "producto3":"Hoja de oficio"
    }
    return render(request, 'catalogoApp/productos.html',datos)

def insumos(request):
    datos = {
        "TITULO":"Insumos",
        "producto1":"Alcohol",
        "producto2":"Vacelina",
        "producto3":"Gel"
    }
    return render(request, 'catalogoApp/productos.html',datos)
