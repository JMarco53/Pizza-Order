from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import tkinter as tk
from tkinter.ttk import *
import threading

#Gui app(tkinter)------------------------------------->
#Main Pizza---------------------------------------------------------------------------------->

#Oder Complete: WOuld you like to....
class PizzaBot:
    #Pizza Size---------------------->
    global button_peperoni
    def GetPizza(self):
        global Pizza_Choice
        #Pizza Choice-------------------->
        self.peperoni = 'https://www5.pizzapizza.ca/catalog/config/pepperoni-collection_12900'
        peperoni = self.peperoni
        self.classic_super = "https://www5.pizzapizza.ca/catalog/config/classic-super-collection_12400"
        classic_super = self.classic_super
        self.meat_supreme = 'https://www5.pizzapizza.ca/catalog/config/meat-supreme-collection_13300'
        meat_supreme = self.meat_supreme
        if Pizza_Choice == "peperoni":
            print("pizza peperoni")
            self.driver.get(peperoni)
        elif Pizza_Choice == "classic":
            self.driver.get(classic_super)
        elif Pizza_Choice == "meat":
            self.driver.get(meat_supreme)
        else:
            print("Please enter a valid pizza choice")
            self.GetPizza(peperoni, classic_super, meat_supreme)
    def GetAmount(self,amount):
        amount -= 1
        for am in range(int(amount)):
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[3]/div[1]/app-quantity-selector/div/div/div/div/button[2]")\
                .click()

    def GetPizzaSize(self):
        global Size_Choice
        self.small = "/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/app-product-size-picker/div/div/button[1]"
        small = self.small
        self.medium = "/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/app-product-size-picker/div/div/button[2]"
        medium = self.medium
        self.large = "/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/app-product-size-picker/div/div/button[3]"
        large = self.large
        self.xlarge = "/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/app-product-size-picker/div/div/button[4]"
        xlarge = self.xlarge
        if Size_Choice == "small":
            self.driver.find_element_by_xpath(small)\
            .click()
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/app-add-product-btn/button")\
            .click()#Submit
        elif Size_Choice == "medium":
            self.driver.find_element_by_xpath(medium)\
            .click()
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/app-add-product-btn/button")\
            .click()#Submit
        elif Size_Choice == "large":
            self.driver.find_element_by_xpath(large)\
            .click()
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/app-add-product-btn/button")\
            .click()#Submit
        elif Size_Choice == "xlarge":
            self.driver.find_element_by_xpath(xlarge)\
            .click()
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-product-configurator/div/div[1]/div[2]/div[1]/div[2]/div/div/div[4]/div/app-add-product-btn/button")\
            .click()#Submit
        else:
            print("Please enter a valid size!")
            GetPizzaSize(small, medium, large, xlarge)
    def __init__(self, email, pw, upgrade_xpath):
        self.driver = webdriver.Chrome()
        self.email = email
        self.upgrade_xpath = upgrade_xpath
        try:
            self.driver.get("https://www.pizzapizza.ca/")#Get to Main Website
            sleep(1)
            progress_bar["value"] = 5
            if self.driver.find_element_by_css_selector("#close-btn"):
                self.driver.find_element_by_css_selector("#close-btn").click()
                sleep(1)
                progress_bar["value"] = 10
            else:
                None
            self.driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-location-modal/div/div[1]/div/div[1]/i")\
            .click()#Enleve la notification
            progress_bar["value"] = 15
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-header/div/div/div/div/nav/div[3]/div/div[4]/app-login-register/div/div[2]/a[1]")\
            .click()
            progress_bar["value"] = 15
            sleep(2)#Étape de connexion
            progress_bar["value"] = 20
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-sign-in/div/div[2]/div[1]/app-sign-in-form-component/div/div/form/div[1]/div/input")\
            .send_keys(email)
            progress_bar["value"] = 25
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-sign-in/div/div[2]/div[1]/app-sign-in-form-component/div/div/form/div[2]/div/input")\
            .send_keys(pw)
            progress_bar["value"] = 30
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-sign-in/div/div[2]/div[1]/app-sign-in-form-component/div/div/form/div[4]/div[1]/button")\
            .click()
            sleep(2)#Connecté au compte Pizza Pizza
            progress_bar["value"] = 35
            self.GetPizza()#Choix de Pizza
            sleep(2)
            progress_bar["value"] = 40
            self.GetAmount(amount)#Choix du montant
            progress_bar["value"] = 45
            self.GetPizzaSize()#Choix de la taille/Pizza commandé
            progress_bar["value"] = 50
            if self.driver.find_element_by_xpath(upgrade_xpath):
                self.driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/app-confirmation-modal/div/div[2]/div/div/div[1]/button")\
                .click()#Closing upgrade pop-up
                progress_bar["value"] = 60
            else:
                None
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-global-cart-overlay/div/div[1]/div/div/div")\
                .click()#Cliquez pour checkout
            progress_bar["value"] = 70
            sleep(2)
            self.driver.find_element_by_css_selector("#cart-overlay-component > div:nth-child(1) > div > div.row.cart-content > div > div.container-fluid.cart-content-container > div.row.my-3.button-row.align-items-end > div")\
            .click()
            progress_bar["value"] = 75
            sleep(1)
            self.driver.find_element_by_xpath("/html/body/app-root/div/app-checkout-container/div/div[2]/div[1]/ngb-accordion/div[1]/div[2]/div/div[3]/button")\
            .click()
            progress_bar["value"] = 80
            self.driver.find_element_by_css_selector("#payment-header > button")\
            .click()#Click on payment method
            progress_bar["value"] = 90
            sleep(1)
            debit = self.driver.find_element_by_css_selector("input[type='radio'][value='Debit']")
            self.driver.execute_script("arguments[0].click();", debit)#Click on Debit Card:Payment method
            progress_bar["value"] = 95
            self.driver.find_element_by_css_selector("body > app-root > div > app-checkout-container > div > div:nth-child(2) > div.col-12.col-md-4 > div > div.col-12.my-3 > app-order-summary > div > div.row.px-4.pt-3 > div > app-add-coupon-widget > div > div.row.align-items-center.h-100 > div > button")\
            .click()#A remplacer par le button Submit quand tout est completé: body > app-root > div > app-checkout-container > div > div:nth-child(2) > div.col-12.col-md-4 > div > div.col-12.my-3 > app-order-summary > div > div.row.px-4.pb-3 > div > button
            progress_bar["value"] = 100
            self.driver.quit()
            #Terminer!!
        except NoSuchElementException:
            pass
        
                                        
