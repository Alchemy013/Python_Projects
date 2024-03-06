from tkinter import *
window = Tk()
window.geometry('550x200')
window.minsize(550,250)
window.maxsize(550,250)
window.title("Website Blocker")

heading=Label(window, text ='Website Blocker' , font ='Courier  ')
heading.pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

label1=Label(window, text ='Enter Website ' , font ='Courier   13 bold')
label1.place(x=200,y=67)

enter_Website = Text(window,font = 'Courier  ',height='2', width = '39')
enter_Website.place(x= 70,y = 90)

def Blocker():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window, text = 'Already Blocked' , font = 'Courier  ')
                display.place(x=200,y=200)
                pass
            
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text = "Blocked", font = 'Courier  ').place(x=230,y =120)


block_button = Button(window, text = 'Block',font = 'Courier  ',pady = 5,command = Blocker ,width = 7, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 150)

window.mainloop()
