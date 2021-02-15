from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True



CORS(app)
try:
    DATABASE = os.getenv('DATABASE')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')

    connection = psycopg2.connect(database= DATABASE, user= DATABASE_USER, password= DATABASE_PASSWORD, host= DATABASE_HOST, port= DATABASE_PORT)
    cursor = connection.cursor()

    query = """SELECT 
    companies.name AS company_name,
    companies.id AS company_id,
    users.name AS name_user,
    users.last_name AS last_name_user,
    users.audit -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'last_login' AS last_login,
    users.properties -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'rut' AS rut
    FROM companies INNER JOIN users ON companies.id = users.company_id ORDER BY company_name"""

    @app.route('/', methods=['GET'])
    def home():
        print('Hola mundo')

    @app.route('/prueba', methods=['GET'])
    def prueba():
        cursor.execute('SELECT name FROM users')
        result = cursor.fetchall()
        print(result)
        return jsonify(result)


    @app.route('/pdf', methods=['GET'])
    def prueba_pdf():
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        return jsonify(result)


    app.run()
except:
    print('Error')