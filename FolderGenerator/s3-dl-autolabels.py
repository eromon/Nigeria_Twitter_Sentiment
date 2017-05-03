# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:26:11 2017

@author: Eromon
"""
import os as os
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import boto3

#The code below connects to the MySQL server and returns a dataframe 
engine = create_engine('mysql+pymysql://root:mypassword@192.168.99.100:3306/dl-auto')
df = pd.read_sql_query('SELECT * FROM tbl_02_models', engine)

#Here we create a list of the unique car brand in the dataset
brands = df["model_make_id"].unique()
brands = brands[0:100]

#The code below helps us connect with AWS s3 and access our bucket of choice
s3 = boto3.resource("s3")
my_bucket = s3.Bucket("dl-autolabels-classification")

#Creates an AWS s3 client to help create objects
client = boto3.client("s3")

views = ["front_view", "rear_view","side_view"]

for i,brand in enumerate(brands):
    years = df.model_year[df["model_make_id"] == brand]
    years = years.astype(str)
    #response = client.put_object(
     #   Bucket = "dl-autolabels-classification",
      #  Body = " ",
       # Key = "cars/"+brand+"/"
        #) 
   
    for i,year in enumerate(years):
        #response = client.put_object(
        #Bucket = "dl-autolabels-classification",
        #Body = " ",
        #Key = "cars/"+brand+"/"+year+"/"
        #)
        models = df.model_name[(df["model_year"] == int(year)) & (df["model_make_id"] == brand)]
        
        for s,model in enumerate(models):
            model = model.strip()
         #   response = client.put_object(
          #  Bucket = "dl-autolabels-classification",
           # Body = " ",
            #Key = "cars/"+brand+"/"+year+"/"+model+"/"
            #)
            
            for view in views:
                #This command creates the object
                response = client.put_object(
                Bucket = "dl-autolabels-classification",
                Body = " ",
                Key = "cars/"+brand+"/"+year+"/"+model+"/"+view+"/"
                )
                print("updating"+"  "+brand)
