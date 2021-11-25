import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import Flask, request, render_template
import sys

@app.route('/')
def rest():    
    return render_template('index.html')

@app.route('/Events_Active_Community')
def Events_Active_Community():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT count(*) Events_Active_Community FROM SLC_community_all")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/Registered_Webinars')
def Registered_Webinars():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT count(*) Registered_Webinars FROM SLC_webinar")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/Participants_Per_Webinar')
def Participants_Per_Webinar():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT W.webinar Webinar_Name, count(P.email) Participants FROM SLC_Participants P, SLC_webinar W where P.id_webinar = W.id_webinar group by P.id_webinar ORDER by Participants")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/Participations_Per_Country')
def Participations_Per_Country():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT CO.Country, count(c.email) Participants FROM SLC_community_all c, SLC_Country CO where CO.ID_Country = c.ID_Country group by c.ID_Country ORDER by Participants")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/followers')
def followers():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT SN.Social_Network, sum(FD.Total_Follower) FROM SLC_Followers_Date FD, SLC_Social_Network SN where SN.ID_Network = FD.ID_Network GROUP by FD.ID_Network ORDER BY Total_Follower")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

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