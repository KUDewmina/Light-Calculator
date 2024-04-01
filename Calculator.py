import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk,Image
import os

root = ctk.CTk()
root.title("Calculator")
root.geometry('343x575')
root.resizable(False,False)

script_directory = os.path.dirname(__file__) #Path to File
btncut_path = os.path.join(script_directory+ "\cut.png") #Path to Cut Image

frame1 = ctk.CTkFrame(root, width=343 ,height=575 ,corner_radius=20 ,fg_color="#E1E6FB" )
frame1.pack(padx=1 ,pady=1)



def show(value):
    equation = l1.cget("text")
    if value == "=" :
           try:
              l2.configure(text=equation)
              result = eval(equation)
              l1.configure(text=result)
           except SyntaxError:
              l1.configure(text="Error")
           except TypeError:
              l1.configure(text="Error")
           except ZeroDivisionError:
              l1.configure(text="Error")
           except ValueError:
              l1.configure(text="Error")   
    else :          
          equation = str(equation)+str(value)
          l1.configure(text=equation)
          #equation = l1.cget(text)


def clear_all():
    global equation
    equation = ""
    l1.configure(text=equation)
    l2.configure(text="")   


def delete_last_character():
    
    current_text = l1.cget("text")
    updated_text = current_text[:-1]  # Remove the last character
    l1.configure(text=updated_text) 
  

#Creating Buttons

button_font = ctk.CTkFont(size=32)
button_font1 = ctk.CTkFont(size=42)
button_font2 = ctk.CTkFont(size=28)

btn0 = ctk.CTkButton(frame1,width=129,height=50, corner_radius=10,fg_color="white" , text="0" , text_color="#077BE5",font=button_font , command=lambda:show("0"))
btn0.place(relx=0.08, rely=0.85)

btndot = ctk.CTkButton(frame1, width=51,height=52, corner_radius=10,fg_color="white" , text="." , text_color="#077BE5",font=button_font, command=lambda:show(".") )
btndot.place(relx=0.54, rely=0.85)

btnequal = ctk.CTkButton(frame1, width=50,height=88, corner_radius=10,fg_color="#369BE4" , text="=" , text_color="white",font=button_font ,command=lambda:show("="))
btnequal.place(relx=0.77, rely=0.79)

btnadd = ctk.CTkButton(frame1, width=50,height=88, corner_radius=10,fg_color="#87C4F0" , text="+" , text_color="#2F2BFA",font=button_font, command=lambda:show("+") )
btnadd.place(relx=0.77, rely=0.59)

btn1 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="1" , text_color="#077BE5",font=button_font , command=lambda:show("1"))
btn1.place(relx=0.08, rely=0.72)

btn2 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="2" , text_color="#077BE5",font=button_font , command=lambda:show("2"))
btn2.place(relx=0.31, rely=0.72)

btn3 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="3" , text_color="#077BE5",font=button_font , command=lambda:show("3"))
btn3.place(relx=0.54, rely=0.72)

btn4 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="4" , text_color="#077BE5",font=button_font, command=lambda:show("4") )
btn4.place(relx=0.08, rely=0.59)

btn5 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="5" , text_color="#077BE5",font=button_font, command=lambda:show("5") )
btn5.place(relx=0.31, rely=0.59)

btn6 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="6" , text_color="#077BE5",font=button_font, command=lambda:show("6") )
btn6.place(relx=0.54, rely=0.59)

btn7 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="7" , text_color="#077BE5",font=button_font, command=lambda:show("7") )
btn7.place(relx=0.08, rely=0.46)

btn8 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="8" , text_color="#077BE5",font=button_font, command=lambda:show("8") )
btn8.place(relx=0.31, rely=0.46)

btn9 = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="9" , text_color="#077BE5",font=button_font , command=lambda:show("9"))
btn9.place(relx=0.54, rely=0.46)

btnminus = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="#87C4F0" , text="-" , text_color="#2F2BFA",font=button_font , command=lambda:show("-"))
btnminus.place(relx=0.77, rely=0.46)

btnAc = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="white" , text="Ac" , text_color="black",font=button_font,command=clear_all)
btnAc.place(relx=0.08, rely=0.33)

btnBackicon = tk.PhotoImage(file = btncut_path)
btnBack = ctk.CTkButton(frame1, width=50,height=50,image=btnBackicon, corner_radius=10,fg_color="white" , text="" , text_color="black",font=button_font ,command=delete_last_character)
btnBack.place(relx=0.31, rely=0.33)

btnDivid = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="#87C4F0" , text="/" , text_color="#2F2BFA",font=button_font, command=lambda:show("/") )
btnDivid.place(relx=0.54, rely=0.33)

btnMultiply = ctk.CTkButton(frame1, width=50,height=50, corner_radius=10,fg_color="#87C4F0" , text="*" , text_color="#2F2BFA",font=button_font, command=lambda:show("*"))
btnMultiply.place(relx=0.77, rely=0.33)

#Creating Labels

l1 = ctk.CTkLabel(frame1 , width = 285, height=60,text_color="black" , font=button_font1, text="" ,anchor="e", justify="right")
l1.place(relx=0.08, rely=0.15)

l2 = ctk.CTkLabel(frame1 , width = 285, height=40,text_color="grey" , font=button_font2, text="" ,anchor="e", justify="right")
l2.place(relx=0.08, rely=0.09)


root.mainloop()
