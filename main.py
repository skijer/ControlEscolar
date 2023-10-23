from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import CRUD as api

root = tk.Tk()
root.geometry('1250x600')
root.title('Control Escolar')
root.resizable(False,False)
tier = 3
frame_state = IntVar()
options_fm = tk.Frame(root, bg = 'gray')

def switch(indicator_lb, page):
    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg'] = 'SystemButtonFace'
            
    indicator_lb['bg'] = '#0097e8'
    
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()

    page()

login_btn = tk.Button(options_fm, text='Login', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=login_indicator_lb, page=login_page))
login_btn.place (x=0, y=0, width=125)

login_indicator_lb = tk.Label(options_fm, bg='#0097e8')
login_indicator_lb.place(x=22, y=30, width=80, height=2)

users_btn = tk.Button(options_fm, text='Usuarios', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=users_indicator_lb, page=users_page), state="disabled")
users_btn.place (x=125, y=0, width=125)

users_indicator_lb = tk.Label(options_fm, bg='#0097e8')
users_indicator_lb.place(x=147, y=30, width=80, height=2)

students_btn = tk.Button(options_fm, text='Alumnos', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=students_indicator_lb, page=students_page), state="disabled")
students_btn.place (x=250, y=0, width=125)
students_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
students_indicator_lb.place(x=272, y=30, width=80, height=2)

teachers_btn = tk.Button(options_fm, text='Maestros', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                         command=lambda: switch(indicator_lb=teachers_indicator_lb, page=teachers_page), state="disabled")
teachers_btn.place (x=375, y=0, width=125)

teachers_indicator_lb = tk.Label(options_fm, bg='#0097e8')
teachers_indicator_lb.place(x=397, y=30, width=80, height=2)

subject_btn = tk.Button(options_fm, text='Materias', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=subject_indicator_lb, page=subject_page), state="disabled")
subject_btn.place (x=500, y=0, width=125)

subject_indicator_lb = tk.Label(options_fm, bg='#0097e8')
subject_indicator_lb.place(x=522, y=30, width=80, height=2)

group_btn = tk.Button(options_fm, text='Grupos', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                      command=lambda: switch(indicator_lb=group_indicator_lb, page=groups_page), state="disabled")
group_btn.place (x=625, y=0, width=125)

group_indicator_lb = tk.Label(options_fm, bg='#0097e8')
group_indicator_lb.place(x=647, y=30, width=80, height=2)

schedule_btn = tk.Button(options_fm, text='Horario', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=schedule_indicator_lb, page=schedule_page), state="disabled")
schedule_btn.place (x=750, y=0, width=125)
schedule_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
schedule_indicator_lb.place(x=772, y=30, width=80, height=2)

classroom_btn = tk.Button(options_fm, text='Salón', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=classroom_indicator_lb, page=classroom_page), state="disabled")
classroom_btn.place (x=875, y=0, width=125)
classroom_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
classroom_indicator_lb.place(x=897, y=30, width=80, height=2)

degree_btn = tk.Button(options_fm, text='Carreras', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=degree_indicator_lb, page=degree_page), state="disabled")
degree_btn.place (x=1000, y=0, width=125)
degree_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
degree_indicator_lb.place(x=1022, y=30, width=80, height=2)

planner_btn = tk.Button(options_fm, text='Planeación', font=('Arial', 13), bd = 0, fg = '#0097e8', activebackground='#0097e8', 
                        command=lambda: switch(indicator_lb=planner_indicator_lb, page=planner_page), state="disabled")
planner_btn.place (x=1125, y=0, width=125)
planner_indicator_lb = tk.Label(options_fm, state="disabled",bg='#0097e8')
planner_indicator_lb.place(x=1147, y=30, width=80, height=2)


def login_page():
    login_page_fm = tk.Frame(main_fm)
    login_page_fm.pack(fill=tk.BOTH, expand=True)
    
    login_page_lb = tk.Label(login_page_fm, text='Bienvenido al sistema de \nControl Escolar', font=('Arial', 30), fg='#0097e8')
    login_page_lb.place(x=420, y=30)

    username_var = tk.StringVar()
    username_label = tk.Label(login_page_fm, text="Usuario:")
    username_label.place(x=550, y=250)
    username_entry = tk.Entry(login_page_fm, textvariable=username_var)
    username_entry.place(x=620, y=250)

    password_var = tk.StringVar()
    password_label = tk.Label(login_page_fm, text="Contraseña:")
    password_label.place(x=550, y=280)
    password_entry = tk.Entry(login_page_fm, show="*", textvariable=password_var)
    password_entry.place(x=620, y=280)

    def EventLogin():
        global tier
        tier=3
        aux = api.Login(username_var.get(),password_var.get())
        if(aux == "administrativo"):
            tier = 0
        if(aux == "alumno"):
            tier = 2
        if(aux == "maestro"):
            tier = 1
        users_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        students_btn.config(state=tk.NORMAL if tier==0 or tier==2 else tk.DISABLED)
        teachers_btn.config(state=tk.NORMAL if tier==0 or tier==1 else tk.DISABLED)
        subject_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        classroom_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        group_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        schedule_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        degree_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)
        planner_btn.config(state=tk.NORMAL if tier==0 else tk.DISABLED)

    
    userfm_btn = tk.Button(login_page_fm, text="Iniciar Sesión", command=EventLogin)
    userfm_btn.place(x=550, y=310)
    root.bind("<Return>", lambda event: userfm_btn.invoke())

    return

