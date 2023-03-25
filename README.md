# Proyecto Final Ramos_Neira
Proyecto Final Python - Web Django Sistema de Gestión Hospitalaria - Ramos Neira Ana Carolina

# Pasos para probar el programa

* Ejecutar el comando: python manage.py runserver para iniciar el servidor.
* Ingresar a la aplicación: http://127.0.0.1:8000/AppCoder
* Sin necesidad de autenticarse, se visualizarán 4 opciones (Botones)
    - Opción Buscar un doctor. Permite realizar la búsqueda por especialidad de un doctor.
    - Opción Ingresar al sistema. Login del sistema da acceso a opciones solo para usuarios autorizados.
    - Opción Registrar Usuario. Formulario para poder registrar nuevos usuarios.
    - Opción Acerca de Mi. Se mostrará siempre y mostrará información del autor.
* Una vez se haya ingresado al sistema, se visualizarán las siguientes opciones:
    - Opción Doctor. Mostrará un listado de los doctores registrados. Se presentarán sub opciones:
        - Detalle: Mostrar el detalle de la información de un doctor seleccionado.
        - Borrar: Para eliminar un registro de doctor de la base de datos.
        - Actualizar: Para actualizar la información de un doctor.
        - Nota: Se registrará información de auditoría en los campos creado_por y creado_el.
    - Opción Paciente. Mostrará un listado de los pacientes registrados. Se presentarán sub opciones:
        - Detalle: Mostrar el detalle de la información de un paciente seleccionado.
        - Borrar: Para eliminar un registro de un paciente de la base de datos.
        - Actualizar: Para actualizar la información de un paciente.    
        - Nota: Se registrará información de auditoría en los campos creado_por y creado_el.
    - Opción Medicinas. Mostrará un listado de medicinas registradas. Se presentarán sub opciones:
        - Detalle: Mostrar el detalle de la información de una medicina seleccionado.
        - Borrar: Para eliminar un registro de una medicina de la base de datos.
        - Actualizar: Para actualizar la información de una medicina.
        - Nota: Se registrará información de auditoría en los campos creado_por y creado_el.
    - Opción Perfil. Para registrar una imagen avatar de un usuario (Esta imagen se visualizará en la parte superior derecha).
    - Opción Salir. Se mostrará el nombre del usuario autenticado, al dar clic se cerrará la sesión.
        

# Video Demo:
https://drive.google.com/drive/folders/17XnsAzE4oQg7o4E2QPBFUbcw5XMAwdDn?usp=sharing


