from tkinter import*

xy=Tk()

xy.title('Calculator')
xy.geometry('500x500')
#--------------------------------------------------
ti=StringVar()
op=''
#
def BC(v):
    global op
    op=op+str(v)
    ti.set(op)
#This is what cleares the text box
def clear():
    global op
    op=''
    ti.set('')
#This is what evaluates the final expression
def equal():
    try:
        global op
        total=str(eval(op))
        ti.set(total)
        op=''
    except:
        ti.set('error')
        op=''
#---------------------------------------------------
l1=Label(xy,text='Calculator',)
l1.grid(columnspan=5)

textbox=Entry(xy,textvariable=ti)
textbox.grid(columnspan=5)


b1=Button(xy,padx=15, text='7',fg='purple',height=1,command=lambda:BC(7))
b1.grid(row=3, column=0,pady=10)

b2=Button(xy,text='4',padx=15,fg='purple',command=lambda:BC(4))
b2.grid(row=4,column=0,pady=10)

b3=Button(xy,text='1',padx=15,fg='purple',command=lambda:BC(1))
b3.grid(row=5,column=0,pady=10,padx=10)

b4=Button(xy,text='0',padx=15,fg='purple',command=lambda:BC(0))
b4.grid(row=6,column=0,pady=10)

b5=Button(xy,text='8',padx=15,fg='purple',command=lambda:BC(8))
b5.grid(row=3,column=1,pady=10)

b6=Button(xy,text='5',padx=15,fg='purple',command=lambda:BC(5))
b6.grid(row=4,column=1,pady=10)

b7=Button(xy,text='2',padx=15,fg='purple',command=lambda:BC(2))
b7.grid(row=5,column=1,pady=10)

b8=Button(xy,text='9',padx=15,fg='purple',command=lambda:BC(9))
b8.grid(row=3,column=3,pady=10)

b9=Button(xy,text='6',padx=15,fg='purple',command=lambda:BC(6))
b9.grid(row=4,column=3,pady=10)

b10=Button(xy,text='3',padx=15,fg='purple',command=lambda:BC(3))
b10.grid(row=5,column=3,pady=10)

b11=Button(xy,text='/',padx=15,fg='purple',command=lambda:BC('/'))
b11.grid(row=3,column=4,pady=10,padx=10)

b12=Button(xy,text='*',padx=15,fg='purple',command=lambda:BC('*'))
b12.grid(row=4,column=4,pady=10)
                          
b13=Button(xy,text='-',padx=15,fg='purple',command=lambda:BC('-'))
b13.grid(row=5,column=4,pady=10)

b14=Button(xy,text='+',padx=15,fg='purple',command=lambda:BC('+'))
b14.grid(row=6,column=4,pady=10)

b15=Button(xy,text='.',padx=15,width=10,fg='purple',command=lambda:BC('.'))
b15.grid(row=6,column=1,columnspan=3)

b16=Button(xy,text='=',width=25,fg='purple',command=equal)
b16.grid(row=7,columnspan=5,pady=10)

b17=Button(xy,text='CLEAR',height=12,fg='purple',command=clear)
b17.grid(row=3,rowspan=7,column=5,pady=10)
#-----------------------------------------------------------------



xy.mainloop()



