from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

#Connessione al Database
app.config['MYSQL_HOST'] = "138.41.20.102"
app.config['MYSQL_PORT'] = 53306  #Deve essere intero
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
    cursor.close()

    return render_template("products.html", titolo="Products", dati=dati)

@app.route("/categories/<categoryID>")
def categories(categoryID):
    #Creazione cursore e interrogazione al Database
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    
    #Il cursore esegue la query
    cursor.execute(query)

    #Il risultato della query viene memorizzato in una tupla di tuple chiamata dati
    dati = cursor.fetchall()
    print(dati)
    
    l=[]
    for i in dati:
        if i[3] == categoryID:
            l.append(i)

    cursor.close()
    return render_template("categories.html", titolo="Categories", categoryID=categoryID, l=l)

if __name__ == '__main__': 
    app.run(debug=True)
