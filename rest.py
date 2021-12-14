import pymysql
from app import app
from db import mysql
from flask import jsonify
from flask import Flask, request, render_template
import itertools

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
		rows = {}
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		
		cursor.execute("SELECT SN.Social_Network, FD.Total_Follower FROM SLC_Followers_Date FD, SLC_Social_Network SN where SN.ID_Network = FD.ID_Network AND SN.Social_Network = 'LinkedIn'")
		
		result = 0
		for row in cursor:
			Social_Network = row['Social_Network']
			Total_Follower = int(row['Total_Follower'])
			result = result + Total_Follower
		print()
		print("Nuestra red social {} tiene {} seguidores".format(Social_Network, result))
		rows[Social_Network] = result

		cursor.execute("SELECT SN.Social_Network, FD.Total_Follower FROM SLC_Followers_Date FD, SLC_Social_Network SN where SN.ID_Network = FD.ID_Network AND SN.Social_Network = 'Facebook'")
		
		result = 0
		for row in cursor:
			Social_Network = row['Social_Network']
			Total_Follower = int(row['Total_Follower'])
			result = result + Total_Follower
		
		print("Nuestra red social {} tiene {} seguidores".format(Social_Network, result))
		print()
		rows[Social_Network] = result
		
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