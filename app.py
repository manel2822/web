from logging.handlers import DatagramHandler
from flask import Flask, render_template

from flask import jsonify
import json
import random


# Step_1
from flaskext.mysql import MySQL

app = Flask(__name__)
# Step_2
mysql = MySQL()

# Step_4
app.config['MYSQL_DATABASE_HOST'] 	  = 'localhost'
app.config['MYSQL_DATABASE_PORT'] 	  = 3306
app.config['MYSQL_DATABASE_USER'] 	  = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Liiamsra*&M4n3l'
app.config['MYSQL_DATABASE_DB'] 	  = 'db_university'

pourcentage=[]
pourcentagetotale=[100,100,100]
# Step_3
mysql.init_app(app)
app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/api/data')
def doGetData():
	
		
	Data = {"years":[],"datasets":[]}
	conn = mysql.connect()	
	cursor =conn.cursor()
	cursor.execute("SELECT distinct  annee from  db_university.resultats")	
	annee_tuple = cursor.fetchall()
	annee_list =  [item[0] for item in annee_tuple]
	Data["years"]=annee_list
	cursor.execute("SELECT count(matricule) ,annee  from  db_university.resultats where resultats.moyenne>10 group by annee")	
	value_tuple = cursor.fetchall()
	value_succ=([item[0] for item in value_tuple])
    
	Data["datasets"].append({"label":"admitted","data":value_succ,"type":"bar"}),

    
	cursor.execute("SELECT count(matricule) ,annee  from  db_university.resultats where resultats.moyenne<10 group by annee")	
	value_tuple = cursor.fetchall()
	value_fail=([item[0] for item in value_tuple])


	cursor.execute("SELECT count(matricule) ,annee  from  db_university.resultats  group by annee")	
	value_tuple = cursor.fetchall()
	value_all=([item[0] for item in value_tuple])  

	for i in range(len(value_all) ):
		pourcentage.append( round((100-((value_succ[i]*100)/value_all[i])),2))
    

	Data["datasets"].append({"label":"failed","data": value_fail,"type":"line"}),	
        
	data_JSON = json.dumps(Data)	
	return data_JSON 














annee=2021
@app.route('/api/data1')
def doGetData1():
	conn = mysql.connect()	
	cursor =conn.cursor()	
	cursor.execute("SELECT distinct  annee from  db_university.resultats ")	

	annee_tuple = cursor.fetchall()
	annee_list =  [item[0] for item in annee_tuple]

	cursor.execute("SELECT count(matricule)as failed ,specialite from  db_university.resultats  where resultats.moyenne<10 and annee='"+str(annee)+"'  group by specialite ,annee")	

	data = cursor.fetchall()	
	row_headers=[x[0] for x in cursor.description]

	cursor.close()

	json_data=[]
	for result in data:
		json_data.append(dict(zip(row_headers,result)))					
	return jsonify(json_data)			


	
		
	
@app.route('/api/data2')
def doGetData2():
	
	Data = {"years":[],"datasets":[]}
	conn = mysql.connect()	
	cursor =conn.cursor()
	cursor.execute("SELECT distinct   annee from  db_university.resultats")	
	annee_tuple = cursor.fetchall()
	annee_list =  [item[0] for item in annee_tuple]
	Data["years"]=annee_list

	cursor.execute("SELECT distinct  specialite from  db_university.resultats")	
	sp_tuple = cursor.fetchall()
	sp_list =  [item[0] for item in sp_tuple]
    
	for sp  in sp_list:
        
		cursor.execute("SELECT  avg(moyenne)  from  db_university.resultats where specialite='"+sp+"'  group by annee ")	
		value_tuple = cursor.fetchall()
		value_list=[item[0] for item in value_tuple]

		Data["datasets"].append({"label":sp
		,"data": value_list}),	
	
		
        
	data_JSON = json.dumps(Data)	
	return data_JSON 














@app.route('/api/data3')
def doGetData3():
	
	Data = {"label":[],"datasets":[]}
    
	conn = mysql.connect()	
	cursor =conn.cursor()
	 
	cursor.execute("SELECT distinct  specialite from  db_university.resultats" )		
	sp_tuple = cursor.fetchall()
	sp_list =  [item[0] for item in sp_tuple]
	Data["label"]=sp_list

	cursor.execute("SELECT distinct  sexe from  db_university.resultats" )		
	sx_tuple = cursor.fetchall()
	sx_list =  [item[0] for item in sx_tuple]
	for sx  in sx_list:
		cursor.execute("SELECT count(matricule)  from  db_university.resultats  where sexe='"+sx+"'  group by specialite "),	
	    
		value_tuple = cursor.fetchall()
		value_list=[item[0] for item in value_tuple]
		Data["datasets"].append({"label":sx,"backgroundColor":"#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)]),"data": value_list}),	
	
	data_JSON = json.dumps(Data)	
	return data_JSON 
	







@app.route('/api/data4')
def doGetData4():
	data = []
	conn = mysql.connect()	
	cursor =conn.cursor()
	cursor.execute("SELECT distinct  specialite from  db_university.resultats")	
	sp_tuple = cursor.fetchall()
	sp_list =  [item[0] for item in sp_tuple]

	cursor.execute("SELECT count(matricule)  from  db_university.resultats  group by specialite")	
	value_tuple = cursor.fetchall()
	total_sp=([item[0] for item in value_tuple])

	cursor.execute("SELECT count(matricule)  from  db_university.resultats where resultats.moyenne>10 group by specialite")	
	value_tuple = cursor.fetchall()
	sp_succ=([item[0] for item in value_tuple])

	for i in range(len(total_sp) ):
         
		data.append({"specialite":sp_list[i], "total":( round(((sp_succ[i]*100)/total_sp[i]),2))}),

	data_JSON = json.dumps(data)
	return data_JSON

    


@app.route('/api/data5')
def doGetData5():
	data = {"years":[],"datasets":[]}
	
	conn = mysql.connect()	
	cursor =conn.cursor()
	cursor.execute("SELECT  annee from  db_university.resultats  group by annee")	
	annee_tuple = cursor.fetchall()
	annee_list =  [item[0] for item in annee_tuple]
	data["years"]=annee_list
	for annee in annee_list:
		cursor.execute("SELECT count(matricule) as student from  db_university.resultats   WHERE annee="+str(annee)+"")	
		student_tuple = cursor.fetchall()
		student_list =  [item[0] for item in student_tuple]
	  
		data["datasets"].append(student_list[0]),	
        
	data_JSON = json.dumps(data)	
	return data_JSON 	



@app.route('/api/data6')
def doGetData6():
	
	Data = {"years":[],"datasets":[]}
	conn = mysql.connect()	
	cursor =conn.cursor()
	cursor.execute("SELECT distinct   annee from  db_university.resultats")	
	annee_tuple = cursor.fetchall()
	annee_list =  [item[0] for item in annee_tuple]
	Data["years"]=annee_list
  
	cursor.execute("SELECT distinct  specialite from  db_university.resultats")	
	sp_tuple = cursor.fetchall()
	sp_list =  [item[0] for item in sp_tuple]
    

	for sp  in sp_list:
        
		

		cursor.execute("SELECT count(matricule) ,annee  from  db_university.resultats where specialite='"+sp+"'  group by annee ")	
		value_tuple = cursor.fetchall()
		value_list=[item[0] for item in value_tuple]

		Data["datasets"].append({"label":sp,"data": value_list}),	
	
		
        
	data_JSON = json.dumps(Data)	
	return data_JSON 

   


if __name__ == '__main__':
	app.run(debug=True, port=5000)
	