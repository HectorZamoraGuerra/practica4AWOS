from flask import Flask, render_template, request, jsonify, make_response, session

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/preguntas')
def productos():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_24005037_usr",
        password="N&2lbK=8;Mrt",
        database="u760464709_24005037_bd"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Preguntas")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
