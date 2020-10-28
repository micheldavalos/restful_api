from flask import Flask, jsonify
from conexion import get_usuarios

app = Flask(__name__)

@app.route("/")
def hola():
    return "<b>Hola Mundo!<b>"

# @app.route("/usuarios/<string:nombre>")
# def usuarios(nombre):
#     return "Hola %s" % nombre

@app.route("/api/v1/usuarios")
def usuarios():
    usuarios_list = get_usuarios()
    # usuario_dict = {
    #     'id': 10,
    #     'correo': 'michel@gmail.com',
    #     'contraseña': '12345678'
    # }
    # usuarios_list.append(usuario_dict)

    return jsonify(usuarios_list)


app.run()