from logging import debug
from flask import Flask #importamos la libreria Flask


app = Flask(__name__) #creamos una variablle donde guardaremos nuestra
#aplicación utilizando la instancia de Flask

"""
@app.route('/') #Con esto creamos una ruta de enlace para la vista del navegador, en este caso es la ruta raíz.
def index(): #Creamos un método que nos devolverá un texto en el navegador.
    return "Cybermito Web"
"""
def index():
    return "Bienvenidos a mi nueva aplicación"

@app.route('/holamundo') #definimos una segunda ruta, para una segunda vista (página web)
def hola_mundo(): #Definimos una segunda vista (página web), en estos casos solo devolvemos un texto plano.
    return "Hola Mundo"

if __name__ == '__main__': #Comprobamos si vamos a lanzar la aplicación como principal.
    app.add_url_rule('/', view_func=index)#Esta es otra manera de crear una ruta, en el primer argumento
                                          #definimos la ruta, en este caso la raíz del documento, después,
                                          #en el segundo argumento indicamos cuál es la vista llamando al método
                                          #función que la contiene, en este caso index.
    app.run(debug=True, port=8000) #iniciamos el servidor con el método run, le indicamos con dos argumentos,
                                   #que lo queremos arrancar en modo debug (Esto hace que se refresque el servidor vez
                                   # que actualicemos y grabemos el proyecto.) En el segundo argumento le indicamos el
                                   #puerto que queremos utilizar para nuestra aplicación.