#Main Gui variable------------------------------------>
HEIGHT = 500
WIDTH = 600
root = tk.Tk()
root.resizable(width=False, height=False)
#---------------------------------------------------->
Pizza_Choice = ("peperoni", "classic", "meat")
Size_Choice = ("small", "medium", "large", "xlarge")
amount = 0
all_good = False
#Progress Bar------------------------------------------------------------------------------->

#When button click to decide wich pizza type---------->
def onclick_p():
    global Pizza_Choice
    #Disable other button C------------------------------------------->
    button_classic.configure(state='normal', bg="white")
    #Enable other button M------------------------------------------->
    button_meat.configure(state='normal', bg="white")
    Pizza_Choice = "peperoni"
    print(Pizza_Choice)
    button_peperoni.configure(state="disable", bg="#ff7e0e")
def onclick_c():
    global Pizza_Choice
    #Enable other button P------------------------------------------->
    button_peperoni.configure(state='normal', bg="white")
    #Enable other button M ------------------------------------------->
    button_meat.configure(state='normal', bg="white")

    Pizza_Choice = "classic"
    button_classic.configure(state="disable", bg="#ff7e0e")
def onclick_m():
    global Pizza_Choice
    #Enable other button C------------------------------------------->
    button_classic.configure(state='normal', bg="white")
    #Enable other button P------------------------------------------->
    button_peperoni.configure(state='normal', bg="white")

    Pizza_Choice = "meat"
    button_meat.configure(state="disable", bg="#ff7e0e")
#When button click to decide Pizza Size--------------->
def onclick_s():
    global Size_Choice
    #Enable other button xl------------------------------------------->
    button_xlarge.configure(state='normal', bg="white")
    #Enable other button m------------------------------------------->
    button_medium.configure(state='normal', bg="white")
    #Enable other button x------------------------------------------->
    button_large.configure(state='normal', bg="white")

    Size_Choice = "small"
    print(Size_Choice)
    button_small.configure(state="disable", bg="#ff7e0e")
