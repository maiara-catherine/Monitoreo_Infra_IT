import sqlite3
import pandas as pd
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Monitoreo IT",
    page_icon="🖥️",
    layout="wide"
)

DB_PATH = "data/monitoreo.db"

def cargar_registros():
    """Lee el historial de mediciones de la base de datos SQLite."""
    try:
        conexion = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM REGISTROS_DISPOSITIVOS ORDER BY id DESC", conexion)
        conexion.close()
        return df
    except Exception as e:
        st.error(f"Error al conectar con la base de datos: {e}")
        return pd.DataFrame()

def cargar_tickets():
    """Lee la lista de tickets generados."""
    try:
        conexion = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM tickets ORDER BY id DESC", conexion)
        conexion.close()
        return df
    except Exception as e:
        st.error(f"Error al leer la tabla de tickets: {e}")
        return pd.DataFrame()

def resolver_ticket(ticket_id):
    """Actualiza el estado de un ticket a RESUELTO."""
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("UPDATE tickets SET estado = 'RESUELTO' WHERE id = ?", (ticket_id,))#marca como resuelto el id ingresado
    conexion.commit()
    conexion.close()

# --- INTERFAZ DE STREAMLIT ---
st.title("🖥️ Dashboard de Monitoreo de Infraestructura IT")
st.markdown("Plataforma interactiva para visualizar métricas en tiempo real y gestión de incidencias.")

# Cargar datos
df_registros = cargar_registros()
df_tickets = cargar_tickets()

if df_registros.empty:
    st.warning("No hay registros disponibles en la base de datos. Ejecuta 'python main.py' para generar datos.")
else:
    # 1. TARJETAS DE MÉTRICAS (KPIs)
    st.subheader("📊 Estado Actual del Sistema")
    col1, col2, col3, col4 = st.columns(4)
    
    ultimo_registro = df_registros.iloc[0]
    total_nodos = df_registros['dispositivo'].nunique()
    nodos_online = df_registros[df_registros['estado'] == 'Conectado']['dispositivo'].nunique()
    
    col1.metric("Última Actualización", str(ultimo_registro.get('fecha', 'N/A'))[-8:])
    col2.metric("Uso CPU Local", f"{ultimo_registro.get('cpu', 0)}%")
    col3.metric("Uso RAM Local", f"{ultimo_registro.get('ram', 0)}%")
    col4.metric("Nodos Respondiendo", f"{nodos_online} / {total_nodos}")

    st.divider()

    # 2. SECCIÓN DE GRÁFICOS Y TABLAS
    col_izq, col_der = st.columns([2, 1])

    with col_izq:
        st.subheader("📈 Histórico de Recursos (CPU / RAM)")
        if 'fecha' in df_registros.columns:
            # Mostramos un gráfico de líneas con los registros
            df_grafico = df_registros.copy()
            df_grafico = df_grafico.sort_values('id')
            st.line_chart(df_grafico.set_index('fecha')[['cpu', 'ram']])
        
        st.subheader("📋 Últimas Mediciones Registradas")
        st.dataframe(df_registros.head(10), use_container_width=True)

    with col_der:
        st.subheader("🚨 Mesa de Ayuda / Tickets")
        
        if df_tickets.empty:
            st.success("No se han registrado incidencias.")
        else:
            tickets_abiertos = df_tickets[df_tickets['estado'] == 'ABIERTO']
            st.write(f"**Tickets Abiertos:** {len(tickets_abiertos)}")
            
            for _, ticket in df_tickets.iterrows():
                estado_icon = "🔴" if ticket['estado'] == "ABIERTO" else "🟢"
                with st.expander(f"{estado_icon} #{ticket['id']} - {ticket['dispositivo']} ({ticket['prioridad']})"):
                    st.write(f"**Incidencia:** {ticket['incidencia']}")
                    st.write(f"**Fecha:** {ticket['fecha']}")
                    st.write(f"**Estado:** {ticket['estado']}")
                    
                    if ticket['estado'] == "ABIERTO":
                        if st.button(f"Marcar como Resuelto #{ticket['id']}", key=f"btn_{ticket['id']}"):
                            resolver_ticket(ticket['id'])
                            st.success(f"Ticket #{ticket['id']} marcado como resuelto.")
                            st.rerun()

st.sidebar.header("Acciones")
if st.sidebar.button("🔄 Actualizar Datos"):
    st.rerun()