def users_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state
    frame_state = 0
    users_page_fm = tk.Frame(main_fm)
    users_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(users_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(users_page_fm, textvariable=id_search_var, state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL)
    id_search_entry.place(x=580, y=30)
    
    #profile_options = tk.OptionMenu(users_page_fm)
    id_var = tk.StringVar()
    id_lbl = tk.Label(users_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(users_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(users_page_fm, text="Nombre: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(users_page_fm, textvariable=name_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    name_entry.place(x= 370, y=90)    

    last_var = tk.StringVar()
    last_name_lbl = tk.Label(users_page_fm, text="Apellido Paterno: ")
    last_name_lbl.place(x=230, y=120)
    last_name_entry = tk.Entry(users_page_fm, textvariable=last_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    last_name_entry.place(x= 370, y=120)  

    last_name2_var = tk.StringVar()
    last_name2_lbl = tk.Label(users_page_fm, text="Apellido Materno: ")
    last_name2_lbl.place(x=230, y=150)
    last_name2_entry = tk.Entry(users_page_fm, textvariable=last_name2_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    last_name2_entry.place(x= 370, y=150)   
    
    email_var = tk.StringVar()
    email_lbl = tk.Label(users_page_fm, text="Email: ")
    email_lbl.place(x=530, y=60)
    email_entry = tk.Entry(users_page_fm, textvariable=email_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    email_entry.place(x= 670, y=60) 

    username_var = tk.StringVar()
    username_lbl = tk.Label(users_page_fm, text="Nombre de usuario: ")
    username_lbl.place(x=530, y=90)
    username_entry = tk.Entry(users_page_fm, textvariable=username_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    username_entry.place(x= 670, y=90) 
    
    password_var = tk.StringVar()
    password_lbl = tk.Label(users_page_fm, text="Contraseña: ")
    password_lbl.place(x=530, y=120)
    password_entry = tk.Entry(users_page_fm, textvariable=password_var, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    password_entry.place(x=670, y=120)

    profiles = ['administrativo', 'alumno','maestro']
    profile_lbl = tk.Label(users_page_fm, text="Perfil: ")
    profile_lbl.place(x=530, y=150)
    profile_entry = Combobox(users_page_fm, values=profiles, state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    profile_entry.place(x=670, y=150)
    
    #Validaciones
    def Validate():
        validation=name_var.get()
        mes_val=None
        if not validation.isalpha():
            mes_val="\n"+"El nombre solo debe contener letras"
        validation=last_var.get()
        if not validation.isalpha():
            mes_val=str(mes_val)+"\n"+"El apellido solo debe contener letras"
        validation=last_name2_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"El télefono solo debe contener números"
        validation=profile_entry.get()
        if not validation in profiles:
            mes_val=str(mes_val)+"\n"+"No se seleccionó el perfil del usuario"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        
    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectUsuario(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            last_var.set(obj[2])
            last_name2_var.set(obj[3])
            profile_entry.set([obj[4]])
            email_var.set(obj[5])
            username_var.set(obj[6])
            password_var.set(obj[7])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==1):
                api.InsertUsuario(
                name_var.get(),
                last_var.get(),
                last_name2_var.get(),
                profile_entry.current(),
                email_var.get(),
                username_var.get(),
                password_var.get())
            if(frame_state==2):
                api.UpdateUsuario(
                id_var.get(),
                name_var.get(),
                last_var.get(),
                last_name2_var.get(),
                profile_entry.current(),
                email_var.get(),
                username_var.get(),
                password_var.get())

    def EventClean():
        StateChange(0)
        id_var.set("")
        username_var.set("")
        password_var.set("")
        profile_entry.set("")
        name_var.set("")
        last_var.set("")
        last_name2_var.set("")
        email_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0 else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0 else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        id_search_entry.config(state=tk.DISABLED if frame_state !=0 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        last_name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        last_name2_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        email_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        username_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        password_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        profile_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    search_btn = tk.Button(users_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0 else tk.NORMAL,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(users_page_fm, text="Nuevo", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=200)
    save_btn = tk.Button(users_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                         command=EventSave)
    save_btn.place(x=400, y=200)
    cancel_btn = tk.Button(users_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                           command=EventClean)
    cancel_btn.place(x=445, y=200)
    edit_btn = tk.Button(users_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                         command=lambda: StateChange(2))
    edit_btn.place(x=505, y=200)
    remove_btn = tk.Button(users_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=EventDelete)
    remove_btn.place(x=550, y=200)

    return

def students_page():
    return

def teachers_page():
    return

def subject_page():
    return

def groups_page():
    return

def schedule_page():
    return

def classroom_page():
    return

def degree_page():
    return

def planner_page():
    return

options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=1300, height=35)

main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)

switch(indicator_lb=login_indicator_lb, page=login_page)

root.mainloop()