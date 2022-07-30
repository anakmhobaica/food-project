from crypt import methods
from flask import request, Flask, redirect, url_for, jsonify
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
    query = 'DELETE FROM recetas WHERE id_receta = %s;'
    cursor.execute(query, (id_receta,))
    receta = cursor.fetchall()
    recetas = []
    for row in receta:
        recetas.append(dict(row))
    return jsonify(recetas)


if __name__ == '__main__':
    app.run()