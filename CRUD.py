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
        val = (nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena,)
        cursor.execute(sql, val)
        id = cursor.lastrowid
        messagebox.showinfo("Acción realizada con éxito","Usuario ingresado correctamente con ID:" + str(id))
        db.commit()
        return id
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar usuario")
        db.rollback()

def InsertAlumno(codigo, estado, fecha_nacimiento, carrera):
    try:
        sql = "INSERT INTO alumnos (codigo, estado, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
        val = (codigo, estado, fecha_nacimiento, carrera,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Alumno ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar alumno: {e}")
        db.rollback()

def InsertMaestro(codigo, grado_estudios):
    try:
        sql = "INSERT INTO maestros (codigo, grado_estudios) VALUES (%s, %s)"
        val = (codigo, grado_estudios,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Maestro ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar maestro: {e}")
        db.rollback()

def InsertMateria(nombre_asignatura, creditos, semestre, carrera):
    try:
        sql = "INSERT INTO materias (nombre_asignatura, creditos, semestre, carrera) VALUES (%s, %s, %s, %s)"
        val = (nombre_asignatura, creditos, semestre, carrera,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Materia ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar materia: {e}")
        db.rollback()

def InsertSalon(edificio, nombre_salon):
    try:
        sql = "INSERT INTO salon (edificio, nombre_salon) VALUES (%s, %s)"
        val = (edificio, nombre_salon,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Salón ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar salón: {e}")
        db.rollback()

def InsertGrupo(nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon):
    try:
        max_num_alumnos=int(max_num_alumnos)
        sql = "INSERT INTO grupos (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        print(1)
        val = (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon,)
        print(2)
        print(sql,val)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Grupo ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar grupo: {e}")
        db.rollback()

def InsertCarrera(nombre_carrera, num_semestres):
    try:
        sql = "INSERT INTO carreras (nombre_carrera, num_semestres) VALUES (%s, %s)"
        val = (nombre_carrera, num_semestres,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Carrera ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar carrera: {e}")
        db.rollback()

def InsertUsuarioMateria(codigo_usuario, codigo_materia):
    try:
        try:
            sql = "SELECT codigo_materia, COUNT(*) AS cantidad FROM usuarios_materias WHERE codigo_materia = %s GROUP BY codigo_materia"
            val = (codigo_materia,)
            cursor.execute(sql, val)
            result = cursor.fetchall()
            temp=str(codigo_materia)
            temp=temp.split(maxsplit=1)
            cupos = SelectCuposGrupo(temp[0],temp[-1])
            print(cupos, result[0][-1])
        except:
            pass
        flag=0
        if not result == []:
            try:
                if int(result[0][-1])+1 > int(cupos):
                    flag=1
                    print('entro')
                    messagebox.showerror("Falló al intentar","No hay cupos disponibles")
                    return
            except:
                print("Clase vacía")
        if flag==0:
                sql_select = "SELECT * FROM usuarios_materias WHERE codigo_usuario = %s AND codigo_materia = %s"
                val_select = (codigo_usuario, codigo_materia)
                cursor.execute(sql_select, val_select)
                resultado = cursor.fetchone()
                if resultado:
                    messagebox.showinfo("Error", "Ya estas en esta materia y grupo")
                else:
                        sql = "INSERT INTO usuarios_materias (codigo_usuario, codigo_materia) VALUES (%s, %s)"
                        print("intenta insertar")
                        val = (codigo_usuario, codigo_materia,)
                        cursor.execute(sql, val)
                        db.commit()
                        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-materia ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-materia: {e}")
        db.rollback()

def InsertHorario(horario, turno):
    try:
        sql = "INSERT INTO horarios (horario, turno) VALUES (%s, %s)"
        val = (horario, turno,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Horario ingresado correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al insertar horario: {e}")
        db.rollback()

def InsertGrupoMaestros(codigo_maestro, codigo_grupo):
    try:
        sql = "INSERT INTO grupo_maestros (codigo_maestro, codigo_grupo) VALUES (%s, %s)"
        val = (codigo_maestro, codigo_grupo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-grupo ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-grupo: {e}")
        db.rollback()

def InsertUsuarioHorario(codigo_usuario, horario):
    try:
        sql = "INSERT INTO usuario_horario (codigo_usuario, horario) VALUES (%s, %s)"
        val = (codigo_usuario, horario,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-horario ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-horario: {e}")
        db.rollback()


def Login(nombre_usuario, contrasena):
    try:
        sql = "SELECT * FROM usuarios WHERE nombre_usuario = %s"
        val = (nombre_usuario,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        if (result[-1] == contrasena):
            return result[4]
        else:
            messagebox.showerror("Error", f"Contraseña incorrecta")
            return 3
    except Exception as e:
        messagebox.showerror("Error 404", f"Usuario no encontrado")
        return 3
        
def SelectLogin(nombre_usuario, contrasena):
    try:
        sql = "SELECT * FROM usuarios WHERE nombre_usuario = %s"
        val = (nombre_usuario,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        if (result[-1] == contrasena):
            return result[0]
    except Exception as e:
        pass

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
    
def SelectHorarioDia(codigo):
    try:
        sql = "SELECT turno FROM horarios WHERE horario = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar horario: {e}")
        return None
def SelectMateriaCarrera(codigo):
    try:
        sql = "SELECT carrera FROM materias WHERE nombre_asignatura = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Fallo al intentar seleccionar carrera: {e}")
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
        val = (nombre, apellido_paterno, apellido_materno, perfil, email, nombre_usuario, contrasena, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de usuario actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de usuario: {str(e)}")

def UpdateAlumno(codigo, estado, fecha_nacimiento, carrera):
    try:
        codigo = int(codigo)
        sql = "UPDATE alumnos SET estado=%s, fecha_nacimiento=%s, carrera=%s WHERE codigo = %s"
        val = (estado, fecha_nacimiento, carrera, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de alumno actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de alumno: {str(e)}")

def UpdateMateria(codigo, nombre_asignatura, creditos, semestre, carrera):
    try:
        codigo = int(codigo)
        sql = "UPDATE materias SET nombre_asignatura=%s, creditos=%s, semestre=%s, carrera=%s WHERE codigo = %s"
        val = (nombre_asignatura, creditos, semestre, carrera, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de materia actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de materia: {str(e)}")

def UpdateHorario(codigo, horario, turno):
    try:
        codigo = int(codigo)
        sql = "UPDATE horarios SET horario=%s, turno=%s WHERE codigo = %s"
        val = (horario, turno, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de horario actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de horario: {str(e)}")

def UpdateCarrera(codigo, nombre_carrera, num_semestres):
    try:
        codigo = int(codigo)
        sql = "UPDATE carreras SET nombre_carrera=%s, num_semestres=%s WHERE codigo = %s"
        val = (nombre_carrera, num_semestres, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de carrera actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de carrera: {str(e)}")

def UpdateGrupo(codigo, nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon):
    try:
        codigo = int(codigo)
        sql = "UPDATE grupos SET nombre_grupo=%s, semestre=%s, horario=%s, codigo_materia=%s, codigo_maestro=%s, max_num_alumnos=%s, codigo_salon=%s WHERE codigo = %s"
        val = (nombre_grupo, semestre, horario, codigo_materia, codigo_maestro, max_num_alumnos, codigo_salon, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de grupo actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de grupo: {str(e)}")

def UpdateSalon(codigo, edificio, nombre_salon):
    try:
        codigo = int(codigo)
        sql = "UPDATE salon SET edificio=%s, nombre_salon=%s WHERE codigo = %s"
        val = (edificio, nombre_salon, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de salón actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de salón: {str(e)}")

def UpdateMaestro(codigo, grado_estudios):
    try:
        codigo = int(codigo)
        sql = "UPDATE maestros SET grado_estudios=%s WHERE codigo = %s"
        val = (grado_estudios, codigo,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Exito","Registro de maestro actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error",f"Error al actualizar el registro de maestro: {str(e)}")

def ListarCarreras():
    try:
        sql = "SELECT nombre_carrera FROM carreras"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None
    
def ListarMaterias(carrera):
    try:
        carrera=str(carrera)
        sql = "SELECT nombre_asignatura FROM materias WHERE carrera = %s"
        val = (carrera,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None    
    
def MateriaGrupo(cadena):
    result=[]
    for materia in cadena:    
        try:
            print(materia[0])
            sql = "SELECT nombre_grupo, codigo_materia FROM grupos WHERE codigo_materia = %s"
            val = (materia[0],)
            cursor.execute(sql, val)
            temp = cursor.fetchall()
            if temp!=[]:
                val=str(temp[0][0])+" "+str(temp[0][1])
                print(val)
                result.append(val)
        except Exception:
                pass
    return result
    
def ListarHorarios():
    try:
        sql = "SELECT turno, horario FROM horarios"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None    
    
def GetCodigoHorario(horario):
    try:
        horario=str(horario)
        sql = "SELECT codigo FROM horarios WHERE horario = %s"
        val = (horario,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None
    
def GetCodigoUsuario(horario):
    try:
        horario=str(horario)
        sql = "SELECT codigo FROM usuarios WHERE nombre_usuario = %s"
        val = (horario,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None

def ListaGeneralMaterias():
    try:
        sql = "SELECT nombre_asignatura FROM materias"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None
    
def ListarMaestros():
    try:
        sql = "SELECT nombre_usuario FROM usuarios WHERE perfil='maestro'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None
    
def ListarSalones():
    try:
        sql = "SELECT nombre_salon FROM salon"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        return None

def UpdateUsuarioHorario(usuario_nuevo, horario_nuevo,codigo_usuario, horario):
    try:
        sql = "UPDATE usuario_horario SET codigo_usuario=%s, horario=%s WHERE codigo_usuario=%s AND horario=%s;"
        val = (usuario_nuevo, horario_nuevo, codigo_usuario, horario,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Actualización usuario-horario ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar asociar usuario-horario: {e}")

def SelectGrupo_UsuarioHorario(usuario, horario):
    try:
        sql = "SELECT * FROM grupos WHERE codigo_maestro=%s AND horario=%s;"
        val = (usuario, horario,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def SelectGrupo_SalonHorario(usuario, horario):
    try:
        sql = "SELECT * FROM grupos WHERE codigo_salon=%s AND horario=%s;"
        val = (usuario, horario,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def SelectGrupo_GrupoHorario(grupo, horario):
    try:
        sql = "SELECT * FROM grupos WHERE nombre_grupo=%s AND horario=%s;"
        val = (grupo, horario,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def DeleteUsuarioMateria(codigo_usuario, codigo_materia):
    try:
        sql = "DELETE FROM usuarios_materias WHERE codigo_usuario = %s AND codigo_materia = %s"
        val = (codigo_usuario, codigo_materia,)
        cursor.execute(sql, val)
        db.commit()
        messagebox.showinfo("Acción realizada con éxito","Asociación usuario-materia eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Falló al intentar","Error al intentar eliminar usuario-materia: {e}")
        db.rollback()

def SelectCuposGrupo(grupo, materia):
    try:
        sql = "SELECT max_num_alumnos FROM grupos WHERE nombre_grupo=%s AND codigo_materia=%s;"
        print(grupo,materia)
        val = (grupo, materia,)
        cursor.execute(sql,val)
        result=cursor.fetchone()
        return result[0]
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")
    
def ListarNombresGrupos():
    try:
        sql = "SELECT DISTINCT nombre_grupo FROM grupos"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402") 

def ListarMaestrosGrupos():
    try:
        sql = "SELECT DISTINCT codigo_maestro FROM grupos"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def SelectGrupoMaestroHorario(maestro, horario):
    try:
        sql = "SELECT codigo_materia FROM grupos WHERE codigo_maestro=%s AND horario=%s"
        val = (maestro, horario,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def SelectGrupoNombreHorario(nombre, horario):
    try:
        sql = "SELECT codigo_materia FROM grupos WHERE nombre_grupo=%s AND horario=%s"
        val = (nombre, horario,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

def SelectNombreAlumno(codigo):
    try:
        sql = "SELECT nombre, apellido_paterno, apellido_materno FROM usuarios WHERE codigo=%s"
        print(codigo)
        val = (codigo,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        return result
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")


def ListarAlumnosMateria(materia):
    try:
        sql = "SELECT codigo_usuario FROM usuarios_materias WHERE codigo_materia=%s"
        val = (materia,)
        cursor.execute(sql,val)
        result = cursor.fetchall()
        real=[]
        for user in result:
            real.append(SelectNombreAlumno(user[0]))
        return real
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")
        
def StepListarAlumnosMateria(maestro,materia,horario):
    try:
        sql = "SELECT nombre_grupo FROM grupos WHERE maestro=%s AND horario=%s"
        val = (maestro,horario,)
        cursor.execute(sql,val)
        result = cursor.fetchone()
        info = result[0]
        return ListarAlumnosMateria(info+" "+materia)
    except Exception as e:
        messagebox.showerror("Falló al intentar","No deberías ver esto error 402")

