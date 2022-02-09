# tkinter for gui part
from tkinter import *
from tkinter import ttk
# time for access date and time
from time import *
# menu is module 2
import menu
# random for generating random numbers
import random
# subprocess for accessing the programs of windows
import subprocess
# creation of main gui window
root = Tk()
# making window fullscreen
root.attributes('-fullscreen', True)
# --------definitions ------------------
def close():
    root.destroy()

def reset():
    varFries.set(0)
    varTotal.set(0)
    varTax.set(0)
    varService.set(0)
    varMeal.set(0)
    varOrder.set("")
    varDrinks.set(0)
    varCheeze.set(0)
    varPizza.set(0)
    varBurger.set(0)
    varLunch.set(0)

def recipt(fries, lunch, burger, pizza, cheezeBurger, drinks, varOrder, mealCost, service, tax, tcost):
    bill = "-----------------------------------Your Bill----------------------------------"
    fr = "Fries\t:\t"+str(fries)+" Rs/-"
    lnch = "Lunch\t:\t"+str(lunch)+ "Rs/-"
    pb = "Plane-Burger :\t"+str(burger)+" Rs/-"
    cb = "Cheeze-Burger:\t"+str(cheezeBurger)+" Rs/-"
    dr = "Drinks\t:\t"+str(drinks)+" Rs/-"
    ordr ="Order-Number:\t"+str(varOrder)
    mlcst = "Meal-Cost:\t"+str(mealCost)+" Rs/-"
    srvc = "Service-Charge:\t"+str(service)+" Rs/-"
    tx = "GST-Tax:\t\t"+str(tax)+" Rs/-"
    tc = "Total-Cost:\t"+str(tcost)+" Rs/-"
    ending = "--------------------------------------------------------------------------------"
    l1 = Label(bill_frame, text=bill, font=(8), bg="white")
    l1.place(x=0, y=0)
    l2 = Label(bill_frame, text=ordr, font=(8), bg="white")
    l2.place(x=0, y=30)
    l3 = Label(bill_frame, text=fr, font=(8), bg="white")
    l3.place(x=0,y=60)
    l4 = Label(bill_frame, text=lnch, font=(8), bg="white")
    l4.place(x=0, y=90)
    l5 = Label(bill_frame, text=pb, font=(8), bg="white")
    l5.place(x=0, y=120)
    l6 = Label(bill_frame, text=cb, font=(8), bg="white")
    l6.place(x=0, y=150)
    l7 = Label(bill_frame, text=dr, font=(8), bg="white")
    l7.place(x=0, y=180)
    l8 = Label(bill_frame, text=mlcst, font=(8), bg="white")
    l8.place(x=0, y=210)
    l9 = Label(bill_frame, text=srvc, font=(8), bg="white")
    l9.place(x=0, y=240)
    l10 = Label(bill_frame, text=tx, font=(8), bg="white")
    l10.place(x=0, y=270)
    l11 = Label(bill_frame, text=ending, font=(8), bg="white")
    l11.place(x=0, y=300)
    l12 = Label(bill_frame, text=tc, font=(8), bg="white")
    l12.place(x=0, y=330)
    
def calc():
    # accessing the calculator of windows
    subprocess.Popen("C:\\Windows\\System32\\calc.exe")

def total():
    # getting values of entry boxes
    fries = varFries.get()
    lunch = varLunch.get()
    burger = varBurger.get()
    pizza = varPizza.get()
    cheezeBurger = varCheeze.get()
    drinks = varDrinks.get()
    #-----Random order number generation--------
    x = random.randint(10000000000, 50000000000)
    randomRef = str(x)
    varOrder.set(randomRef)
    #-----Calculating the cost of meals--------
    cost_of_fries = fries * 50
    cost_of_lunch = lunch * 49
    cost_of_pizza = pizza * 69
    cost_of_burger = burger * 30
    cost_of_cburger = cheezeBurger * 35
    cost_of_drinks = drinks * 45
    #-------calculating the total cost ---------------
    total_cost_of_meal = cost_of_fries + cost_of_lunch + cost_of_pizza + cost_of_burger + cost_of_cburger + cost_of_drinks
    y = str(total_cost_of_meal)
    varMeal.set(y)
    # ----calculating Service charge----------
    service = total_cost_of_meal/99
    a = str(service)
    varService.set(a)
    #------calculating tax----------------------------
    tax = total_cost_of_meal*0.18
    b = str(tax)
    varTax.set(tax)
    #------total cost payable-------------------------
    total_cost_pay = total_cost_of_meal + service + tax
    tcost = str(total_cost_pay)
    varTotal.set(tcost)
    # calling recipt function 
    recipt(fries, lunch, burger, pizza, cheezeBurger, drinks, randomRef, total_cost_of_meal, service, tax, tcost)

