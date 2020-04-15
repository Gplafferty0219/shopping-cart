#shopping.py
from pprint import pprint
import datetime

tax = 0.0875

#setting a formatting variable
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

if __name__ == "__main__":

    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

    #inputs
    total_price = 0 
    selected_ids = [] #empty list user will be adding to
    ids= ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"] #to make it easier to validate id's

    #a little welcome message
    print("~~~~~~~Welcome to Groceries R Us~~~~~~~")
    print("When you are ready, proceed below!")
    print()

    #loop the input message and add each input to my empty list
    while True: 
        selected_id = input("Please enter a product identifier, or type 'DONE' if there are no more items: ")
        if selected_id == "DONE":
            #little something special I added... makes user confirm their list before checking out!
            print("Your List: ")
            for selected_id in selected_ids:
                matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
                matching_product = matching_products[0]
                print("   " + matching_product["name"])            
            list_validation = input("Confirmation: Are you finished? (y/n): ")
            if list_validation == "n":
                print("ADD YOUR REMAINING ITEMS!")
            elif list_validation == "y":
                break
            else:
                print("INVALID RESPONSE: PLEASE ONLY ENTER 'y' or 'n'")
                print("Type 'DONE' to proceed")
        #will add to my empty list as long as a valid input is detected
        elif selected_id in ids:
            selected_ids.append(selected_id)
        else:
            print("Please enter a valid product identifier!")


    #reciept starts here
    #store info here
    print("------------------------------------------")
    print("              Groceries R Us              ")
    print("        phone number: 215-485-1218        ")
    print("           wwww.GroceriesRUs.com          ")
    print("------------------------------------------")

    #date and time are here
    today = datetime.datetime.today()
    print("               Checkout at:               ")
    print("          ", today.strftime("%Y-%m-%d %I:%M %p"), "          ")

    print("------------------------------------------")

    #shopping cart items here (the output of your code)
    print("Selected Products:")
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        total_price = total_price + matching_product["price"]
        print("- " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

    print("------------------------------------------")


    #subtotal, sales tax, final total
    sales_tax = total_price * tax
    total = total_price + sales_tax

    #print total
    print("SUBTOTAL: " + to_usd(total_price))
    print("TAX: " + to_usd(sales_tax))
    print(" ")
    print("TOTAL: " + to_usd(total))
    print("------------------------------------------")

    # thank you message
    print("Thanks for shopping with us! Enjoy your food and stuff!")


