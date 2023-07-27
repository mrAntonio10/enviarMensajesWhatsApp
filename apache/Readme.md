# Este es un formulario simple para enviar mensajes por whats
    Este mini proyecto se encarga de abrir en tu navegador "WHATSAPP.WEB" (Debes de iniciar sesion en tu navegador por defecto)
    El mensaje se ejecutará de tu hora actual +1 minuto.
    DATO: No se envia automáticamente.
 
 **PARA UTILIZARLO EN APACHE DEBES SEGUIR LOS SIGUIENTES PASOS**
##    1. Copiar el fichero "envio.py" de apache en la ruta > Apache24/cgi-bin. 

 ##   2. Manejar las librerias de pywhat
        **INICIA TU CMD O TERMINAL
            **procede a copiar los siguientes codigos

```
         pip install virtualenv
         virtualenv env
         env\Scripts\activate.bat
         pip install virtualenvwrapper-win
	       pip install pywhatkit
```

  ##  3. Y PASO MAS IMPORTANTE!! REVISA EL ARCHIVO HTTPD.CONF DE APACHE24
	Ruta: Apache24/conf/httpd.conf
	
	Abre el fichero en un editor de texto y verifica que la siguiente linea esté descomentada: 
		-> LoadModule cgi_module modules/mod_cgi.so (Sin # por delante).

Cualquier consulta contactame en mi cuenta o a mi correo:
	marcorocadota@gmail.com :D

Santa Cruz - Bolivia : 27/Julio/2023.
Marco Antonio Roca Montenegro.
