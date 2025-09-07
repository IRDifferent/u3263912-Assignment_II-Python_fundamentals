#Stephen James | u3263912 | 07/09/2025 | Cafe POS System

#Allows for the time.sleep() function for the card payment system to simulate waiting for the payment processing
import time

#Dictionary menu list
menu_list = {
    "Bacon & Egg roll" : 8.50,
    "Avocado & Toast" : 10.00,
    "Scrambled Eggs & Toast" : 7.00,
    "Blueberry Muffin" : 5.00,
    "Full English Breakfast" : 16.00,
    "Banana Bread" : 7.50,
    "Flat White" : 6.00,
    "Cappucino" : 6.00,
    "Latte" : 6.00,
    "Long Black" : 4.50,
    "Iced Latte" : 7.50,
    "Milkshake" : 7.50
}

items_ordered = [] #(item, price)
#Tracks the total price of the cart
total_price = 0
#Only used to calculate the student discount, it it applies
student_discount = 0

#Prints the menu when the function starts
print("Menu:")
for key, value in menu_list.items(): #Loop to just print the items and values in the format I want it to be in, rather than the default mess
    print(f"{key} | ${value:.2f}")
print("\n")
print("Please type ""Cart"" to view your cart.\n")

#Runs the food order system - Allows items to be added to the items_ordered list, and adds the price to the total_price value
def food_order():
    while True:
        order = input("What would you like to order today? ")
        if order == "Done":
            break
        elif order in menu_list:
            global total_price
            total_price += menu_list[order] #Adds price of item to the total_price value
            global items_ordered
            items_ordered += [order] #Adds the item to the items_ordered list
            print(f"${total_price:.2f}") #Running total of the price
            print("Item added") #Confirmation item was added so the user knows they can continue
        elif order == "Cart": #Allows the user to pull the current cart
            for item in set(items_ordered): #Same as used in the receipt to show the number of each item and the cost
                item_quant = items_ordered.count(item)
                item_price = menu_list.get(item, 0) * item_quant  
                print(f"{item_quant} x {item} ${item_price:.2f}")
        else:
            print("Sorry, that item isn't on the menu")

#Runs the payment system - Allows users to choose cash or card
def payment():
    while True:
        payment_method = input("Would you like to pay with Cash or Card today? ")
        if payment_method == "Cash":
            cash_amount = input("How much cash was handed over? ")
            cash_change = float(cash_amount) - float(total_price) #Calculates how much change is due
            print(f"Your change is ${cash_change:.2f}. Thanks for coming and enjoy your day!")
            break
        if payment_method == "Card":
            print("Please direct your attention to the eftpos machine for payment.")
            time.sleep(10)
            payment_accepted = input("Payment accepted (Y/N)? ")
            if payment_accepted == "Y":
                print("Thanks for coming, enjoy your day!")
                break
            if payment_accepted == "N": #Returns to payment if payment unsuccessful to be re-attempted
                print("Payment Declined, please try again")
                return payment()

def receipt_printout():
    value_food_menu = menu_list[items_ordered[0]]
    print(f"{len(items_ordered)} items ordered:") #counts the items in the cart
    for item in set(items_ordered): #Separates the list of items into quantities of each item
        item_quant = items_ordered.count(item)
        item_price = menu_list.get(item, 0) * item_quant  
        print(f"{item_quant} x {item} ${item_price:.2f}")
    if student_discount >0: #Shows the student discount on the receipt if the discount is greater than 0
        print(f"Discounts: ${student_discount}")
    print(f"Subtotal: ${total_price:.2f}")
    print(f"GST Incl: ${(total_price * 10 / 100):.2f}")
          

food_order()

print(f"Subtotal: ${total_price:.2f}")
print(f"GST Incl: ${(total_price * 5 / 100):.2f}")
student_status = input("\nAre you a student(Y/N)? ")#Student discount decision point
if student_status == "Y":
    student_discount = total_price * 5 / 100 #Adds the student discount to the student_discount value if it applies
    total_price = total_price - total_price * 5 / 100
    print(f"You have recevied a discount of ${student_discount:.2f}")
    print(f"Your new total comes to ${total_price:.2f}")
    print(f"GST Included in transaction ${(total_price * 10 / 100):.2f}")
    payment()
else:
    payment()


receipt_printout()

