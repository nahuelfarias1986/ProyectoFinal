
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse , redirect
from django.http import HttpResponse
from AppCoder.models import Consultorio , Medico , Paciente
from AppCoder.forms import ConsultorioFormulario, MedicoFormulario , PacienteFormulario , UserRegisterForm, UserEditForm

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse



@login_required
def consultorio(request):
      consultorio =  Consultorio(especialidad="Traumatologia", sala="2")
      consultorio.save()
      documentoDeTexto = f"--->Consultorio: {consultorio.especialidad}   Sala: {consultorio.sala}"

      return HttpResponse(documentoDeTexto)




def inicio(request):

      return render(request, "AppCoder/inicio.html")

@login_required
def consultorios(request):

      return render(request, "AppCoder/consultorios.html")

@login_required
def medicos(request):

      return render(request, "AppCoder/medicos.html")


@login_required
def pacientes(request):

      return render(request, "AppCoder/pacientes.html")



def Nosotros(request):

      return render (request, "AppCoder/Nosotros.html")



@login_required
def buscar(request):
      if  request.GET["especialidad"]:
            #respuesta = f"Estoy buscando la especialidad: {request.GET['especialidad'] }" 
            especialidad= request.GET['especialidad'] 
            sala = Consultorio.objects.filter(especialidad__icontains=especialidad)
            return render(request, "AppCoder/inicio.html", { "sala":sala , "especialidades":especialidad})
      else:
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

@login_required
def medicos(request):

      if request.method == 'POST':

            miFormulario = MedicoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  medico = Medico (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], especialidad=informacion['especialidad']) 

                  medico.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= MedicoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/medicos.html", {"miFormulario":miFormulario})


def leerMedicos(request):

      medicos = Medico.objects.all() #trae todos los profesores

      contexto= {"medicos": medicos} 

      return render(request, "AppCoder/leerMedicos.html",contexto)



def eliminarMedico(request, medico_nombre):

    medico = Medico.objects.get(nombre=medico_nombre)
    medico.delete()

    # vuelvo al menú
    medicos = Medico.objects.all()  # trae todos los médicos

    contexto = {"medicos": medicos}

    return render(request, "AppCoder/inicio.html", contexto)




def editarMedico(request, medico_nombre):

    # Recibe el nombre del médico que vamos a modificar
    medico = Medico.objects.get(nombre=medico_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = MedicoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            medico.nombre = informacion['nombre']
            medico.apellido = informacion['apellido']
            medico.email = informacion['email']
            medico.especialidad = informacion['especialidad']
            

            medico.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = MedicoFormulario(initial={'nombre': medico.nombre, 'apellido': medico.apellido,
                                                   'email': medico.email, 'especialidad': medico.especialidad, })

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarMedico.html", {"miFormulario": miFormulario, "medico_nombre": medico_nombre})


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ConsultorioList(ListView):

    model = Consultorio
    template_name = "AppCoder/consultorios_list.html"

class ConsultorioDetalle(DetailView):

    model = Consultorio
    template_name = "AppCoder/consultorio_detalle.html"

class ConsultorioCreacion(CreateView):

    model = Consultorio
    success_url = "/AppCoder/consultorio/list"
    fields = ['especialidad', 'sala']

class ConsultorioUpdate(UpdateView):

    model = Consultorio
    success_url = "/AppCoder/consultorio/list"
    fields = ['especialidad', 'sala']

class ConsultorioDelete(DeleteView):

    model = Consultorio
    success_url = "/AppCoder/consultorio/list"



@login_required
def consultorios(request):
      if request.method == 'POST':
            miFormulario = ConsultorioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  consultorio = Consultorio (especialidad=informacion['especialidad'], sala=informacion['sala']) 
                  consultorio.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= ConsultorioFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/consultorios.html", {"miFormulario":miFormulario})

@login_required
def pacientes(request):

      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  paciente = Paciente (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], obra_social=informacion['obra_social'],) 

                  paciente.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PacienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/pacientes.html", {"miFormulario":miFormulario})


def leerPacientes(request):

      pacientes = Paciente.objects.all() #trae todos los profesores

      contexto= {"pacientes": pacientes} 

      return render(request, "AppCoder/leerPacientes.html",contexto)



def eliminarPaciente(request, paciente_nombre):

    paciente = Paciente.objects.get(nombre=paciente_nombre)
    paciente.delete()

    # vuelvo al menú
    pacientes = Paciente.objects.all()  # trae todos los pacientes

    contexto = {"pacientes": pacientes}

    return render(request, "AppCoder/inicio.html", contexto)




def editarPaciente(request, paciente_nombre):

    # Recibe el nombre del estudiante que vamos a modificar
    paciente = Paciente.objects.get(nombre=paciente_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = PacienteFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            paciente.nombre = informacion['nombre']
            paciente.apellido = informacion['apellido']
            paciente.email = informacion['email']
            paciente.obra_social = informacion['obra_social']

            paciente.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = PacienteFormulario(initial={'nombre': paciente.nombre, 'apellido': paciente.apellido,
                                                   'email': paciente.email, 'obra_social': paciente.obra_social})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarPaciente.html", {"miFormulario": miFormulario, "paciente_nombre": paciente_nombre})


from django.contrib.auth.decorators import login_required

# Vista de login
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})



# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})




@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")



# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
