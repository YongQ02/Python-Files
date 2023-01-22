##tuple = ('a sheng','ajun','a qin')
##print(tuple[0])
##print(tuple)
##print(len(tuple))
##print(min(tuple))
##print(max(tuple))
##
##
##kg = [39,58,20,72,20,20]
##print(min(kg))
##print(kg.count(20))


##numbers = {1,2,3,4,5,6,7,8,9}
##app = {"Icomic",4.9,50000000}
##
##print(numbers)
##print(app)


# Set Union (combine) |
# Set intersection (Value that exists with both set) &
# Set diffenrence (Value that unexists with both set) - "A-B" "B-A"

##A = {1,2,3,}
##B = {3,4,5,6,7}
##print(B&A)
##
##print(A.intersection(B))


##A = {1,2,3,4,5}
##B = {4,5,6,7,8}
##print(A-B)
##print(B.difference(A))

##languages = {"Swift","Java","Python","Kotlin"}
##print(languages)
##languages.add("Golang")
##print(languages)
##languages.update("Kotlin","Swift")
##print(languages)
##print(languages)
##languages.update("Kotlin")
##print(languages)


##A = frozenset([1,2,3,4,5])
##B = frozenset([6,7,8,9,])
##print(A|B)
##A.add(9)
##print(A)

##with open('hero.txt','r') as f:
##    f_content = f.read()
##    print(f_content)

##try:
##    a = 1
##    raise ValueError(a)
##    print(a)
##except Exception as e:
##    print("Something kacau")

##import random
##
##def Data():
##    for i in range(5):
##        yield random.randint(1,10)
##
##for num in Data():
##    print(num)


##class Number:
##    def __init__(self,num1,num2):
##        self.num1 = num1
##        self.num2 = num2
##
##    def __add__(self,other):
##        numb1 = self.num1+other.num1
##        numb2 = self.num2 + other.num2
##        return Number(numb1,numb2)
##
##a1 = Number(1,2)
##a2 = Number(3,4)
##print("addition is",a1 + a2)


##from tkinter import *
##window = Tk()
##window.title('Miharja Class')

##oneone = Button(window,text="1-1",width=8)
##onetwo =Button(window,text="1-2",width=8)
##onethree =Button(window,text="1-3",width=8)
##onefour =Button(window,text="1-4",width=8)
##twoone =Button(window,text="2-1",width=8)
##twotwo =Button(window,text="2-2",width=8)
##twothree =Button(window,text="2-3",width=8)
##twofour =Button(window,text="2-4",width=8)
##threeone =Button(window,text="3-1",width=8)
##threetwo =Button(window,text="3-2",width=8)
##threethree =Button(window,text="3-3",width=8)
##threefour = Button(window,text="3-4",width=8)
##
##oneone.grid(row=0,column=0)
##onetwo.grid(row=0,column=1)
##onethree.grid(row=0,column=2)
##onefour.grid(row=0,column=3)
0##twoone.grid(row=1,column=0)
##twotwo.grid(row=1,column=1)
##twothree.grid(row=1,column=2)
##twofour.grid(row=1,column=3)
##threeone.grid(row=2,column=0)
##threetwo.grid(row=2,column=1)
##threethree.grid(row=2,column=2)
##threefour.grid(row=2,column=3)

##tips = Label(window,text="Name: ")
##txtbox = Entry(window)
##tips.grid(row=0,column=1)
##txtbox.grid(row=0,column=2)

##window.mainloop()




## Use command option to handle events.

##from tkinter import *
##
##def enroll():
##    output["text"] = "Enrolled Succesfully."
##
##root = Tk()
##
##lbl = Label(root, text="Python Course")
##btn = Button(root, text="Enroll Now", command=enroll)
##output = Label()
##lbl.pack()
##btn.pack()
##output.pack()
##
##root.mainloop()


# Import Custom Module

##import oddeven
##
##number = int(input("Enter a number: "))
##print(oddeven.isEven(number))
##print(oddeven.isOdd(number))          



##import requests
##
##url = 'https://google.com'
##
##response = requests.get(url)
##html = response.text
##print(html)


#age = 18
#txt = "My name is Jogh, and I am {}"
#print(txt.format(age))

help('modules')
