from flask import Flask #importamos la libreria Flask


app = Flask(__name__) #creamos una variablle donde guardaremos nuestra
#aplicación utilizando la instancia de Flask

if __name__ == '__main__': #Comprobamos si vamos a lanzar la aplicación como principal.
    app.run() #iniciamos el servidor con el método run
