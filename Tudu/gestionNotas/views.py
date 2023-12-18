from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import Login, Register, Note
from .models import Usuario, Nota
from gestionNotas.utils import *
from django.contrib.auth.decorators import login_required

@login_required
def vista_principal(request):

    # Formulario para crear Nota
    if request.method == "POST":

        form = Note(request.POST)
        if form.is_valid():

            title = form.cleaned_data['title']
            title = title.upper()

            nota = form.cleaned_data['note']

            user_id = None
            if request.user.is_authenticated:
                user_id = request.user.id

            if title != "":
                Nota.objects.create(titulo=title, contenido=nota, urgencia=0, user_id = user_id)
            
            return redirect('vista_principal')  
    

    elif request.method == "GET":

        # Formulario para ver contenido de las notas
        if 'ver-nota' in request.GET:
            
            titulo_nota = request.GET.get('ver-nota')
            user_id = None

            if request.user.is_authenticated:
                user_id = request.user.id

            try:
                contenido_nota = Nota.objects.get(titulo=titulo_nota, user_id = user_id)
                lista_renglones = separarRenglones(contenido_nota)
                form = Note()
                titulos = getAllTitles(request)
                return render(request, "index.html", {'titulos':titulos, 'nota':contenido_nota,'contenido_nota':lista_renglones})
                
            except Nota.DoesNotExist:
                pass
            

        # Formulario para borrar una nota       
        elif 'borrar-nota' in request.GET:
            titulo_nota = request.GET.get('borrar-nota-titulo')
            eliminarNota(request, titulo_nota)

    form = Note()
    titulos = getAllTitles(request)

                    
        
    return render(request, "index.html", {'titulos':titulos})


def vista_login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:

                usuario = Usuario.objects.get(username=username, password=password)
                login(request, usuario)  
                return redirect('vista_principal')
            
            except Usuario.DoesNotExist:
                pass
    else:
        form = Login()

    return render(request, "login.html", {"form": form})


def vista_register(request):
    error = []
    respuesta = False
    reason = ""

    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():

            usuario = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']

            if password == password_repeat:
                valida, error = validatePassword(password)

                if valida and not error:

                    respuesta, reason = comprobarUser(usuario, email)

                    if respuesta:

                        try:
                            Usuario.objects.create(username=usuario, email=email, password=password)
                            return redirect('vista_login')
                        
                        except:
                            pass
                    else:
                        existantAccount = reason
                        
                else:
                    return render(request, "register.html", {"form": form, "error": error, 'error_bd':respuesta, "datos_error": existantAccount})
                
    else:
        form = Register()

    return render(request, "register.html", {"form": form, "error": error, 'error_bd':respuesta, "datos_error": reason})