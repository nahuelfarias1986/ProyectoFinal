from django.urls import path

from AppCoder import views

from django.contrib.auth.views import LogoutView




urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('consultorios', views.consultorios, name="Consultorios"),
    path('medicos', views.medicos, name="Medicos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    
    path('consultorioFormulario', views.ConsultorioFormulario, name="ConsultorioFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaSala',  views.busquedaSala, name="BusquedaSala"),
    path('buscar/', views.buscar),
    path('leerMedicos', views.leerMedicos, name = "LeerMedicos"),
    path('eliminarMedico/<medico_nombre>/', views.eliminarMedico, name="EliminarMedico"),
    path('editarMedico/<medico_nombre>/', views.editarMedico, name="EditarMedico"),
    
   path('consultorio/list', views.ConsultorioList.as_view(), name='List'),
   path(r'^(?P<pk>\d+)$', views.ConsultorioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ConsultorioCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ConsultorioUpdate.as_view(), name='Edit'),
   path(r'^borrar/(?P<pk>\d+)$', views.ConsultorioDelete.as_view(), name='Delete'),
   path('leerPacientes', views.leerPacientes, name = "LeerPacientes"),
   path('eliminarPaciente/<paciente_nombre>/', views.eliminarPaciente, name="EliminarPaciente"),
   path('editarPaciente/<paciente_nombre>/', views.editarPaciente, name="EditarPaciente"),

   path('login', views.login_request, name="Login"),

   path('register', views.register, name='Register'),

   path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
   path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
   
   path('Nosotros', views.Nosotros, name='Nosotros'),








]

