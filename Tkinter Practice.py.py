from tkinter import *

window = Tk()
ProgramTitle = window.title('program')
WindowSize = window.geometry('1080x400')

Title = Label(window, text='Python Course' , font = 200)
Article = Label(window, text='You  can play AI, Web Crawiling , Data Analys, Game Development, Web Development and etc with using Python.\nLooks Interesting ? Lets dive inside and explore more ! ')
Title.pack()
Article.pack()

Empty1 = Label(window, text='')
Empty2 = Label(window, text='')
Empty1.pack()
Empty2.pack()

SigninMessage = Label(window,text='Sign up to explore')
Email = Label(window,text='Email: ')
EmailInput = Entry(window, width = 30)
Pass = Label(window,text='Enter Password: ')
InputPass = Entry(window, width = 30)
Empty3 = Label(window, text='')
Submit = Button(window,text='Comfirm')

SigninMessage.pack()
Email.pack()
EmailInput.pack()
Pass.pack()
InputPass.pack()
Empty3.pack()
Submit.pack()

window.mainloop()