# APIS SLC 💚 :) [![@SamanthaRojasH](https://i.imgur.com/skj3q6L.png?2 "@SamanthaRojasH")](https://i.imgur.com/skj3q6L.png?2 "@SamanthaRojasH")

Este es el primer proyecto que he logrado desarrollar con los conocimientos adquiridos en [Platzi](https://platzi.com/ "Platzi") y en otras fuentes de conocimiento. Está desarrollado con Flask en el lenguaje Python con conexión a MongoDB y MySQL. Este proyecto fue desarrollado para contribuir con mi trabajo como voluntaria en la comunidad Scrum Latam, a la cual me siento muy orgullosa de pertenecer.


> Si quieres conocer un poco más de mi, puedes hacerlo en:
>
> - [LinkedIn Sandra](https://www.linkedin.com/in/sandra-rojas-herran/ "LinkedIn")
> - [Twitter @SamanthaRojasH](https://twitter.com/SamanthaRojasH "Twitter @SamanthaRojasH")

## Recomendaciones para usar el proyecto
* Crear nuestro entorno virtual en la carpeta del proyecto.
* Crea tu archivo config.ini, según la configuración de mongoDB:

```
; config.ini
[DEFAULT]
CONNECTION_DB = connection_string
DB = db
COLLECTION = db_collection
    
[TESTING]
CONNECTION_DB = connection_string_testing
DB = db_testing
COLLECTION = db_collection_testing
    
[PRODUCTION]
CONNECTION_DB = connection_string_production
DB = db_production
COLLECTION = db_collection_production
```

* Si lo vas en tu ambiente local sigue, ejecuta los siguientes comandos, si eres SO Windows:

```
	- set FLASK_APP=./app.py
	- set FLASK_ENV=development
	- flask run
```

> **Haz tus proyectos con amor y con pasión y lograrás grandes éxitos.**
