from flask import Flask
from flask import request, make_response, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
import datetime, json, hashlib, os, jwt

app = Flask(__name__, static_url_path='/static')
CORS(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anuj@1996'
app.config['MYSQL_DB'] = 'nanoheal'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)



# Show all movies
@app.route('/home',methods=['GET'])
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("""select * from movies""")
    results = cursor.fetchall()
    cursor.close()
    items = []
    for item in results:
        items.append(item)
    return json.dumps(items)
    
#Add Movie
@app.route('/addmovies',methods=['POST'])
def addmovies():
    name = request.headers.get('name')
    category = request.headers.get('category')
    description = request.headers.get('description')
    if request.method == 'POST':
        f = request.files['image']
        location = "static/img/" + f.filename
        f.save(location)
    cursor = mysql.connection.cursor()
    cursor.execute(""" INSERT INTO movies(name ,category, description, image) values (%s,%s,%s,%s)""",[name ,category,description,location])
    mysql.connection.commit()
    cursor.close()
    return json.dumps("Registerd Successfully")

#Edit Movie
@app.route('/edit', methods=['POST'])
def edit():
    id = request.headers.get('id')
    name = request.headers.get('name')
    category = request.headers.get( 'category')
    description = request.headers.get('description')
    if request.method == 'POST':
        f = request.files['image']
        location = "static/img/" + f.filename
        f.save(location)
    cursor = mysql.connection.cursor()
    cursor.execute("""update movies set name =(%s), category=(%s), description = (%s), image = (%s) where id=(%s)""",[name, category,description,location,id])
    mysql.connection.commit()
    cursor.close()
    return json.dumps("Edited Successfully")

#Delete Movie
@app.route('/delete',methods=["POST"])
def delete():
    id =request.headers.get('id')
    cursor = mysql.connection.cursor()
    cursor.execute("""delete from movies where id =(%s)""",[id])
    mysql.connection.commit()
    cursor.close()
    return json.dumps("Delete Successfully")

#Search Movie By name
@app.route('/search')
def search():
    name = request.headers.get('name')
    cursor = mysql.connection.cursor()
    search_string = f"%{name}%"
    cursor.execute("""select * from movies where name like (%s)""", [search_string])
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug = True)