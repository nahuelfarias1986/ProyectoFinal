from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Consultorio)

admin.site.register(Paciente)

admin.site.register(Medico)

admin.site.register(Avatar)

