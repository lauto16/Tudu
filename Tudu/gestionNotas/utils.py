from .models import Nota, Usuario


def validatePassword(password):

    password = password.lower()
    symbols = False
    numbers = False
    tilde_espacio = False

    for i in password:
        
        if i in ("áéíóú") or i == " ":
            tilde_espacio = True
        if not i.isalnum():
            symbols = True
        if i.isdigit():
            numbers = True
        
    error_messages = []

    # Resto de tu código permanece igual, solo cambia la forma en que agregas mensajes de error a 'r'
    if len(password) < 10:
        error_messages.append("Debe contener al menos 10 caracteres")
    
    if not symbols:
        error_messages.append("Debe contener al menos un símbolo")
    
    if not numbers:
        error_messages.append("Debe contener al menos un número")
    
    if tilde_espacio:
        error_messages.append("No debe contener tildes o espacios")
    
    if not error_messages:
        return True, None
    
    return False, error_messages


def getAllTitles(request):
    lista_titulos = []
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    
    notas = Nota.objects.filter(user_id=user_id)
    if notas:
        for nota in notas.iterator():
            lista_titulos.append(nota.titulo)
    
        return lista_titulos
    

def separarRenglones(nota):
    contenido = nota.contenido

    cadena = ""
    lista = []
    cc = 0

    for i in range(len(contenido)):
        cadena += contenido[i]
        cc += 1
        if cc == 65 or i == len(contenido) - 1:
            lista.append(cadena)
            cadena = ""
            cc = 0
            continue
    
    return lista

        
def eliminarNota(request, titulo):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id

    try:
        nota_a_eliminar = Nota.objects.get(user_id=user_id, titulo=titulo)
        nota_a_eliminar.delete()

    except(Nota.DoesNotExist):
        pass


def comprobarUser(usuario, email):
    
    try:
        user = Usuario.objects.get(username=usuario)
        if user:
            return False, "El nombre de usuario ya existe"
    
        
    
    except(Usuario.DoesNotExist):

        try:
            Usuario.objects.get(email=email)
        
        except(Usuario.DoesNotExist):
            return True, None
        
    return False, "Este email ya esta registrado en una cuenta"
