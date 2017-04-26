# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:31:12 2017

@author: Eromon
"""
import os as os
import pandas as pd
import pymysql
from sqlalchemy import create_engine
#engine = create_engine('mysql+pymysql://root:mypassword@192.168.99.100:3306/mysql')
engine = create_engine('mysql+pymysql://root:mypassword@192.168.99.100:3306/dl-auto')

df = pd.read_sql_query('SELECT * FROM tbl_02_models', engine)
#print(df.head())

brands = df["model_make_id"].unique()
brands = brands[100:] 
rootPath = "C:\\Users\\Eromon D Great\\.spyder-py3\\cars\\"
views = ["front_view", "rear_view","side_view"]
'''for i,brand in enumerate(brands):
    print(brand,i)

'''
for i,brand in enumerate(brands):
    #df = pd.read_excel("dl-auto.xlsx", sheetname=brand)
    #years = df["model_year"]
    years = df.model_year[df["model_make_id"] == brand]
    years = years.astype(str)
    #print(years)
    #os.makedirs(os.path.join(rootPath,brand),exist_ok=True)
    
    for i,year in enumerate(years):
        
        #os.makedirs(os.path.join(rootPath,brand,year),exist_ok=True)
        models = df.model_name[(df["model_year"] == int(year)) & (df["model_make_id"] == brand)]
        #print(model + "   " + year)
       
        #print(models)
        
        #for s,model in enumerate(df.model_name[years == year].astype(str)):
        for s,model in enumerate(models):
            #print(s,model)
            os.makedirs(os.path.join(rootPath,brand,year,model),exist_ok=True)
            model = model.strip() 
            for view in views:
                os.makedirs(os.path.join(rootPath,brand,year,model,view),exist_ok=True)


'''
import os as os
#import MySQLdb as sql
import mysql.connector as sql
conn = sql.connect(host="192.168.99.100",user="root",password="mypassword",database="mysql")
cursor = conn.cursor()
query = "SELECT * FROM taula "
#query = "SELECT model_year, model_name FROM taula "
cursor.execute(query)

rows = cursor.fetchall()
#rows[0] = rows[0].astype(str)
#print(rows)
rows1 = rows[:,0]
print(rows1)

rootPath = "C:\\Users\\Eromon D Great\\.spyder-py3\\test_dir\\"
for i,eachRow in enumerate(rows):
    os.makedirs(os.path.join(rootPath,str(eachRow[0])),exist_ok=True)
    print(eachRow[1])
    years = eachRow[1]
    for i,year in enumerate(years):
        print(year)
        
cursor.close()
'''