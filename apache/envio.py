#!C:\Python\python.exe
#Librerias
import cgi
import pywhatkit as wm
import datetime

print("Content-type: text/html\n")

form = cgi.FieldStorage()

def what(numTel, mensaje, hora, minuto):
    try:
        # Convertir hora y minuto a enteros
        hora = int(hora)
        minuto = int(minuto)

        # Validar que la hora y el minuto sean válidos
        if 0 <= hora <= 23 and 0 <= minuto <= 59:
            # Formatear la hora y el minuto para el mensaje
            hora_str = str(hora).zfill(2)
            minuto_str = str(minuto).zfill(2)

            # Enviar el mensaje usando pywhatkit
            wm.sendwhatmsg(f"+{numTel}", mensaje, hora, minuto)
            print(f"Mensaje programado para enviar a las {hora_str}:{minuto_str} a {numTel}:")
            print(mensaje)
        else:
            print("Error: Hora o minuto inválido.")
    except ValueError:
        print("Error: Hora y minuto deben ser valores numéricos.")


if "mensaje" in form and "numTel" in form:
    
    #Obtenemos los parametros
    sendMsg = form['mensaje'].value
    sendNum = form['numTel'].value

    fecha_hora_actual = datetime.datetime.now()
    # Obtener la hora actual en formato de 24 horas
    hora_actual = fecha_hora_actual.hour
    # Obtener el minuto actual
    minuto_actual = fecha_hora_actual.minute

    #Ejecuta pywhat
    what(sendNum, sendMsg, hora_actual,minuto_actual+1)

    print(f"Mensaje enviado "+sendMsg)


    #funcion 
    
else:
    print("<h1>Error: No se enviaron datos válidos desde el formulario.</h1>")





  





