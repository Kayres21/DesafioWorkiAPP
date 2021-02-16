from dotenv import load_dotenv
import psycopg2
import os
import pandas as pd
import pdf


load_dotenv()



def connection():
    DATABASE = os.getenv('DATABASE')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')

    connection = psycopg2.connect(database= DATABASE, user= DATABASE_USER, password= DATABASE_PASSWORD, host= DATABASE_HOST, port= DATABASE_PORT)
    cursor = connection.cursor()

    return cursor 

def get_data(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def grup(data):
    datos  = pd.DataFrame(data, columns=["Empresa", "Id_empresa", "Nombre_usuario", "Apellido_usuario", "Ultimo_ingreso", "Rut"], dtype = str ) 
    datos_agrupados =datos.groupby('Empresa')
    datos.to_csv('./result.csv', index=False)
    

def main():
    cursor = connection()

    query = """SELECT 
    companies.name AS company_name,
    companies.id AS company_id,
    users.name AS name_user,
    users.last_name AS last_name_user,
    users.audit -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'last_login' AS last_login,
    users.properties -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'rut' AS rut
    FROM companies INNER JOIN users ON companies.id = users.company_id ORDER BY company_name"""
    resultado = get_data(cursor, query)
    grup(resultado)
    pdf.make_pdf()
    



try:
    main()
except:
    print('Error')

    

  
