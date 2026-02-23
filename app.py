from flask import Flask, render_template, request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/productos')
def productos():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="46.28.42.226",
        user="u760464709_prueba_usr",
        password="|Au/mc*H2jH3",
        database="u760464709_prueba_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM productos")
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult))
