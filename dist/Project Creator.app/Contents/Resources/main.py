from tkinter import *
import os
from tkinter import filedialog



main_window = Tk()
main_window.title('Create Project')
main_window.iconbitmap('/Users/unknowncosmicdot/PythonProjects/create-project/icon.ico')
main_window.geometry('500x700+200+200')
main_window.configure(bg='#282c34')

path = str()


def create_C_file(the_name):

    print(the_name)

    file_name = 'main.c'

    os.mkdir(f'{path}/{the_name}')

    c_file = open(f'{path}/{the_name}/{file_name}','w+')

    c_file.write('#include<stdio.h>\n')
    c_file.write('#include<stdlib.h>\n\n')
    c_file.write('int function();\n\n\n')

    c_file.write('int main(){\n\n\n}\n\n\n')
    c_file.write('int function(){\n\n}\n')
    

    c_file.close()


    c_src = open(f'{path}/{the_name}/source.c','w+')
    c_src.close()

    c_header = open(f'{path}/{the_name}/header.h','w+')
    c_header.write('#ifndef HEADER_H_INCLUDED\n#define HEADER_H_INCLUDED|\n\n\n\n\n\n')
    c_header.write('#endif HEADER_H_INCLUDED')

    c_header.close()


def get_location():
    global path
    path = filedialog.askdirectory()
    print(path)


def main():
    global the_name
    project_name = Entry(main_window)
    project_name.place(width=250, heigh=30, x=10, y=10)
    
    def cr():
        the_name = project_name.get()    

        file_type = clicked.get()

        if (file_type == 'C File'):
            create_C_file(the_name)
            exit()

        elif (file_type == 'Python File'):
            print("I'm busy at the moment!")
            exit()


    options = ["C File","Python File"]
    option_box = StringVar(main_window)

    for data in options:
        option_box.set(data)

    global clicked
    
    clicked = StringVar()
    
    option_menu = OptionMenu( main_window, clicked, *options)
    option_menu.place(width=250, heigh=30, x=10, y=50)


    project_name_label = Label(main_window,text='Project Name', bg='#282c34')
    project_name_label.config(fg='#d7dae0')
    project_name_label.place(x=270, y=10)


    option_box_label = Label(main_window, text='Language', bg='#282c34')
    option_box_label.config(fg='#d7dae0')
    option_box_label.place(x=270, y=50)



    create = Button(main_window ,text='Create', font = '20', bg='green', fg='black', command=cr)
    create.place( x=10, y=170, width=80, heigh=68)

    choose_location = Button(main_window, text='Choose Location..', font = '20', bg='green', fg='black', command=get_location)
    choose_location.place(x=10, y=90, width=250, heigh=30)

main()
main_window.mainloop()
