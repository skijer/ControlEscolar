import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="skijer",
  password="admin",
  ##Ignore if database not created
  database="cotrolescolar"
)

cursor = db.cursor()

# Crear la tabla 'usuarios'
cursor.execute("""
    CREATE TABLE usuarios (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        apellido_paterno VARCHAR(255),
        apellido_materno VARCHAR(255),
        perfil ENUM('alumno', 'maestro', 'administrativo'),
        email VARCHAR(255),
        nombre_usuario VARCHAR(255),
        contrasena VARCHAR(255)
    )
""")

# Crear la tabla 'alumnos'
cursor.execute("""
    CREATE TABLE alumnos (
        codigo INT PRIMARY KEY,
        estado VARCHAR(255),
        fecha_nacimiento DATE,
        carrera VARCHAR(255)
    )
""")

# Crear la tabla 'maestros'
cursor.execute("""
    CREATE TABLE maestros (
        codigo INT PRIMARY KEY,
        grado_estudios VARCHAR(255)
    )
""")

# Crear la tabla 'materias'
cursor.execute("""
    CREATE TABLE materias (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        nombre_asignatura VARCHAR(255),
        creditos INT,
        semestre INT,
        carrera VARCHAR(255)
    )
""")

# Crear la tabla 'usuarios-materias'
cursor.execute("""
    CREATE TABLE usuarios_materias (
        codigo_usuario INT,
        codigo_materia INT
    )
""")

# Crear la tabla 'salon'
cursor.execute("""
    CREATE TABLE salon (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        edificio VARCHAR(255),
        nombre_salon VARCHAR(255)
    )
""")

# Crear la tabla 'grupos'
cursor.execute("""
    CREATE TABLE grupos (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        nombre_grupo VARCHAR(255),
        semestre INT,
        horario INT,
        codigo_materia INT,
        codigo_maestro INT,
        max_num_alumnos INT,
        codigo_salon INT
    )
""")

# Crear la tabla 'carreras'
cursor.execute("""
    CREATE TABLE carreras (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        nombre_carrera VARCHAR(255),
        num_semestres INT
    )
""")

# Crear la tabla 'horarios'
cursor.execute("""
    CREATE TABLE horarios (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        horario VARCHAR(255),
        turno ENUM('mañana', 'tarde', 'noche')
    )
""")

# Crear la tabla 'grupo_maestros'
cursor.execute("""
    CREATE TABLE grupo_maestros (
        codigo_maestro INT,
        codigo_grupo INT
    )
""")
# Crear la tabla "usuario_horario"
cursor.execute("""
CREATE TABLE usuario_horario (
    codigo_usuario INT,
    horario INT
)
""")

# Confirmar los cambios en la base de datos
db.commit()

# Cerrar la conexión
db.close()