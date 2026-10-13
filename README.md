🖥️ Plataforma de Monitoreo de Infraestructura IT y Gestión de Incidencias (AIOps)

Una solución integral de monitoreo de infraestructura tecnológica y mesa de ayuda automatizada. El sistema captura métricas de hardware del nodo servidor en tiempo real, rastrea el estado de conectividad en la red local o topologías virtuales (Cisco Packet Tracer) mediante protocolo ICMP (ping), persiste las mediciones en una base de datos relacional SQLite y genera tickets de alerta de manera inteligente ante anomalías o caídas de servicio.

🚀 Características Principales

Monitoreo de Recursos Locales (Host System): Captura continua del porcentaje de uso de CPU y memoria RAM.

Escaneo de Disponibilidad de Red: Verificación periódica de conectividad (Uptime/Downtime) de la lista de infraestructura mediante comprobaciones ICMP (Ping).

Gestión de Tickets Automatizada: Motor de reglas que genera tickets de incidencia categorizados por nivel de prioridad (ALTA, MEDIA, BAJA) cuando se superan umbrales críticos de consumo o falla la conectividad.

Persistencia Relacional: Almacenamiento optimizado y desacoplado mediante dos tablas relacionales (REGISTROS_DISPOSITIVOS y tickets) en SQLite.

Panel de Control Interactivo (Dashboard): Visualización en tiempo real de métricas, gráficos de rendimiento histórico y mesa de ayuda operativa con Streamlit.

Arquitectura Modular y Escalable: Código estructurado bajo principios de separación de responsabilidades (Separation of Concerns).

Arquitectura del Sistema

                               +-----------------------------+
                               |   config.py / DISPOSITIVOS  |
                               +--------------+--------------+
                                              |
                                              v
+------------------------+             +--------------+             +-----------------------+
|   src/recolector.py    | ----------> |   main.py    | ----------> |    src/tickets.py     |
| (CPU, RAM, Ping ICMP)  |             | (Coordinador)|             | (Evaluación de Reglas)|
+------------------------+             +------+-------+             +-----------+-----------+
                                              |                                 |
                                              v                                 v
                               +------------------------------+                 |
                               |      src/base_datos.py       | <---------------+
                               |  (Persistencia SQLite 3)     |
                               +--------------+---------------+
                                              |
                                              v
                               +------------------------------+
                               |     data/monitoreo.db        |
                               +--------------+---------------+
                                              |
                                              v
                               +------------------------------+
                               |      dashborad/app.py        |
                               |    (Interfaz Streamlit)      |
                               +------------------------------+


🚀 Modo de Uso

Configuración del Inventario de Red

Añade los dispositivos que deseas monitorear editando la lista DISPOSITIVOS en src/config.py o src/recolector.py:

DISPOSITIVOS = [
    {"nombre": "Router Principal", "ip": "192.168.1.1"},
    {"nombre": "Servidor Web Local", "ip": "127.0.0.1"},
    {"nombre": "Switch Oficina", "ip": "192.168.1.20"}
]


Ejecución del Motor de Recolección y Tickets

Para realizar un ciclo de recolección, evaluación e inserción en la base de datos:

python main.py


📊 Dashboard de Control

Para iniciar la interfaz gráfica interactiva y visualizar las métricas y la mesa de ayuda:

streamlit run dashborad/app.py


La interfaz se abrirá automáticamente en tu navegador web predeterminado (por defecto en http://localhost:8501), permitiéndote:

Consultar métricas en tiempo real e histórico de recursos.

Revisar la lista de nodos activos y desconectados.

Monitorear los tickets de incidencias generados por el sistema y cambiar su estado (ABIERTO / RESUELTO).