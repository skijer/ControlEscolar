import mysql.connector
from tkinter import messagebox

db = mysql.connector.connect(
  host="localhost",
  user="skijer",
  password="admin",
  database="cotrolescolar"
)

cursor = db.cursor()

def InsertUsuario(nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena):
    try:
        sql = "INSERT INTO usuarios (nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Usuario ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar usuario: {e}")
        db.rollback()

def InsertAlumno(codigo, estado, fecha_nacimiento, carrera):
    try:
        sql = "INSERT INTO alumnos (codigo, estado, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
        val = (codigo, estado, fecha_nacimiento, carrera)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Alumno ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar alumno: {e}")
        db.rollback()

def InsertMaestro(codigo, grado_estudios):
    try:
        sql = "INSERT INTO maestros (codigo, grado_estudios) VALUES (%s, %s)"
        val = (codigo, grado_estudios)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Maestro ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar maestro: {e}")
        db.rollback()

def InsertMateria(nombre_asignatura, creditos, semestre, carrera):
    try:
        sql = "INSERT INTO materias (nombre_asignatura, creditos, semestre, carrera) VALUES (%s, %s, %s, %s)"
        val = (nombre_asignatura, creditos, semestre, carrera)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Materia ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar materia: {e}")
        db.rollback()

def InsertSalon(edificio, nombre_salon):
    try:
        sql = "INSERT INTO salon (edificio, nombre_salon) VALUES (%s, %s)"
        val = (edificio, nombre_salon)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Salón ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar salón: {e}")
        db.rollback()

def InsertGrupo(nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon):
    try:
        sql = "INSERT INTO grupos (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Grupo ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar grupo: {e}")
        db.rollback()

def InsertCarrera(nombre_carrera, num_semestres):
    try:
        sql = "INSERT INTO carreras (nombre_carrera, num_semestres) VALUES (%s, %s)"
        val = (nombre_carrera, num_semestres)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Carrera ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar carrera: {e}")
        db.rollback()

def InsertUsuarioMateria(codigo_usuario, codigo_materia):
    try:
        sql = "INSERT INTO usuarios_materias (codigo_usuario, codigo_materia) VALUES (%s, %s)"
        val = (codigo_usuario, codigo_materia)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-materia ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-materia: {e}")
        db.rollback()

def InsertHorario(codigo, horario, turno):
    try:
        sql = "INSERT INTO horarios (codigo, horario, turno) VALUES (%s, %s, %s)"
        val = (codigo, horario, turno)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Horario ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar horario: {e}")
        db.rollback()

def InsertGrupoMaestros(codigo_maestro, codigo_grupo):
    try:
        sql = "INSERT INTO grupo_maestros (codigo_maestro, codigo_grupo) VALUES (%s, %s)"
        val = (codigo_maestro, codigo_grupo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-grupo ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-grupo: {e}")
        db.rollback()

def InsertUsuarioHorario(codigo_usuario, horario):
    try:
        sql = "INSERT INTO usuario_horario (codigo_usuario, horario) VALUES (%s, %s)"
        val = (codigo_usuario, horario)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-horario ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-horario: {e}")
        db.rollback()




def SelectUsuario(codigo):
    try:
        sql = "SELECT * FROM usuarios WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar usuario: {e}")
        return None
    
def SelectAlumno(codigo):
    try:
        sql = "SELECT * FROM alumnos WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar alumno: {e}")
        return None
    
def SelectMaestro(codigo):
    try:
        sql = "SELECT * FROM maestros WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar maestro: {e}")
        return None
    
def SelectMateria(codigo):
    try:
        sql = "SELECT * FROM materias WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar materia: {e}")
        return None
    
def ListarMateriasDeUsuario(codigo_usuario):
    try:
        sql = "SELECT materias.* FROM materias JOIN usuarios_materias ON materias.codigo = usuarios_materias.codigo_materia WHERE usuarios_materias.codigo_usuario = %s"
        val = (codigo_usuario,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar listar materias del usuario: {e}")
        return None

def SelectSalon(codigo):
    try:
        sql = "SELECT * FROM salon WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar salón: {e}")
        return None
    
def SelectGrupo(codigo):
    try:
        sql = "SELECT * FROM grupos WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar grupo: {e}")
        return None
    
def SelectCarrera(codigo):
    try:
        sql = "SELECT * FROM carreras WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar carrera: {e}")
        return None
    
def SelectHorario(codigo):
    try:
        sql = "SELECT * FROM horarios WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar horario: {e}")
        return None
    
def SelectGrupoMaestros(codigo_maestro):
    try:
        sql = "SELECT * FROM grupo_maestros WHERE codigo_maestro = %s"
        val = (codigo_maestro,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar grupo de maestros: {e}")
        return None

def ListarUsuariosEnHorario(horario):
    try:
        sql = "SELECT usuarios.* FROM usuarios JOIN usuario_horario ON usuarios.codigo = usuario_horario.codigo_usuario WHERE usuario_horario.horario = %s"
        val = (horario,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar listar usuarios en horario: {e}")
        return None
    
def UpdateUsuario(codigo, nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena):
    try:
        codigo = int(codigo)
        sql = "UPDATE usuarios SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, perfil=%s, email=%s, nombre_usuario=%s, contrasena=%s WHERE codigo = %s"
        val = (nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de usuario actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de usuario: {str(e)}")

def UpdateAlumno(codigo, estado, fecha_nacimiento, carrera):
    try:
        codigo = int(codigo)
        sql = "UPDATE alumnos SET estado=%s, fecha_nacimiento=%s, carrera=%s WHERE codigo = %s"
        val = (estado, fecha_nacimiento, carrera, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de alumno actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de alumno: {str(e)}")

def UpdateMateria(codigo, nombre_asignatura, creditos, semestre, carrera):
    try:
        codigo = int(codigo)
        sql = "UPDATE materias SET nombre_asignatura=%s, creditos=%s, semestre=%s, carrera=%s WHERE codigo = %s"
        val = (nombre_asignatura, creditos, semestre, carrera, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de materia actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de materia: {str(e)}")

def UpdateHorario(codigo, horario, turno):
    try:
        codigo = int(codigo)
        sql = "UPDATE horarios SET horario=%s, turno=%s WHERE codigo = %s"
        val = (horario, turno, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de horario actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de horario: {str(e)}")

def UpdateCarrera(codigo, nombre_carrera, num_semestres):
    try:
        codigo = int(codigo)
        sql = "UPDATE carreras SET nombre_carrera=%s, num_semestres=%s WHERE codigo = %s"
        val = (nombre_carrera, num_semestres, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de carrera actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de carrera: {str(e)}")

def UpdateGrupo(codigo, nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon):
    try:
        codigo = int(codigo)
        sql = "UPDATE grupos SET nombre_grupo=%s, semestre=%s, horario=%s, codigo_materia=%s, codigo_maestro=%s, max_num_alumnos=%s, codigo_salon=%s WHERE codigo = %s"
        val = (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de grupo actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de grupo: {str(e)}")

def UpdateSalon(codigo, edificio, nombre_salon):
    try:
        codigo = int(codigo)
        sql = "UPDATE salon SET edificio=%s, nombre_salon=%s WHERE codigo = %s"
        val = (edificio, nombre_salon, codigo)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de salón actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de salón: {str(e)}")



