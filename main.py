from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import re
import CRUD as api
import horario as planner

root = tk.Tk()
root.geometry('1250x600')
root.title('Control Escolar')
root.resizable(False,False)
tier = 3
usercode = 0
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
        global tier, usercode
        tier=3
        aux = api.Login(username_var.get(),password_var.get())
        if(aux == "administrativo"):
            tier = 0
        if(aux == "alumno"):
            usercode = api.SelectLogin(username_var.get(),password_var.get())
            tier = 2
        if(aux == "maestro"):
            usercode = api.SelectLogin(username_var.get(),password_var.get())
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
    
            
    def check_password_strength(password):
        # Define regular expressions for each of the required elements
        upper_regex = re.compile(r'[A-Z]')
        lower_regex = re.compile(r'[a-z]')
        symbol_regex = re.compile(r'[!@#$%^&*()]')
        digit_regex = re.compile(r'\d')

        # Check if the password contains at least one of each element
        has_upper = bool(upper_regex.search(password))
        has_lower = bool(lower_regex.search(password))
        has_symbol = bool(symbol_regex.search(password))
        has_digit = bool(digit_regex.search(password))
        
        return has_upper and has_lower and has_symbol and has_digit
    
    #Validaciones
    def Validate():
        mes_val=None
        if not check_password_strength(password_var.get()):
            mes_val="\n"+"La contraseña debe contener una mayúscula, una minúscula, un número y un caracter especial"
        #name, lastname contains a number
        validation=name_var.get()
        if not validation.isalpha():
            mes_val="\n"+"El nombre solo debe contener letras"
        validation=last_var.get()
        if not validation.isalpha():
            mes_val=str(mes_val)+"\n"+"El apellido paterno solo debe contener letras"
        validation=last_name2_var.get()
        if not validation.isalpha():
            mes_val=str(mes_val)+"\n"+"El apellido materno solo debe contener letras"
        validation=profile_entry.get()
        if not validation in profiles:
            mes_val=str(mes_val)+"\n"+"No se seleccionó el perfil del usuario"
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@+[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        if not email_regex.match(email_var.get()):
            mes_val=str(mes_val)+"\n"+"No se ingresó una dirección de correo electrónico"
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
                codigo_usuario = api.InsertUsuario(
                    name_var.get(),
                    last_var.get(),
                    last_name2_var.get(),
                    profile_entry.current(),
                    email_var.get(),
                    username_var.get(),
                    password_var.get())
                if (profile_entry.current()==1):
                    api.InsertAlumno(codigo_usuario,"","2011-11-11","")
                if (profile_entry.current()==2):
                    api.InsertMaestro(codigo_usuario,"")
                    
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
            EventClean()

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
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
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
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier, usercode
    frame_state = 0
    print(usercode)
    students_page_fm = tk.Frame(main_fm)
    students_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(students_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(students_page_fm, textvariable=id_search_var, state=tk.DISABLED if tier!=0 else tk.NORMAL)
    id_search_entry.place(x=580, y=30)
    
    #profile_options = tk.OptionMenu(students_page_fm)
    id_var = tk.StringVar()
    id_lbl = tk.Label(students_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(students_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(students_page_fm, text="Nombre: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(students_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    last_var = tk.StringVar()
    last_name_lbl = tk.Label(students_page_fm, text="Apellido Paterno: ")
    last_name_lbl.place(x=230, y=120)
    last_name_entry = tk.Entry(students_page_fm, textvariable=last_var, state="readonly")
    last_name_entry.place(x= 370, y=120)  

    last_name2_var = tk.StringVar()
    last_name2_lbl = tk.Label(students_page_fm, text="Apellido Materno: ")
    last_name2_lbl.place(x=230, y=150)
    last_name2_entry = tk.Entry(students_page_fm, textvariable=last_name2_var, state="readonly")
    last_name2_entry.place(x= 370, y=150)   
    
    email_var = tk.StringVar()
    email_lbl = tk.Label(students_page_fm, text="Email: ")
    email_lbl.place(x=230, y=180)
    email_entry = tk.Entry(students_page_fm, textvariable=email_var, state="readonly")
    email_entry.place(x= 370, y=180) 

    state_var = tk.StringVar()
    state_lbl = tk.Label(students_page_fm, text="Estado: ")
    state_lbl.place(x=530, y=90)
    state_entry = tk.Entry(students_page_fm, textvariable=state_var, state="readonly")
    state_entry.place(x= 670, y=90) 
    
    birth_var = tk.StringVar()
    birth_lbl = tk.Label(students_page_fm, text="Fecha de Nacimiento: ")
    birth_lbl.place(x=530, y=60)
    birth_entry = tk.Entry(students_page_fm, textvariable=birth_var, state="readonly")
    birth_entry.place(x=670, y=60)

    temp = api.ListarCarreras()
    careers=[]
    for career in temp:
        careers.append(career[0])
    career_lbl = tk.Label(students_page_fm, text="Carrera: ")
    career_lbl.place(x=530, y=120)
    career_entry = Combobox(students_page_fm, values=careers, state="disabled")
    career_entry.place(x=670, y=120)
    
    #Validaciones
    def Validate():
        mes_val=None
        #name, lastname contains a number
        validation=career_entry.get()
        if not validation in careers:
            mes_val=str(mes_val)+"\n"+"No se seleccionó una carrera"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectAlumno(id)
            state_var.set(obj[1])
            career_entry.set(obj[3])
            birth_var.set(obj[2])
            try:
                obj = api.SelectUsuario(id)
                id_var.set(obj[0])
                name_var.set(obj[1])
                last_var.set(obj[2])
                last_name2_var.set(obj[3])
                email_var.set(obj[5])
            except:
                pass
            if (usercode==0):
                StateChange(3)
            else:
                subject_entry.config(state="normal")
        except:
            pass
    
    if(usercode!=0):
        EventSearch(usercode)
    
    def carrera_event():
        try:
            temp = api.ListarMaterias(career_entry.get())
            temp = api.MateriaGrupo(temp)
            subjects=[]
            for subject in temp:
                subjects.append(subject)
            return subjects
        except: pass
        
    
    subjects=carrera_event()
    subject_lbl = tk.Label(students_page_fm, text="Materia: ")
    subject_lbl.place(x=530, y=150)
    subject_entry = Combobox(students_page_fm, state="disabled",values=subjects)
    subject_entry.place(x=670, y=150)
        
    def EventSave():
        validate=Validate()
        if validate:
            api.UpdateAlumno(id_var.get(),state_var.get(),birth_var.get(),career_entry.get())
            EventClean()
    
    def EventAdd():
        api.InsertUsuarioMateria(str(id_var.get()),str(subject_entry.get()))    


    def EventClean():
        StateChange(0)
        id_var.set("")
        state_var.set("")
        birth_var.set("")
        subject_entry.set("")
        career_entry.set("")
        name_var.set("")
        last_var.set("")
        last_name2_var.set("")
        email_var.set("")


    def EventDelete():
        api.DeleteUsuarioMateria(id_var.get(),subject_entry.get())    

        
    def StateChange(number):
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0 or tier!=0 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0 else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        
        state_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        career_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        birth_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        subject_entry.config(state=tk.DISABLED if frame_state != 1 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    if tier==0:
        search_btn = tk.Button(students_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0  else tk.NORMAL,
                                command= lambda: EventSearch(id_search_var.get()))
        search_btn.place(x=850, y=30)
        save_btn = tk.Button(students_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                            command=EventSave)
        save_btn.place(x=400, y=200)
        cancel_btn = tk.Button(students_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                            command=EventClean)
        cancel_btn.place(x=445, y=200)
        edit_btn = tk.Button(students_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=lambda: StateChange(2))
        edit_btn.place(x=505, y=200)
    else:
        new_btn = tk.Button(students_page_fm, text="Agregar", state="normal",
                            command=EventAdd)
        new_btn.place(x=340, y=200)
        remove_btn = tk.Button(students_page_fm, text="Remover", state="normal",
                                command=EventDelete)
        remove_btn.place(x=550, y=200)
    if(usercode!=0):
        EventSearch(usercode)
    return

def teachers_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier, usercode
    frame_state = 0
    students_page_fm = tk.Frame(main_fm)
    students_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(students_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(students_page_fm, textvariable=id_search_var, state=tk.DISABLED if tier!=0 else tk.NORMAL)
    id_search_entry.place(x=580, y=30)
    
    id_var = tk.StringVar()
    id_lbl = tk.Label(students_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(students_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(students_page_fm, text="Nombre: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(students_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    last_var = tk.StringVar()
    last_name_lbl = tk.Label(students_page_fm, text="Apellido Paterno: ")
    last_name_lbl.place(x=230, y=120)
    last_name_entry = tk.Entry(students_page_fm, textvariable=last_var, state="readonly")
    last_name_entry.place(x= 370, y=120)  

    last_name2_var = tk.StringVar()
    last_name2_lbl = tk.Label(students_page_fm, text="Apellido Materno: ")
    last_name2_lbl.place(x=230, y=150)
    last_name2_entry = tk.Entry(students_page_fm, textvariable=last_name2_var, state="readonly")
    last_name2_entry.place(x= 370, y=150)   
    
    email_var = tk.StringVar()
    email_lbl = tk.Label(students_page_fm, text="Email: ")
    email_lbl.place(x=230, y=180)
    email_entry = tk.Entry(students_page_fm, textvariable=email_var, state="readonly")
    email_entry.place(x= 370, y=180) 

    birth_var = tk.StringVar()
    birth_lbl = tk.Label(students_page_fm, text="Grado de Estudios: ")
    birth_lbl.place(x=530, y=60)
    birth_entry = tk.Entry(students_page_fm, textvariable=birth_var, state="readonly")
    birth_entry.place(x=670, y=60)

    temp = api.ListaGeneralMaterias()
    subjects = []
    for subject in temp:
        subjects.append(subject[0])
    subject_lbl = tk.Label(students_page_fm, text="Materia: ")
    subject_lbl.place(x=530, y=90)
    subject_entry = Combobox(students_page_fm, values=subjects, state="disabled")
    subject_entry.place(x=670, y=90)

    if(usercode!=0):
        EventSearch(usercode)
    
    #Validaciones
    def Validate():
        mes_val=None
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectMaestro(id)
            birth_var.set(obj[1])  
            try:
                obj = api.SelectUsuario(id)
                id_var.set(obj[0])
                name_var.set(obj[1])
                last_var.set(obj[2])
                last_name2_var.set(obj[3])
                email_var.set(obj[5])
            except:
                pass
            if (usercode == 0):
                StateChange(3)
            else:
                subject_entry.config(state="normal")
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==2):
                api.UpdateMaestro(id_var.get(),birth_var.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        birth_var.set("")
        subject_entry.set("")
        name_var.set("")
        last_var.set("")
        last_name2_var.set("")
        email_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0 or tier!=0 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if (frame_state==0 or frame_state==3) or tier!=0 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0 or tier!=0 else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        
        birth_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        subject_entry.config(state=tk.DISABLED if frame_state != 1 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    if tier==0:
        search_btn = tk.Button(students_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0  else tk.NORMAL,
                                command= lambda: EventSearch(id_search_var.get()))
        search_btn.place(x=850, y=30)
        save_btn = tk.Button(students_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                            command=EventSave)
        save_btn.place(x=400, y=200)
        cancel_btn = tk.Button(students_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                            command=EventClean)
        cancel_btn.place(x=445, y=200)
        edit_btn = tk.Button(students_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=lambda: StateChange(2))
        edit_btn.place(x=505, y=200)
        remove_btn = tk.Button(students_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                                command=EventDelete)
        remove_btn.place(x=550, y=200)
    else:
        temp=api.ListarMateriasDeUsuario(usercode)
        list=[]
        for subject in temp:
            list.append(subject[0])
        new_btn = tk.Button(students_page_fm, text="Agregar", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                            command=lambda : StateChange(1))
        new_btn.place(x=340, y=200)
    return

def subject_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier
    frame_state = 0
    subjects_page_fm = tk.Frame(main_fm)
    subjects_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(subjects_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(subjects_page_fm, textvariable=id_search_var, state=tk.DISABLED if tier!=0 else tk.NORMAL)
    id_search_entry.place(x=580, y=30)
    
    id_var = tk.StringVar()
    id_lbl = tk.Label(subjects_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(subjects_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(subjects_page_fm, text="Materia: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(subjects_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    credits_var = tk.StringVar()
    credits_lbl = tk.Label(subjects_page_fm, text="Créditos: ")
    credits_lbl.place(x=530, y=60)
    credits_entry = tk.Entry(subjects_page_fm, textvariable=credits_var, state="readonly")
    credits_entry.place(x= 670, y=60)  

    semester_var = tk.StringVar()
    semester_lbl = tk.Label(subjects_page_fm, text="Semestre: ")
    semester_lbl.place(x=230, y=120)
    semester_entry = tk.Entry(subjects_page_fm, textvariable=semester_var, state="readonly")
    semester_entry.place(x= 370, y=120)   

    temp = api.ListarCarreras()
    careers=[]
    for career in temp:
        careers.append(career[0])
    career_lbl = tk.Label(subjects_page_fm, text="Carrera: ")
    career_lbl.place(x=530, y=90)
    career_entry = Combobox(subjects_page_fm, values=careers, state="disabled")
    career_entry.place(x=670, y=90)
    
    #Validaciones
    def Validate():
        mes_val=None
        #name, lastname contains a number
        validation=career_entry.get()
        if not validation in careers:
            mes_val=str(mes_val)+"\n"+"No se seleccionó una carrera"
        validation=semester_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"Ingrese un número en semestre"
        validation=credits_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"Ingrese un número en créditos"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectMateria(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            credits_var.set(obj[2])
            semester_var.set(obj[3])
            career_entry.set(obj[4])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==1):
                api.InsertMateria(
                    name_var.get(),
                    credits_var.get(),
                    semester_var.get(),
                    career_entry.get())
            if(frame_state==2):
                api.UpdateMateria(
                    id_var.get(),
                    name_var.get(),
                    credits_var.get(),
                    semester_var.get(),
                    career_entry.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        credits_var.set("")
        semester_var.set("")
        career_entry.set("")
        name_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0 or tier!=0 else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if (frame_state==0 or frame_state==3) or tier!=0 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0 or tier!=0 else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        
        credits_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        career_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        semester_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    search_btn = tk.Button(subjects_page_fm, text="Buscar", state="normal",
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(subjects_page_fm, text="Nuevo", state="normal",
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=200)
    save_btn = tk.Button(subjects_page_fm, text="Salvar", state="disabled",
                         command=EventSave)
    save_btn.place(x=400, y=200)
    cancel_btn = tk.Button(subjects_page_fm, text="Cancelar", state="disabled",
                           command=EventClean)
    cancel_btn.place(x=445, y=200)
    edit_btn = tk.Button(subjects_page_fm, text="Editar", state="disabled",
                         command=lambda: StateChange(2))
    edit_btn.place(x=505, y=200)
    remove_btn = tk.Button(subjects_page_fm, text="Remover", state="disabled",
                            command=EventDelete)
    remove_btn.place(x=550, y=200)
    return

def groups_page():
        #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    temp_hour=tk.StringVar()
    temp_prof=tk.StringVar()
    temp_group=tk.StringVar()
    temp_classroom=tk.StringVar()
    global frame_state, tier, last_hour
    frame_state = 0
    last_hour = 0
    students_page_fm = tk.Frame(main_fm)
    students_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(students_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(students_page_fm, textvariable=id_search_var, state=tk.DISABLED if tier!=0 else tk.NORMAL)
    id_search_entry.place(x=580, y=30)
    
    #profile_options = tk.OptionMenu(students_page_fm)
    id_var = tk.StringVar()
    id_lbl = tk.Label(students_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(students_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(students_page_fm, text="Nombre del grupo: ")
    name_lbl.place(x=530, y=60)
    name_entry = tk.Entry(students_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x=670, y=60)    

    day_var = tk.StringVar()
    day_lbl = tk.Label(students_page_fm, text="Día: ")
    day_lbl.place(x=230, y=90)
    day_entry = tk.Entry(students_page_fm, textvariable=day_var, state="readonly")
    day_entry.place(x= 370, y=90)

    career_var = tk.StringVar()
    career_lbl = tk.Label(students_page_fm, text="Carrera: ")
    career_lbl.place(x=230, y=120)
    career_entry = tk.Entry(students_page_fm, textvariable=career_var, state="readonly")
    career_entry.place(x= 370, y=120)  

    temp = api.ListaGeneralMaterias()
    subjects=[]
    for subject in temp:
        subjects.append(subject[0])

    temp = api.ListarMaestros()
    teachers=[]
    for teacher in temp:
        teachers.append(teacher[0])
    
    teacher_var = tk.StringVar()
    teacher_lbl = tk.Label(students_page_fm, text="Maestro: ")
    teacher_lbl.place(x=230, y=150)
    teacher_entry = Combobox(students_page_fm, values=teachers ,textvariable=teacher_var, state="disabled")
    teacher_entry.place(x= 370, y=150) 

    temp = api.ListarHorarios()
    hours=[]
    for hour in temp:
        hours.append(hour)

    hour_var = tk.StringVar()
    hour_lbl = tk.Label(students_page_fm, text="Hora: ")
    hour_lbl.place(x=530, y=90)
    hour_entry = Combobox(students_page_fm, textvariable=hour_var, values=hours, state="disabled")
    hour_entry.place(x= 670, y=90)
    
    temp = api.ListarSalones()
    classrooms=[]
    for classroom in temp:
        classrooms.append(classroom[0])

    classroom_var = tk.StringVar()
    classroom_lbl = tk.Label(students_page_fm, text="Salón: ")
    classroom_lbl.place(x=530, y=150)
    classroom_entry = Combobox(students_page_fm, values=classrooms ,textvariable=classroom_var, state="disabled")
    classroom_entry.place(x=670, y=150)       

    subject_lbl = tk.Label(students_page_fm, text="Materia: ")
    subject_lbl.place(x=530, y=120)
    subject_entry = Combobox(students_page_fm, values=subjects, state="disabled")
    subject_entry.place(x=670, y=120)
        
    cap_var = tk.StringVar()
    cap_lbl = tk.Label(students_page_fm, text="Max. Alumnos: ")
    cap_lbl.place(x=530, y=180)
    cap_entry = tk.Entry(students_page_fm, textvariable=cap_var, state="readonly")
    cap_entry.place(x= 670, y=180) 
    
    semester_var = tk.StringVar()
    semester_lbl = tk.Label(students_page_fm, text="Semestre: ")
    semester_lbl.place(x=230, y=180)
    semester_entry = tk.Entry(students_page_fm, textvariable=semester_var, state="readonly")
    semester_entry.place(x= 370, y=180) 
    
    #Validaciones
    def Validate():
        mes_val=None
        #name, lastname contains a number
        validation=subject_entry.get()
        if not validation in subjects:
            mes_val=str(mes_val)+"\n"+"No se seleccionó una carrera"
        validation=cap_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"Ingrese la capacidad de alumnos en números"
        if temp_hour.get()==day_var.get()+" "+hour_var.get():
            validation=api.SelectGrupo_UsuarioHorario(teacher_var.get(),str(day_var.get()+" "+hour_var.get()))
        else:
            validation=api.SelectGrupo_UsuarioHorario(teacher_var.get(),hour_var.get())
        if (not validation==None and temp_prof.get()!=teacher_entry.get()):
            mes_val=str(mes_val)+"\n"+"El profesor ya está ocupado en esa hora y ese día"
        if temp_hour.get()==day_var.get()+" "+hour_var.get():
            validation=api.SelectGrupo_GrupoHorario(name_var.get(),str(day_var.get()+" "+hour_var.get()))
        else:
            validation=api.SelectGrupo_GrupoHorario(name_var.get(),hour_var.get())
        if (not validation==None and name_entry.get()!=temp_group.get()):
            mes_val=str(mes_val)+"\n"+"El salon ya está ocupado en esa hora y ese día"
        if temp_hour.get()==day_var.get()+" "+hour_var.get():
            validation=api.SelectGrupo_SalonHorario(classroom_var.get(),str(day_var.get()+" "+hour_var.get()))
        else:
            validation=api.SelectGrupo_SalonHorario(classroom_var.get(),hour_var.get())
        if (not validation==None and temp_classroom.get()!=classroom_entry.get()):
            mes_val=str(mes_val)+"\n"+"El salon ya está ocupado en esa hora y ese día"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectGrupo(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            semester_var.set(obj[2])
            cadena=str(obj[3]).split(" ")
            hour_var.set(cadena[-1])
            subject_entry.set(obj[4])
            teacher_var.set(obj[5])
            cap_var.set(obj[6])
            classroom_var.set(obj[7])
            day_var.set(cadena[0])
            career_var.set(api.SelectMateriaCarrera(subject_entry.get()))
            temp_hour.set(obj[3])
            temp_prof.set(obj[5])
            temp_classroom.set(obj[7])
            temp_group.set(obj[1])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if (frame_state==1):
                api.InsertGrupo(
                    name_var.get(),
                    semester_var.get(),
                    hour_var.get(),
                    subject_entry.get(),
                    teacher_var.get(),
                    cap_var.get(),
                    classroom_var.get())
                cod=api.GetCodigoUsuario(teacher_var.get())
                cod=cod[0]
                api.InsertUsuarioHorario(cod,hour_var.get())
            if(frame_state==2):
                if not temp_hour.get()!=(day_var.get()+" "+hour_var.get()):
                    hour_var.set(temp_hour.get())
                api.UpdateGrupo(id_var.get(),
                name_var.get(),
                semester_var.get(),
                hour_var.get(),
                subject_entry.get(),
                teacher_var.get(),
                cap_var.get(),
                classroom_var.get())
                cod1=api.GetCodigoUsuario(teacher_var.get())
                cod1=cod1[0]
                cod2=api.GetCodigoUsuario(temp_prof.get())
                cod2=cod2[0]
                api.UpdateUsuarioHorario(cod1,hour_var.get(),cod2,temp_hour.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        hour_var.set("")
        classroom_var.set("")
        subject_entry.set("")
        name_var.set("")
        day_var.set("")
        teacher_var.set("")
        cap_var.set("")
        semester_var.set("")
        career_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0 or tier!=0 else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if (frame_state==0 or frame_state==3) or tier!=0 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0 or tier!=0 else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 or tier!=0 else tk.NORMAL)
        
        hour_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        classroom_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        subject_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        teacher_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        cap_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        semester_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
    #Botones
    search_btn = tk.Button(students_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0  else tk.NORMAL,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(students_page_fm, text="Nuevo", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=250)
    save_btn = tk.Button(students_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                        command=EventSave)
    save_btn.place(x=400, y=250)
    cancel_btn = tk.Button(students_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                        command=EventClean)
    cancel_btn.place(x=445, y=250)
    edit_btn = tk.Button(students_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                        command=lambda: StateChange(2))
    edit_btn.place(x=505, y=250)
    remove_btn = tk.Button(students_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=EventDelete)
    remove_btn.place(x=550, y=250)
    return

def schedule_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier
    frame_state = 0
    classroom_page_fm = tk.Frame(main_fm)
    classroom_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(classroom_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(classroom_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=580, y=30)
    
    id_var = tk.StringVar()
    id_lbl = tk.Label(classroom_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(classroom_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(classroom_page_fm, text="Hora: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(classroom_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    turns = ['lunes', 'martes','miercoles','jueves','viernes']
    turn_var = tk.StringVar()
    turn_lbl = tk.Label(classroom_page_fm, text="Día: ")
    turn_lbl.place(x=230, y=120)
    turn_entry = Combobox(classroom_page_fm, values=turns, textvariable=turn_var,state=tk.DISABLED if frame_state!=2 or frame_state!=1 else tk.NORMAL)
    turn_entry.place(x=370, y=120)
    
    #Validaciones
    def Validate():
        mes_val=None
        validation = turn_var.get()
        if not validation in turns:
            mes_val=str(mes_val)+"\n"+"No se seleccionó el turno del horario"
        validation = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]\-([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
        if not validation.match(name_var.get()) is not None:
            mes_val=str(mes_val)+"\n"+"Escribe la hora en formato HH:MM-HH:MM"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True
        

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectHorario(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            turn_var.set(obj[2])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==1):
                api.InsertHorario(
                    name_var.get(),
                    turn_var.get())
            if(frame_state==2):
                api.UpdateHorario(
                    id_var.get(),
                    name_var.get(),
                    turn_var.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        turn_entry.set("")
        name_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0  else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0  else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3  else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        
        turn_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    search_btn = tk.Button(classroom_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0 else tk.NORMAL,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(classroom_page_fm, text="Nuevo", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=200)
    save_btn = tk.Button(classroom_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                         command=EventSave)
    save_btn.place(x=400, y=200)
    cancel_btn = tk.Button(classroom_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                           command=EventClean)
    cancel_btn.place(x=445, y=200)
    edit_btn = tk.Button(classroom_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                         command=lambda: StateChange(2))
    edit_btn.place(x=505, y=200)
    remove_btn = tk.Button(classroom_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=EventDelete)
    remove_btn.place(x=550, y=200)
    return

def classroom_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier
    frame_state = 0
    classroom_page_fm = tk.Frame(main_fm)
    classroom_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(classroom_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(classroom_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=580, y=30)
    
    id_var = tk.StringVar()
    id_lbl = tk.Label(classroom_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(classroom_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(classroom_page_fm, text="Aula: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(classroom_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    building_var = tk.StringVar()
    building_lbl = tk.Label(classroom_page_fm, text="Edificio: ")
    building_lbl.place(x=230, y=120)
    building_entry = tk.Entry(classroom_page_fm, textvariable=building_var, state="readonly")
    building_entry.place(x= 370, y=120)   
    
    #Validaciones
    def Validate():
        mes_val=None
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectSalon(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            building_var.set(obj[2])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==1):
                api.InsertSalon(
                    building_var.get(),
                    name_var.get())
            if(frame_state==2):
                api.UpdateSalon(
                    id_var.get(),
                    building_var.get(),
                    name_var.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        building_var.set("")
        name_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0  else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0  else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3  else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        
        building_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    search_btn = tk.Button(classroom_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0 else tk.NORMAL,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(classroom_page_fm, text="Nuevo", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=200)
    save_btn = tk.Button(classroom_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                         command=EventSave)
    save_btn.place(x=400, y=200)
    cancel_btn = tk.Button(classroom_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                           command=EventClean)
    cancel_btn.place(x=445, y=200)
    edit_btn = tk.Button(classroom_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                         command=lambda: StateChange(2))
    edit_btn.place(x=505, y=200)
    remove_btn = tk.Button(classroom_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=EventDelete)
    remove_btn.place(x=550, y=200)
    return

def degree_page():
    #states
    # 0 Search - 1 Create - 2 Edit - 3 Display
    global frame_state, tier
    frame_state = 0
    degrees_page_fm = tk.Frame(main_fm)
    degrees_page_fm.pack(fill=tk.BOTH, expand=True)

    id_search_label = tk.Label(degrees_page_fm, text="Ingrese ID a Buscar:")
    id_search_label.place(x=430, y=30)
    id_search_var = tk.StringVar()
    id_search_entry = tk.Entry(degrees_page_fm, textvariable=id_search_var)
    id_search_entry.place(x=580, y=30)
    
    id_var = tk.StringVar()
    id_lbl = tk.Label(degrees_page_fm, text="Código: ")
    id_lbl.place(x=230, y=60)
    id_entry = tk.Entry(degrees_page_fm, textvariable=id_var, state="readonly")
    id_entry.place(x= 370, y=60)

    name_var = tk.StringVar()
    name_lbl = tk.Label(degrees_page_fm, text="Nombre: ")
    name_lbl.place(x=230, y=90)
    name_entry = tk.Entry(degrees_page_fm, textvariable=name_var, state="readonly")
    name_entry.place(x= 370, y=90)    

    semester_var = tk.StringVar()
    semester_lbl = tk.Label(degrees_page_fm, text="Número de semestres: ")
    semester_lbl.place(x=230, y=120)
    semester_entry = tk.Entry(degrees_page_fm, textvariable=semester_var, state="readonly")
    semester_entry.place(x= 370, y=120)   
    
    #Validaciones
    def Validate():
        mes_val=None
        #name, lastname contains a number
        validation=name_entry.get()
        if not all(x.isalpha() or x.isspace() for x in validation):
            mes_val=str(mes_val)+"\n"+"La carrera debe contener solo letras"
        validation=semester_var.get()
        if not validation.isdigit():
            mes_val=str(mes_val)+"\n"+"Ingrese los semestres en números"
        if mes_val:
            messagebox.showerror("Error al validar inputs",mes_val)
            return False
        else:
            return True

    #Eventos
    def EventSearch(id):
        try:
            obj = api.SelectCarrera(id)
            id_var.set(obj[0])
            name_var.set(obj[1])
            semester_var.set(obj[2])
            StateChange(3)
        except:
            pass
        
    def EventSave():
        validate=Validate()
        if validate:
            if(frame_state==1):
                api.InsertCarrera(
                    name_var.get(),
                    semester_var.get())
            if(frame_state==2):
                api.UpdateCarrera(
                    id_var.get(),
                    name_var.get(),
                    semester_var.get())
            EventClean()

    def EventClean():
        StateChange(0)
        id_var.set("")
        semester_var.set("")
        name_var.set("")


    def EventDelete():
        messagebox.showwarning("Failed","Yet to be implemented")
        
    def StateChange(number):
        global frame_state
        frame_state=number
        search_btn.config(state=tk.DISABLED if frame_state!=0  else tk.NORMAL)
        new_btn.config(state=tk.DISABLED if frame_state==2 or frame_state==1 or frame_state==3 else tk.NORMAL)
        save_btn.config(state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL)
        cancel_btn.config(state=tk.DISABLED if frame_state==0  else tk.NORMAL)
        edit_btn.config(state=tk.DISABLED if frame_state!=3  else tk.NORMAL)
        remove_btn.config(state=tk.DISABLED if frame_state!=3 else tk.NORMAL)
        
        semester_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        name_entry.config(state=tk.DISABLED if frame_state != 2 and frame_state != 1 else tk.NORMAL)
        
        #Botones
    search_btn = tk.Button(degrees_page_fm, text="Buscar", state=tk.DISABLED if frame_state!=0 else tk.NORMAL,
                            command= lambda: EventSearch(id_search_var.get()))
    search_btn.place(x=850, y=30)
    new_btn = tk.Button(degrees_page_fm, text="Nuevo", state=tk.DISABLED if frame_state==2 or frame_state==1 else tk.NORMAL,
                        command=lambda : StateChange(1))
    new_btn.place(x=350, y=200)
    save_btn = tk.Button(degrees_page_fm, text="Salvar", state=tk.DISABLED if frame_state==0 or frame_state==3 else tk.NORMAL,
                         command=EventSave)
    save_btn.place(x=400, y=200)
    cancel_btn = tk.Button(degrees_page_fm, text="Cancelar", state=tk.DISABLED if frame_state==0 else tk.NORMAL,
                           command=EventClean)
    cancel_btn.place(x=445, y=200)
    edit_btn = tk.Button(degrees_page_fm, text="Editar", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                         command=lambda: StateChange(2))
    edit_btn.place(x=505, y=200)
    remove_btn = tk.Button(degrees_page_fm, text="Remover", state=tk.DISABLED if frame_state!=3 else tk.NORMAL,
                            command=EventDelete)
    remove_btn.place(x=550, y=200)
    return

def planner_page():
    students_page_fm = tk.Frame(main_fm)
    students_page_fm.pack(fill=tk.BOTH, expand=True)
    
    temp=api.ListarNombresGrupos()
    grupos=[]
    for grupo in temp:
        grupos.append(grupo[0])
    group_lbl = tk.Label(students_page_fm, text="Buscar por Nombre de Grupo: ")
    group_lbl.place(x=330, y=90)
    group_entry = Combobox(students_page_fm, values=grupos, state="normal")
    group_entry.place(x=530, y=90)

    temp=api.ListarMaestrosGrupos()
    teachers=[]
    for teacher in temp:
        teachers.append(teacher[0])
    teacher_lbl = tk.Label(students_page_fm, text="Buscar por Maestro: ")
    teacher_lbl.place(x=330, y=120)
    teacher_entry = Combobox(students_page_fm, values=teachers, state="normal")
    teacher_entry.place(x=530, y=120)

    def SearchGroup():
        if group_entry.get() in grupos: 
            planner.Horario(group_entry.get(),1)
        else:
            messagebox("Error","No seleccionó un grupo")

    def SearchTeacher():
        if teacher_entry.get() in teachers:
            planner.Horario(teacher_entry.get(),2)
        else:
            messagebox("Error","No seleccionó un maestro")

    group_btn=tk.Button(students_page_fm, text="Confirmar",command=SearchGroup)
    group_btn.place(x=700,y=90)
    teachers_btn=tk.Button(students_page_fm, text="Confirmar",command=SearchTeacher)
    teachers_btn.place(x=700,y=120)
    return

options_fm.pack(pady=5)
options_fm.pack_propagate(False)
options_fm.configure(width=1300, height=35)

main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)

switch(indicator_lb=login_indicator_lb, page=login_page)

root.mainloop()