import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="jardin",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    return conn

def obtener_arboles():
    """Obtiene la lista de árboles de la base de datos."""
    conn = connect()
    arboles = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, tipo, altura_promedio, fecha_plantacion FROM Arboles")
        arboles = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Error al obtener los árboles: {e}")
    finally:
        conn.close()

    return arboles

def obtener_arboles_by_nombre(nombre):
    """Obtiene la lista de árboles de la base de datos."""
    conn = connect()
    arboles = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, tipo, altura_promedio, fecha_plantacion FROM Arboles WHERE nombre = %s", (nombre,))
        arboles = cursor.fetchall()
        cursor.close()
    except Exception as e:
        print(f"Error al obtener los árboles: {e}")
    finally:
        conn.close()

    return arboles


def insertar_arbol(nombre, tipo, altura_promedio, fecha_plantacion):
    """
    Inserta un nuevo árbol en la base de datos.

    Parámetros:
    - nombre (str): Nombre del árbol (ejemplo: "Pino").
    - tipo (str): Puede ser "Perenne" o "Caduca".
    - altura_promedio (int): Altura promedio del árbol en metros.
    - fecha_plantacion (str): Fecha en formato 'YYYY-MM-DD' de la plantación.
    """
    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL

        # Consulta SQL para insertar un nuevo árbol en la tabla 'Arboles'
        query = """
        INSERT INTO Arboles (nombre, tipo, altura_promedio, fecha_plantacion)
        VALUES (%s, %s, %s, %s)
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (nombre, tipo, altura_promedio, fecha_plantacion))

        # Confirmar la transacción
        conn.commit()
        print("Árbol registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos

# Ejemplo de uso:
# insertar_arbol("Pino", "Perenne", 30, "2005-03-15")
