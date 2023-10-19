import time
from colorama import Fore, Back, Style, init
# from termcolor  import colored
#This is a Bot that is supposed to help customers make orders and purchase diffrent types of berverages.
#welcome and take user input
def passed():
   print("Hello", name,". Welcome to Munisha\'s Coffee Point")
print("Welcome to Munisha\'s Coffee Point.")


name = input("What is your name?\n")

#there are reports that people named Kalechi are not to enteer in the premises due to some wanted person in the area


if name == "Kalechi".lower():
    second_name = input("What is your second name? \n")
    if second_name == "Maina".lower():
        location = input("Where are you from? \n")
        if location == "Bamburi".lower():
            evil_deeds = int(input("How many evil deeds have you commited today, "+str(name)+"?\n"))
            if evil_deeds >= 4:
                print(name, ", you are not welcome in Munisha\'s Coffee Point. Kindly exit the premises!!")
                exit()
            else:
                print("Oh. You are one of the good ",name+"\'s, come on in!!")
    else:
        passed()
else:
    passed()
    time.sleep(2)

#display all the producs and prices of the products sold in the coffee point
print("We offer the following coffee flavours. Choose your best of the one that interests you")
flavours = ['Vanilla', 'Hazelnut', 'Caramel', 'Mocha   ', 'Butterscotch', 'Amerito', 'Maple   ', 'Cinnamon', 'Birthday Cake']
prices = [20, 30, 25, 15, 20, 35, 45, 40, 37]
print('FLAVOUR', 'PRICES($), excl Tax', sep='\t\t\t\t\t')
for i in range(len(flavours)):
    print(str(i + 1) + '.' + flavours[i], prices[i], sep='\t\t\t\t')
print("Please select your flavour from the list.")

#you will add some code here for selection and calculation of price
#lets show the payment methods
time.sleep(3)
payment_method = ["PayPal", "M-Pesa", "Cash"]
pay = input("please input your preferred payment method:\n")
choosen_payment = payment_method
while True:
    if choosen_payment in payment_method:
        if choosen_payment == "PayPal".lower():
            print("You have chosen PayPal as your payment method, please use PayPal ID \'muniirlechi@proton.me\' to make payments\n")
        elif choosen_payment == "M-Pesa".lower():
            print("You have chosen M-Pesa as your payment method, please use Till Number \'306892\' to make payments\n")
        else:
            print("You have chosen Cash as your payment method, please move to the counter to recieve your order and make payment. Thank you\n")
        time.sleep(2)
    else:
        print('You have entered the wrong payment method. please try again')
    
    break

       

print("Thank you ",name,"for Visiting Munisha\'s Coffee Point\n Welcome Again\n GoodBye\n")