#------------------------variables----------------------------
varFries = IntVar()
varTotal = IntVar()
varTax = IntVar()
varService = IntVar()
varMeal = IntVar()
varOrder = StringVar()
varDrinks = IntVar()
varCheeze = IntVar()
varPizza = IntVar()
varBurger = IntVar()
varLunch = IntVar()
# -----frames-------------
leftFrame = Frame(root, width=570, height=768, bg="grey20").pack(side=LEFT)
rightFrame = Frame(root, width=800, height=768, bg="grey30").pack(side=RIGHT)
bill_frame =Frame(root, bg="white", width=425, height=390, relief=SUNKEN, bd=10)
bill_frame.place(x=60, y=100)
# ------Branding----------
brand = Label(leftFrame, text="Restuarant Management System", bg="grey20",fg="cornsilk2", font=("segoe-ui",23))
brand.place(x=260, y=30, anchor=CENTER)
# ------Date Time and its functionality definitons ----------
clkLabel = Label(rightFrame, font=('Ariel', 13), bg="grey30",fg="cornsilk2")
clkLabel.place(x=1200, y=30, anchor=CENTER)
# calling function here otherwise it gives us variable error
def mytime():
    format_of_datetime = strftime("%d-%B-%Y\t%H:%M:%S  %p")
    clkLabel.config(text=format_of_datetime)
    clkLabel.after(1000, mytime)
mytime()
# --------Fries meal ----------------------------------
friesLabel = Label(rightFrame, text="Fries Meal", font=("segoe-ui", 15), bg="grey30", fg="white")
friesLabel.place(x=700, y=100)
friesEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15), textvariable=varFries)
friesEntry.place(x=900, y=100)
#---------Lunch Meal -----------------------------------
lunchLabel = Label(rightFrame, text="Lunch Meal", font=("segoe-ui", 15), bg="grey30", fg="white")
lunchLabel.place(x=700, y=150)
lunchEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15), textvariable=varLunch)
lunchEntry.place(x=900, y=150)
#---------Burger Meal-----------------------------------
burgerLabel = Label(rightFrame, text="Plane Burger", font=("segoe-ui", 15), bg="grey30", fg="white")
burgerLabel.place(x=700, y=200)
burgerEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15), textvariable=varBurger)
burgerEntry.place(x=900, y=200)
#---------Pizza Meal -----------------------------------
pizzaLabel = Label(rightFrame, text="Pizza Meal", font=("segoe-ui", 15), bg="grey30", fg="white")
pizzaLabel.place(x=700, y=250)
pizzaEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15), textvariable=varPizza)
pizzaEntry.place(x=900, y=250)
#--------- Cheeze Burger ------------------------------
cheezeBurgerLabel = Label(rightFrame, text="Cheeze Burger", font=("segoe-ui", 15), bg="grey30", fg="white")
cheezeBurgerLabel.place(x=700, y=300)
cheezeBurgerEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15), textvariable=varCheeze)
cheezeBurgerEntry.place(x=900, y=300)
#-------------Drinks------------------------------------
drinksLabel = Label(rightFrame, text="Drinks", font=("segoe-ui", 15), bg="grey30", fg="white")
drinksLabel.place(x=700, y=350)
drinksEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui",15), textvariable=varDrinks)
drinksEntry.place(x=900, y=350)
# ---------Order number ------------------------------
orderLabel = Label(rightFrame, text="Order No.", font=("segoe-ui", 15), bg="grey30", fg="white")
orderLabel.place(x=700, y=450)
orderEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15, "bold", "italic"), textvariable=varOrder)
orderEntry.place(x=900, y=450)
#------------Meals Cost--------------------------------
mealCostLabel = Label(rightFrame, text="Meal Cost", font=("segoe-ui", 15), bg="grey30", fg="white")
mealCostLabel.place(x=700, y=500)
mealCostEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15, "bold", "italic"), textvariable=varMeal)
mealCostEntry.place(x=900, y=500)
#------------Service charge--------------------------------
serviceLabel = Label(rightFrame, text="Service Charge", font=("segoe-ui", 15), bg="grey30", fg="white")
serviceLabel.place(x=700, y=550)
serviceEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15, "bold", "italic"), textvariable=varService)
serviceEntry.place(x=900, y=550)
#------------Tax--------------------------------
taxLabel = Label(rightFrame, text="Tax", font=("segoe-ui", 15), bg="grey30", fg="white")
taxLabel.place(x=700, y=600)
taxEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15, "bold", "italic"), textvariable=varTax)
taxEntry.place(x=900, y=600)
#------------Total--------------------------------
totalLabel = Label(rightFrame, text="Total Cost", font=("segoe-ui", 15), bg="grey30", fg="white")
totalLabel.place(x=700, y=650)
totalEntry = ttk.Entry(rightFrame, width=30, font=("segoe-ui", 15, "bold", "italic"), textvariable=varTotal)
totalEntry.place(x=900, y=650)
# -----------------Buttons------------------------
menuButton = Button(leftFrame, text="Menu", width=20, height=2, font=('segoe-ui', 13),bd=0, bg="cyan3", command=menu.menu)
menuButton.place(x=60, y=500)
totalButton = Button(leftFrame, text="Total Cost", width=20, height=2, font=('segoe-ui', 13), bd=0, bg="cyan3", command=total)
totalButton.place(x=300, y=500)
resetButton = Button(leftFrame, text="Reset", width=20, height=2, font=('segoe-ui', 13), bd=0, bg="cyan3", command=reset)
resetButton.place(x=60, y=580)
calcButton = Button(leftFrame, text="Calculator", width=20, height=2, font=('segoe-ui', 13), bd=0, bg="cyan3", command=calc)
calcButton.place(x=300, y=580)
exitButton = Button(leftFrame, text="Exit", width=20, height=2, font=('segoe-ui', 13), bd=0,  bg="brown1", fg="white",command=close)
exitButton.place(x=180, y=660)
# looping the window
root.mainloop()
