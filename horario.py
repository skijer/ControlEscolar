import tkinter as tk
from tkinter import messagebox
import CRUD as api
def Horario(info, type):
    ventana_principal = tk.Tk()
    ventana_principal.title("Horario de Clases")

    estilo_encabezado = {'font': ('Helvetica', 10, 'bold'), 'background': '#b0c4de', 'foreground': 'black'}
    estilo_celda = {'font': ('Helvetica', 9), 'background': 'white', 'foreground': 'black'}

    dias = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES"]
    horas = [f"{i:02d}:00 - {i+2:02d}:00" for i in range(7, 19, 2)]

    for i, dia in enumerate(dias, 1):
        tk.Label(ventana_principal, text=dia, **estilo_encabezado).grid(row=0, column=i, sticky="ew", padx=1, pady=1)

    def Imprimir(i, j):
        dias=["lunes ","martes ","miércoles ","jueves ","viernes "]
        horas=[f"{i:02d}:00-{i+2:02d}:00" for i in range(7, 19, 2)]
        if type==1:
            print(info+" "+HoraDia(i,j))
            messagebox.showinfo("Alumnos",api.ListarAlumnosMateria(info+" "+HoraDia(i,j)))
        else:
            print(info,HoraDia(i,j),dias[j-1]+horas[i])
            messagebox.showinfo("Alumnos",api.StepListarAlumnosMateria(info,HoraDia(i,j),dias[j-1]+horas[i]))

    def HoraDia(i,j):
        dias=["lunes ","martes ","miércoles ","jueves ","viernes "]
        horas=[f"{i:02d}:00-{i+2:02d}:00" for i in range(7, 19, 2)]
        try:
            if type==1:
                return api.SelectGrupoNombreHorario(info,dias[j-1]+horas[i])[0]
            else:
                return api.SelectGrupoMaestroHorario(info,dias[j-1]+horas[i])[0]
        except:
            pass

    for i, hora in enumerate(horas):
        tk.Label(ventana_principal, text=hora, **estilo_encabezado).grid(row=i+1, column=0, sticky="ew", padx=1, pady=1)
        for j in range(1, 6):
            texto=HoraDia(i,j)
            if texto!=None:
                entrada = tk.Button(ventana_principal, **estilo_celda, text=f"{texto}",command=lambda fila=i, columna=j: Imprimir(fila,columna))
                entrada.grid(row=i+1, column=j, sticky="ew", padx=1, pady=1)
            else:
                entrada = tk.Button(ventana_principal, **estilo_celda, text="LIBRE",state="disabled")
                entrada.grid(row=i+1, column=j, sticky="ew", padx=1, pady=1)

    tk.Label(ventana_principal, text="NOMBRE:", **estilo_encabezado).grid(row=len(horas)+1, column=0, sticky="ew", padx=1, pady=1)
    tk.Entry(ventana_principal, **estilo_celda, textvariable=info).grid(row=len(horas)+1, column=1, columnspan=2, sticky="ew", padx=1, pady=1)

#    tk.Label(ventana_principal, text="GRADO Y GRUPO:", **estilo_encabezado).grid(row=len(horas)+1, column=3, sticky="ew", padx=1, pady=1)
#    tk.Entry(ventana_principal, **estilo_celda).grid(row=len(horas)+1, column=4, columnspan=2, sticky="ew", padx=1, pady=1)

    boton_mostrar_grupo = tk.Button(ventana_principal, text="Cerrar planeación", command=lambda: mostrar_grupo())
    boton_mostrar_grupo.grid(row=len(horas)+2, column=1, columnspan=4, sticky="ew", padx=1, pady=1)

    def mostrar_grupo():
    
        for fm in ventana_principal.winfo_children():
            fm.destroy()

    for i in range(6):
        ventana_principal.grid_columnconfigure(i, weight=1)

    for i in range(len(horas) + 3):
        ventana_principal.grid_rowconfigure(i, weight=1)
    ventana_principal.mainloop()
