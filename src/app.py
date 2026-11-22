import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    try:
        conexion = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root123"),
            database=os.getenv("DB_NAME", "holamundo_db")
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT VERSION();")
        version_mysql = cursor.fetchone()[0]
        cursor.close()
        conexion.close()
        return f"""
        <h1>¡Hola Mundo desde Docker Compose!</h1>
        <p><strong>Estado de la base de datos:</strong> Conectado exitosamente a MySQL (Versión {version_mysql})</p>
        """
    except Exception as error:
        return f"""
        <h1>¡Hola Mundo!</h1>
        <p><strong>Error al conectar con MySQL:</strong> {error}</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
