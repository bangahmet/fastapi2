import sqlite3
import json
from typing import Optional
from fastapi import FastAPI

DB = "pbl_projectdata.db"
app = FastAPI()

@app.get("/")
def getName():
    return{"Name":"Rifqiiiii"}

@app.get("/clothing_list")
def Clothing_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM data WHERE Items_Accepted LIKE '%Clothing%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/shoes_list")
def Shoes_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM data WHERE Items_Accepted LIKE '%Shoes%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows


@app.get("/coat_list")
def Coats_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM data WHERE Items_Accepted LIKE '%Coats%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/towel_list")
def Towel_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM data WHERE Items_Accepted LIKE '%Towels%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/nonprofit_list")
def NonProfit_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT * FROM profitcsv WHERE Nonprofit_Organization ='True'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/profits_list")
def profits_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT * FROM profitcsv WHERE Nonprofit_Organization ='False'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/search/{query}")
def searchitems( query: str ,json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()
    sqlquery = "SELECT *  FROM data WHERE Items_Accepted LIKE '%{0}%'".format(query)
    #sqlquery = "SELECT *  FROM data WHERE Items_Accepted LIKE '%"+ query +"%'"

    rows = db.execute(sqlquery).fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        #return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
        return json.dumps( {'variable' : query} ) #CREATE JSON
    return rows

    
@app.get("/datainfo/clothing_list")
def Clothing_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM datainfo WHERE Items_Accepted LIKE '%Clothing%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/datainfo/clothing_list")
def Clothinfo_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM datainfo WHERE Items_Accepted LIKE '%Clothing%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/datainfo/shoes_list")
def shoesinfo_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM datainfo WHERE Items_Accepted LIKE '%Shoes%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/datainfo/coat_list")
def Coatsinfo_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM datainfo WHERE Items_Accepted LIKE '%Coats%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows

@app.get("/datainfo/towel_list")
def Towelinfo_list( json_str = False ):
    conn = sqlite3.connect( DB )
    conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
    db = conn.cursor()

    rows = db.execute('''
    SELECT *  FROM datainfo WHERE Items_Accepted LIKE '%Towels%'
    ''').fetchmany(10)

    conn.commit()
    conn.close()

    if json_str:
        return json.dumps( [dict(ix) for ix in rows] ) #CREATE JSON
    return rows