import os
import mysql.connector

db_host = os.getenv('DB_HOST')
db_pwd = os.getenv('DB_PWD')
db_name = 'nf_db'
table_name = 'profiles'

def open_connection():
    db = mysql.connector.connect(host=db_host, database=db_name, user='root', password=db_pwd)
    return db

def close_connection(db):
    db.close()

def create_database(cursor, dbName):
    cursor.execute("CREATE DATABASE {}".format(dbName))

def insert_data(db, cursor, val):
    sql_query = "INSERT INTO {} (nfid, nftype, ip, port) VALUES (%s, %s, %s, %s)".format(table_name)
   
    cursor.execute(sql_query, val)
    db.commit()

def fetch_all(cursor):
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    all_result = cursor.fetchall()
    result_dicts = {}
    for result in all_result:
        result_dict = {'nfId':result[0], 'nfType': result[1], 'ip': result[2], 'port': result[3]}
        result_dicts[result[0]] = result_dict
    return result_dicts

def fetch_with_id(cursor, nf_id):
    query = "SELECT * FROM {} where nfid = {}".format(table_name, nf_id)
    cursor.execute(query)
    result = cursor.fetchall()
    result_dict = {'nfId' : result[0][0], 'nfType': result[0][1], 'ip': result[0][2], 'port': result[0][3]}
    return result_dict

def delete_data(db, cursor, nf_id):
    query = "DELETE FROM {} WHERE nfid = {}".format(table_name, nf_id)
    cursor.execute(query)
    db.commit()

def get_all_ids(cursor):
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    all_result = cursor.fetchall()
    id_list = []
    for result in all_result:
        id_list.append(result[0])
    return id_list

if __name__ == '__main__':

    db = open_connection()
    cursor = db.cursor()

    #val1 = ("400", "PCF", "2.2.2.2", "2000")
    #insert_data(db, cursor, val1)
    
    #all_result = fetch_all(cursor)
    #print(all_result)
    #for x in all_result:
    #    print(x)

    #result = fetch_with_id(cursor, "300")
    #print(result)

    #  delete_data(db, cursor, "400")


    close_connection(db)
