#el script que junta los datos (CPU, RAM, ping)
from datetime import datetime
import psutil
from ping3 import ping

def obtener_uso_cpu():
    """
    Devuelve el porcentaje de uso de CPU en este momento.
    El '1' significa que espera 1 segundo para medir bien (si le
    ponés 0, a veces devuelve un dato poco preciso, tipo 0.0).
    """
    return psutil.cpu_percent(interval=1)


def obtener_uso_ram():
    """
    Devuelve el porcentaje de memoria RAM usada.
    psutil.virtual_memory() te da varios datos (total, usado, libre, etc.)
    y con .percent te quedás solo con el porcentaje.
    """
    memoria = psutil.virtual_memory()
    return memoria.percent


def verificar_estado(ip):
    """
    Verifica si un dispositivo responde en la red (como el 'ping'
    que harías desde la terminal, pero en código).
    ping() devuelve el tiempo de respuesta en segundos si el
    dispositivo contesta, o None si no responde.
    Acá lo traducimos a un texto más claro: "activo" o "caído".
    """
    resultado = ping(ip, timeout=2)
    if resultado is not None:
        return "activo"
    else:
        return "caído"

def recolectar_hora_fecha():
    datos=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return datos

#extraigo la hora y fecha actual
 