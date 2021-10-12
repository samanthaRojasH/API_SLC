import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import Flask, request, render_template
import dns
import Mongodb
import sys

@app.route('/')
def rest():    
    return render_template('index.html')

@app.route('/participants')
def participants():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT count(*) participants FROM SLC_community_all")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/webinars')
def webinars():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT count(*) webinars FROM SLC_webinar")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/login')
def login():    
    return render_template('login.html')

@app.route('/tools')
def tools():    
    return render_template('tools.html')

@app.route("/procesar", methods=['POST'])
def procesar():
    username = request.form.get("username")
    password = request.form.get("password")

    database = Mongodb.client["imageBot"]
    collection = database["imageBotCT"]

    usern = collection.find_one({"username":{"$in":[username]}})
    for i in usern:
        
        if usern[i] == password:
            passwordFind = usern[i]            
        elif usern[i] == username: 
            usernameFind = usern[i]
        else:
            usernameFind = ""
            passwordFind = ""
    
    Mongodb.client.close()
    if(usernameFind == username and passwordFind == password):
        return render_template("tools.html", username=username)
    
    return render_template("AccessDenied.html")

@app.route('/join_databases')
def join():    
    return render_template('join_databases.html')

@app.route("/joinFiles", methods=['POST'])
def joinFiles():
    directory = request.form.get("files")
    return render_template('Upload.html', directory=directory)

@app.route('/load_databases')
def load_databases():    
    return render_template('load_databases.html')

@app.route('/procesarscript', methods=['POST'])
def procesarscript():   
	namefinal = str(request.files["files"])	
	filenameH = namefinal[15:31]
	return render_template('run_databases.html', filenameH=filenameH)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()