from cgi import test
from cgitb import text
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font

GUI = Tk() #Tตัวใหญ่ เค ตัวเล็ก
GUI.title('Calculated Durian :')
GUI.geometry('1000x700')

bg = PhotoImage(file='durian-removebg-preview.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='Fill your Durians:',font=(None,20))
L.pack()

v_quantity = StringVar() #ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()


def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 120
        messagebox.showinfo('ราคาทั้งหมด','ราคาทุเรียนทั้งหมด {} บาท'.format(calc))
        v_quantity.set('1')
        E1.focus()
    except:
        messagebox.showwarning('Wrong','Please Fill the Number!')
        v_quantity.set('1')
        E1.focus()



B = ttk.Button(GUI, text='คำนวน',command=Cal)
B.pack(ipadx=30, ipady=20, pady=20) #ipad ขยายความกว้างx,y



GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา