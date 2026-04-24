import sqlite3
import os

def inicializar_db():
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()
    
    # Crear tablas
    cursor.execute('CREATE TABLE IF NOT EXISTS Miembros (cedula TEXT PRIMARY KEY, nombre_completo TEXT, telefono TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Clases (id_clase INTEGER PRIMARY KEY AUTOINCREMENT, nombre_clase TEXT, dia_semana TEXT, horario TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Inscripciones (id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT, cedula_miembro TEXT, id_clase INTEGER, FOREIGN KEY(cedula_miembro) REFERENCES Miembros(cedula), FOREIGN KEY(id_clase) REFERENCES Clases(id_clase))')
    
    # Insertar datos si está vacío
    cursor.execute('SELECT COUNT(*) FROM Miembros')
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Miembros VALUES ('1-1111-1111', 'Juan Perez', '8888-1111')")
        cursor.execute("INSERT INTO Clases (nombre_clase, dia_semana, horario) VALUES ('Yoga', 'Lunes', '08:00')")
        cursor.execute("INSERT INTO Inscripciones (cedula_miembro, id_clase) VALUES ('1-1111-1111', 1)")
        conexion.commit()
    conexion.close()

def listar_miembros():
    conn = sqlite3.connect('base_de_datos.db')
    res = conn.execute('SELECT * FROM Miembros').fetchall()
    print("\n--- LISTA DE MIEMBROS ---")
    for r in res: print(f"Cédula: {r[0]} | Nombre: {r[1]} | Tel: {r[2]}")
    conn.close()

def listar_clases():
    conn = sqlite3.connect('base_de_datos.db')
    res = conn.execute('SELECT * FROM Clases').fetchall()
    print("\n--- CLASES DISPONIBLES ---")
    for r in res: print(f"ID: {r[0]} | Clase: {r[1]} | Día: {r[2]} | Hora: {r[3]}")
    conn.close()

def ver_inscripciones():
    conn = sqlite3.connect('base_de_datos.db')
    query = "SELECT M.nombre_completo, C.nombre_clase FROM Inscripciones I JOIN Miembros M ON I.cedula_miembro = M.cedula JOIN Clases C ON I.id_clase = C.id_clase"
    res = conn.execute(query).fetchall()
    print("\n--- MIEMBROS INSCRITOS POR CLASE ---")
    for r in res: print(f"Miembro: {r[0]} -> Clase: {r[1]}")
    conn.close()

def main():
    inicializar_db()
    while True:
        print("\n=== BIENVENIDO A FITLIFE APP ===")
        print("1. Ver Miembros")
        print("2. Ver Clases")
        print("3. Ver Inscripciones")
        print("4. Agregar Miembro")
        print("5. Salir")
        opc = input("Escoja una opción: ")
        
        if opc == '1': listar_miembros()
        elif opc == '2': listar_clases()
        elif opc == '3': ver_inscripciones()
        elif opc == '4':
            c = input("Cédula: "); n = input("Nombre: "); t = input("Teléfono: ")
            conn = sqlite3.connect('base_de_datos.db')
            conn.execute("INSERT INTO Miembros VALUES (?,?,?)", (c,n,t))
            conn.commit(); conn.close(); print("Miembro agregado.")
        elif opc == '5': break

if __name__ == "__main__":
    main()
