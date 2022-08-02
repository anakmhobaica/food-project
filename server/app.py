from flask import request, Flask, redirect, url_for, jsonify
from datetime import datetime
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

DB = psycopg2.connect(
    user="postgres", 
    password="1234", 
    database="proyecto", 
    host="localhost", 
    port="5432",
    cursor_factory=RealDictCursor
)

cursor = DB.cursor()

print("Successfully connected!!")

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/recetas', methods=['POST', 'GET'])
def recetas():
    if request.method == 'POST':
        json = request.json
        cursor.execute("INSERT INTO recetas (id_receta, imagen, titulo, tiempo, dificultad, parrafo, categoria, ingredientes, procedimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (json['id_receta'], json['imagen'], json['titulo'], json['tiempo'], json['dificultad'], json['parrafo'], json['categoria'], json['ingredientes'], json['procedimiento']))
        cursor.execute("INSERT INTO auditoria (nombre_tabla, operacion, nuevo_valor, fecha, usuario) VALUES (%s, %s, %s, %s, %s)", ('recetas', 'INSERT', json['titulo'], str(datetime.now()), json['usuario']))
        DB.commit()
        return redirect(url_for('recetas'))
    else:
        categoria = request.args.get('categoria', default='')
        if categoria == 'Fit':
            cursor.execute("SELECT * FROM recetas WHERE categoria='Fit';")
        elif categoria == 'Fat':
            cursor.execute("SELECT * FROM recetas WHERE categoria='Fat';")
        else:
            cursor.execute("SELECT * FROM recetas;")
        receta = cursor.fetchall()
        recetas = []
        for row in receta:
            recetas.append(dict(row))
        return jsonify(recetas)

@app.route('/recetas/<id_receta>')
def paginaReceta(id_receta):
    query = "SELECT * FROM recetas WHERE id_receta= %s;"
    cursor.execute(query, (id_receta,))
    receta = cursor.fetchall()
    recetas = []
    for row in receta:
        recetas.append(dict(row))
    return jsonify(recetas)
        
@app.route('/curiosidades', methods=['GET', 'POST'])
def curiosidades():
    if request.method == 'POST':
        json = request.json
        cursor.execute("INSERT INTO curiosidades (id_curiosidad, imagen, titulo, parrafo) VALUES (%s, %s, %s, %s)", (json['id_curiosidad'], json['imagen'], json['titulo'], json['parrafo']))
        cursor.execute("INSERT INTO auditoria (nombre_tabla, operacion, nuevo_valor, fecha, usuario) VALUES (%s, %s, %s, %s, %s)", ('curiosidades', 'INSERT', json['titulo'], str(datetime.now()), json['usuario']))
        DB.commit()
        return redirect(url_for('curiosidades'))
    else:
        cursor.execute("SELECT * FROM curiosidades;")
        curiosidad = cursor.fetchall()
        curiosidades = []
        for row in curiosidad:
            curiosidades.append(dict(row))
        return jsonify(curiosidades)

@app.route('/eliminar-receta/<id_receta>', methods=['DELETE'])
def eliminarReceta(id_receta):
    usuario = request.args.get('usuario', default='')
    cursor.execute('SELECT * FROM recetas WHERE id_receta = %s;', (id_receta,))
    receta_eliminada = cursor.fetchone()
    cursor.execute("INSERT INTO auditoria (nombre_tabla, operacion, nuevo_valor, fecha, usuario) VALUES (%s, %s, %s, %s, %s)", ('recetas', 'DELETE', receta_eliminada['titulo'], str(datetime.now()), usuario))
    query = 'DELETE FROM recetas WHERE id_receta = %s;'
    cursor.execute(query, (id_receta,))
    DB.commit()
    cursor.execute('SELECT * FROM recetas;')
    receta = cursor.fetchall()
    recetas = []
    for row in receta:
        recetas.append(dict(row))
    return jsonify(recetas)

@app.route('/eliminar-curiosidad/<id_curiosidad>', methods=['DELETE'])
def eliminarCuriosidad(id_curiosidad):
    usuario = request.args.get('usuario', default='')
    cursor.execute('SELECT * FROM curiosidades WHERE id_curiosidad = %s;', (id_curiosidad,))
    curiosidad_eliminada = cursor.fetchone()
    cursor.execute("INSERT INTO auditoria (nombre_tabla, operacion, nuevo_valor, fecha, usuario) VALUES (%s, %s, %s, %s, %s)", ('curiosidades', 'DELETE', curiosidad_eliminada['titulo'], str(datetime.now()), usuario))
    query = 'DELETE FROM curiosidades WHERE id_curiosidad = %s;'
    cursor.execute(query, (id_curiosidad,))
    DB.commit()
    cursor.execute('SELECT * FROM curiosidades;')
    curiosidad = cursor.fetchall()
    curiosidades = []
    for row in curiosidad:
        curiosidades.append(dict(row))
    return jsonify(curiosidades)

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # session.permanent = False
        json = request.get_json()
        email_found = 'SELECT * FROM usuarios WHERE correo = %s'
        cursor.execute(email_found, (json['correo'],))
        correo = cursor.fetchone()
        # session['usuario'] = json['nombre']
        if correo:
            print('Este email ya existe en la base de datos.')
            return jsonify({'codigo': 400, 'mensaje': "El email ya existe."})
        else:
            user_found = 'SELECT * FROM usuarios WHERE nombre = %s'
            cursor.execute(user_found, (json['nombre'],))
            usuario = cursor.fetchone()
            if usuario:
                print('Este nombre de usuario ya existe en la base de datos.')
                return jsonify({'codigo': 401, 'mensaje': "El nombre de usuario ya existe."})
            else:
                cursor.execute('INSERT INTO usuarios (nombre, contrasena, correo, tipo_usuario) VALUES (%s, %s, %s, %s)', (json['nombre'], json['contrasena'], json['correo'], json['tipo_usuario']))
                DB.commit()
                return jsonify({'codigo': 201, 'mensaje': "Bienvenido!", 'user':dict(usuario)})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        json = request.get_json()
        user_found = 'SELECT * FROM usuarios WHERE nombre = %s AND contrasena = %s'
        cursor.execute(user_found, (json['nombre'], json['contrasena'],))
        account = cursor.fetchone()
        account = dict(account)
        if account:
            print("entraste")
            return jsonify({'codigo': 200, 'mensaje': "Bienvenido!", 'user':account})
        else:
            return jsonify({'codigo': 403, 'mensaje': "Credenciales Inválidas."})

    
if __name__ == '__main__':
    app.run()