def onclick_md():
    global Size_Choice
    #Enable other button s------------------------------------------->
    button_small.configure(state='normal', bg="white")
    #Enable other button xl------------------------------------------->
    button_xlarge.configure(state='normal', bg="white")
    #Enable other button x------------------------------------------->
    button_large.configure(state='normal', bg="white")

    Size_Choice = "medium"
    button_medium.configure(state="disable", bg="#ff7e0e")
def onclick_l():
    global Size_Choice
    #Enable other button s------------------------------------------->
    button_small.configure(state='normal', bg="white")
    #Enable other button m------------------------------------------->
    button_medium.configure(state='normal', bg="white")
    #Enable other button xl------------------------------------------->
    button_xlarge.configure(state='normal', bg="white")

    Size_Choice = "large"
    button_large.configure(state="disable", bg="#ff7e0e")
def onclick_xl():
    global Size_Choice
    #Enable other button s------------------------------------------->
    button_small.configure(state='normal', bg="white")
    #Enable other button m------------------------------------------->
    button_medium.configure(state='normal', bg="white")
    #Enable other button x------------------------------------------->
    button_large.configure(state='normal', bg="white")
    #Disable/output-------------------------------------------------->
    Size_Choice = "xlarge"
    button_xlarge.configure(state="disable", bg="#ff7e0e")
#When button click to chose PIzza amount
def onclick_plus():
    global amount
    print("Button clicked")
    amount += 1
    pizza_amount.configure(text=str(amount))
    pizza_amount.place(relx=0.45, rely=0.15)
def onclick_minus():
    global amount
    print("Button clicked")
    amount -= 1
    print(amount)
    pizza_amount.config(text=str(clicked))
    pizza_amount.place(relx=0.45, rely=0.15)
def submit_clicked():
    global all_good
    check_if_all_good()
    if all_good == True:
        run_status_bar()
        start = PizzaBot("firephinx53@gmail.com", "jeanmarc123", "/html/body/ngb-modal-window/div/div/app-confirmation-modal/div")
        start.GetPizza(peperoni, classic_super, meat_supreme)
        start.GetAmount(amount)
        start.GetPizzaSize(small, medium, large, xlarge)
        start.__init__("firephinx53@gmail.com", "jeanmarc123", "/html/body/ngb-modal-window/div/div/app-confirmation-modal/div")
        clear_tkinter()
def check_if_all_good():
    global all_good
    global amount
    #Check if Pizza have been selected/if no:error sign
    if Pizza_Choice == "peperoni":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Pizza_Choice == "classic":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Pizza_Choice == "meat":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Pizza_Choice == ("peperoni", "classic", "meat"):
        error_label = tk.Label(image=error_sign)
        error_label.place(relx=0.656, rely=0.86)
    #Check if Size have been selected/if no:error sign
    if Size_Choice == "small":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Size_Choice == "medium":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Size_Choice == "large":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Size_Choice == "xlarge":
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if Size_Choice == ("small", "medium", "large", "xlarge"):
        error_label = tk.Label(image=error_sign)
        error_label.place(relx=0.656, rely=0.86)
    #Check if Amount have been selected/if no:error sign
    if amount > 0:
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
    if amount == 0:
        error_label = tk.Label(image=error_sign)
        error_label.place(relx=0.656, rely=0.86)
    #Else all good/all_good=True:Order started
    else:
        error_label = tk.Label(image=accept_sign)
        error_label.place(relx=0.656, rely=0.86)
        all_good = True

def run_status_bar():
    global progress_bar
    progress_bar["maximum"] = 100
    progress_bar["value"] = 0
def clear_tkinter():
    frame.destroy()
    frame_size.destroy()
    frame_btsize.destroy()
    frame_amount.destroy()
    frame_submit.destroy()

    pizza_amount.destroy()

    plus_button.destroy()
    minus_button.destroy()
    submit_button.destroy()

    pizza_title.config(text="50 Timer")
    pizza_title.place(relx=0.63)
    pizza_type.destroy()

    button_peperoni.destroy()
    button_classic.destroy()
    button_meat.destroy()

    button_small.destroy()
    button_medium.destroy()
    button_large.destroy()
    button_xlarge.destroy()


#Windows + Frame---------------------------------------------->
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas.pack()

progress_bar = Progressbar(orient = 'horizontal', length = 600, mode = 'determinate')
progress_bar.place(relx=0.001, rely=0.95)

app_icon = tk.PhotoImage(file="pizza.png")
root.iconphoto(False, app_icon)

