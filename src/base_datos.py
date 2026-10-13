#funciones para crear tabla e insertar datos
#la tabla se ira creando y este archivo llenandose con la ejecucion de las funciones
import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("data/monitoreo.db")
    cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS REGISTROS_DISPOSITIVOS(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     fecha DATE  ,
     dispositivo TEXT,
     cpu REAL,
     ram REAL,
     estado TEXT)""")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            dispositivo TEXT,
            incidencia TEXT,
            prioridad TEXT,
            estado TEXT
        )
    """)#TABLA PARA INFORMACION DE TICKETS 
    

    conexion.commit()
    conexion.close()

def insertar_registro(fecha, dispositivo, cpu, ram, estado):
    conexion = sqlite3.connect("data/monitoreo.db")
    cursor = conexion.cursor()
    cursor.execute("""
       INSERT INTO REGISTROS_DISPOSITIVOS
    (fecha, dispositivo, cpu, ram, estado)
    VALUES(?,?,?,?,?)""", (fecha, dispositivo, cpu, ram, estado))#INDICO LAS COLUMNAS A RELLENAR 
    conexion.commit()
    conexion.close()


def insertar_ticket(fecha, dispositivo, incidencia, prioridad, estado="ABIERTO"):
    conexion = sqlite3.connect("data/monitoreo.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
        INSERT INTO tickets (fecha, dispositivo, incidencia, prioridad, estado)
        VALUES (?, ?, ?, ?, ?)
    """, (fecha, dispositivo, incidencia, prioridad, estado))
    
    conexion.commit()
    conexion.close()#VALORES DE TABAL TICKETS 
    