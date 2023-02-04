Proyecto-Final-Python-Nahuel Farias
Comisión: 34655
Alumno: Nahuel Farias
Proyecto: CENTRO MÉDICO MENDOZA
SuperUser: nahuelfarias Password: coder_1234
Version: 1.0

Este proyecto es desarrollado en Python utilizando el framework Django. El proyecto trata de una App web sobre un Centro Médico, la cual renderiza la información que está almacenada en la base de datos y la muestra en las diferentes vistas dependiendo cual sea la solicitud. Debajo se encuentra el link para ver la App en funcionamiento
Video Demostración.
https://drive.google.com/file/d/1L_KISdE9lyTHCzduGt4jqIOknQMalW6p/view?usp=sharing
________________________________________
DOCUMENTACIÓN.
Para poder encontrar los archivos que nombrare a posterior ingresar en la carpeta AppCoder. Los archivos son: models.py, forms.py, urls.py, views.py, la carpeta de templates, entre otros.
________________________________________
Models.py:
En este archivo podemos encontrar los modelos de datos usados por el backend.
Descripción: modelo Consultorio. Campos: -especialidad (Char, nombre de la especialidad del consultorio) –sala (Integer, número de la sala)
Descripción: modelo Paciente. Campos: -nombre (Char, nombre del paciente) -apellido (Char, apellido del paciente) -email= (Email, email del paciente) - obra_social (Char, obra social del paciente)
Descripción: modelo Médico. Campos: -nombre (Char, nombre del médico) -apellido (Char, apellido del médico) -email= (Email, email del médico) - especialidad (Char, especialidad del médico)

Descripción: modelo Avatar. Campos: -user (ForeignKey) -image (ImageField) No desarrollado

________________________________________
Forms.py:
En este archivo podemos encontrar los formularios usados para cargar los datos que quedan guardados en nuestra base de datos. Son 5 los formularios, uno por cada modelo, otro para poder registrar los usuarios nuevos y el último que sirve para editar el perfil de un usuario.
________________________________________
Urls.py:
Contiene cada una de las rutas de las vistas de la App.
________________________________________
Views.py:
Aparecen todas las vistas que se utilizan en la App. Asociado a lo anterior, por cada modelo se aplica el concepto de CRUD (Create, Read, Update, Delete); una vista de logueo, registro y edición de perfil del usuario. Además tenemos la vista para buscar una sala por su especialidad. Ejemplo de vistas (CRUD) para el Modelo Medico:
Create: vista MedicoFormulario
Read: vista leerMedico
Update: vista editarMedico
Delete: vista eliminarMedico
________________________________________
Templates:
Es una carpeta donde se encuentran todos los archivos HTML, usados por la App. Se utiliza una platilla de BOOSTRAP y se aplica el concepto de herencia a cada archivo.
________________________________________
Autor: Nahuel Farias

