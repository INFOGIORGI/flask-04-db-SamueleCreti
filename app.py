from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

#Connessione al Database
app.config['MYSQL_HOST'] = "138.41.20.102"
app.config['MYSQL_PORT'] = "53306"
app.config['MYSQL_USER'] = "ospite"
app.config['MYSQL_PASSWORD'] = "ospite"
app.config['MYSQL_DB'] = "w3schools"

#Creazione oggetto mysql
mysql = MySQL(app)

@app.route("/")
def homepage():
    return render_template("home.html", titolo="Home")

@app.route("/products")
def products():
    #Creazione cursore e interrogazione al Database
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    
    #Il cursore esegue la query
    cursor.execute(query)

    #Il risultato della query viene memorizzato in una tupla di tuple chiamata dati
    dati = cursor.fetchall()
    print(dati)
    return render_template("products.html", titolo="Products", dati=dati)


if __name__ == '__main__': 
    app.run(debug=True)
