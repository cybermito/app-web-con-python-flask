from logging import debug
from flask import Flask, render_template  # importamos la libreria Flask, el renderizador de plantillas


app = Flask(__name__)  # creamos una variablle donde guardaremos nuestra
# aplicación utilizando la instancia de Flask

"""
@app.route('/') #Con esto creamos una ruta de enlace para la vista del navegador, en este caso es la ruta raíz.
def index(): #Creamos un método que nos devolverá un texto en el navegador.
    return "Cybermito Web"
"""


def index():
    #return "<h1>Bienvenid@ a mi nueva aplicación</h1>"
    #return render_template('index.html', titulo="Página principal") #Enviamos el titulo para nuestra página web.
    #Creamos un diccionario con los valores que queremos enviar a nuestra plantilla para que se rendericen
    data = {
        'titulo':'Página principal',
        'encabezado':'Bienvenid@ a mi nueva app'
    }
    return render_template('index.html', data=data)

# definimos una segunda ruta, para una segunda vista (página web)
@app.route('/holamundo')
# Definimos una segunda vista (página web), en estos casos solo devolvemos un texto plano.
def hola_mundo():
    return "Hola Mundo, ¿eres un bot?"


# Comprobamos si vamos a lanzar la aplicación como principal.
if __name__ == '__main__':
    # Esta es otra manera de crear una ruta, en el primer argumento
    app.add_url_rule('/', view_func=index)
    # definimos la ruta, en este caso la raíz del documento, después,
    # en el segundo argumento indicamos cuál es la vista llamando al método
    # función que la contiene, en este caso index.
    # iniciamos el servidor con el método run, le indicamos con dos argumentos,
    app.run(debug=True, port=8000)
    # que lo queremos arrancar en modo debug (Esto hace que se refresque el servidor vez
    # que actualicemos y grabemos el proyecto.) En el segundo argumento le indicamos el
    # puerto que queremos utilizar para nuestra aplicación.
