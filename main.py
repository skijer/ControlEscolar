import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry('1250x600')
root.title('Control Escolar')
root.resizable(False,False)
global_tier = 0
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
    return

def users_page():
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

root.mainloop()