plus_sign = tk.PhotoImage(file="plus.png")
minus_sign = tk.PhotoImage(file="minus.png")

accept_sign = tk.PhotoImage(file="accept.png")
error_sign = tk.PhotoImage(file="error.png")
#Frame + Entry--------------------------------------------------------->
frame = tk.Frame(root, bg='#ff7e0e', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

frame_top = tk.Frame(root, bg='#ff7e0e', bd=5)
frame_top.place(relx=0, rely=0, relwidth=4, relheight=0.1, anchor='n')

frame_size = tk.Frame(root, bg="#ff7e0e", bd=5)
frame_size.place(relx=0.5, rely=0.33, relwidth=0.75, relheight=0.1, anchor='n')

frame_btsize = tk.Frame(root, bg="#ff7e0e", bd=5)
frame_btsize.place(relx=0.5, rely=0.476, relwidth=0.3, relheight=0.1, anchor='n')

frame_amount = tk.Frame(root, bg="white", bd=5)
frame_amount.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1, anchor='n')

frame_submit = tk.Frame(root, bg="#ff7e0e", bd=5)
frame_submit.place(relx=0.5, rely=0.93, relwidth=0.3, relheight=0.1, anchor='s')
#Enter pizza amount--------------------------------->
pizza_amount = tk.Label(frame_amount, text="Enter amount", bg="white", font='CoolveticaRg 18')
pizza_amount.place(relx=0.03, rely=0.15)

plus_button = tk.Button(root, image=plus_sign, bg="white", borderwidth=0, command=lambda : onclick_plus())
plus_button.place(relx=0.25, rely=0.685)

minus_button = tk.Button(root, image=minus_sign, bg="white", borderwidth=0, command=lambda : onclick_minus())
minus_button.place(relx=0.64, rely=0.685)

submit_button = tk.Button(text="Submit", font='CoolveticaRg 18', fg="white", borderwidth=0, bg="#ff7e0e", command=lambda : threading.Thread(target=submit_clicked).start())
submit_button.place(relx=0.5, rely=0.93, relwidth=0.3, relheight=0.1, anchor='s')

#Pizza Pizza Order Haut de page------------------------>
pizza_title = tk.Label(frame_top, text="Pizza Pizza Order", bg='#ff7e0e', fg="white", font='BubbleGum 18')
pizza_title.place(relx=0.58,)
#Type de pizza en-tete--------------------------------->
pizza_type = tk.Label(text="Pizza Type", bg='white', font='Arial 12 bold')
pizza_type.place(relx=0.422, rely=0.15)

pizza_size = tk.Label(text="Pizza Size", borderwidth=0, bg='white', font='Arial 12 bold')
pizza_size.place(relx=0.422, rely=0.43)
#Main button:Pizza Type--------------------------------------------------------------------->
button_peperoni = tk.Button(frame, text="Peperoni", bg="white", font=40, borderwidth=0, command=lambda : onclick_p())
button_peperoni.place(relx=0, relheight=1, relwidth=0.3)

button_classic = tk.Button(frame, text="Classic Super", bg="white", font=40, borderwidth=0, command=lambda : onclick_c())
button_classic.place(relx=0.35, relheight=1, relwidth=0.3)

button_meat = tk.Button(frame, text="Meat Supreme", bg="white", font=40,  borderwidth=0, command=lambda : onclick_m())
button_meat.place(relx=0.70, relheight=1, relwidth=0.3)

#Main button:Pizza Size--------------------------------------------------------------------->
button_small = tk.Button(frame_size, text="Small", bg="white", font=40, borderwidth=0, command=lambda : onclick_s())
button_small.place(relx=0, relheight=1, relwidth=0.3)

button_medium = tk.Button(frame_size, text="Medium", bg="white", font=40, borderwidth=0, command=lambda : onclick_md())
button_medium.place(relx=0.35, relheight=1, relwidth=0.3)

button_large = tk.Button(frame_size, text="Large", bg="white", font=40, borderwidth=0, command=lambda : onclick_l())
button_large.place(relx=0.70, relheight=1, relwidth=0.3)

button_xlarge = tk.Button(frame_btsize, text="X-Large", bg="white", font=40, borderwidth=0, command=lambda : onclick_xl())
button_xlarge.place(relx=0.11, relheight=1, relwidth=0.78)



root.mainloop()
