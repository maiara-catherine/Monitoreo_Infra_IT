from src.base_datos import insertar_ticket

def evaluar_condiciones_ticket(fecha, dispositivo, cpu, ram, estado):
    if estado == "Desconectado":
        insertar_ticket(fecha, dispositivo, "Pérdida de conectividad / Red caída", "ALTA")
        print(f"🚨 Ticket generado: {dispositivo} no responde.")

    if cpu > 85.0:
        if cpu > 95.0:
            
          prioridad = "ALTA" 
        else:
            prioridad="MEDIA"
        insertar_ticket(fecha, dispositivo, f"Uso crítico de CPU ({cpu}%)", prioridad)
        print(f"⚠️ Ticket generado: CPU alta en {dispositivo}.")

    if ram > 90.0:
        insertar_ticket(fecha, dispositivo, f"Saturación de RAM ({ram}%)", "MEDIA")#LO AÑADE A LA BASE DE DATOS 
        print(f"⚠️ Ticket generado: RAM elevada en {dispositivo}.")