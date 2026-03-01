from flask import Flask, render_template, request, jsonify, make_response, session

from flask_cors import CORS, cross_origin
import mysql.connector
app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005037_usr",
        password="N&2lbK=8;Mrt",
        database="u760464709_24005037_bd"
    )


@app.route('/preguntas')
def preguntas():

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Preguntas")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))

@app.post('/insertarPregunta')
def insertar_pregunta():

    mycursor = mydb.cursor()
    sql = "CALL CrearPregunta(%s, %s, %s)"
    val = (request.form["txtPregunta"], request.form["cboCurso"], request.form["txtValor"])
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"

@app.post('/modificarPregunta')
def modificar_pregunta():

    mycursor = mydb.cursor()
    sql = "call ModificarPregunta(%s,%s,%s,%s)"
    val = (request.form["cboCurso"], request.form["txtValor"], request.form["txtPregunta"],request.form["txtId"])
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"

@app.post('/eliminarPregunta')
def eliminar_pregunta():

    mycursor = mydb.cursor()
    sql = "call EliminarPregunta(%s)"
    val = (request.form["txtId"],)
    mycursor.execute(sql, val)
    mydb.commit()
    return "correcto"
