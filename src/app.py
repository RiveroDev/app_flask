from flask import Flask

app = Flask('__main__')

@app.route('/')     #forma de hacer una ruta 1
def index():
    return 'Hola Richard'

def hola_mundo():
    return 'Hola mundo Richard'

def prueba_de_vista1():
    return  '<h1> esto es una pruba de vista de como se comporta el interprete </h1>'

if __name__=='__main__':

    app.add_url_rule('/hola', view_func= hola_mundo) #forma de hacer una ruta 2

    app.add_url_rule('/Codigo_facil', view_func= prueba_de_vista1)
    app.run( debug=True, port=3500)



