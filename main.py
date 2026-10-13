from src.config import DISPOSITIVOS #LISTA DE DISPOSITIVOS 
from src.base_datos import crear_tabla, insertar_registro
from src.recolector import obtener_uso_cpu, obtener_uso_ram, verificar_estado,recolectar_hora_fecha
from src.tickets import evaluar_condiciones_ticket
#llamada a funciones:
crear_tabla()

CPU=obtener_uso_cpu()
RAM=obtener_uso_ram()
WIFI=verificar_estado("192.168.1.15")
DATETIME=recolectar_hora_fecha()


for dispositivo in DISPOSITIVOS:
    NOMBRE=dispositivo["nombre"]#SE LE AÑADE "" A LAS CLAVES PARA QUE SEAN TOMADAS 
    IP=dispositivo["ip"]
    insertar_registro(DATETIME,NOMBRE ,CPU,RAM,WIFI)#(fecha, dispositivo, cpu, ram, estado)RELLENA LA TABLA CON LOS VALORES OBTENIDOS 

    evaluar_condiciones_ticket(DATETIME, NOMBRE,CPU,RAM,WIFI)#LE PASO LOS VALORES OBTENIDOS DE CIERTO DISPOSITIVO PARA HACER LA OBTENCION Y CONDICION DE DAT0S