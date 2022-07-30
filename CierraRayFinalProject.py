# INF360 - Programming in Python
# Cierra Ray
# Assignment Final



#Import Statements

try:
    from datetime import datetime
    import logging
except:
    logging.debug("You are missing your Import Modules.")
    
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s-  %(message)s')


#I used debug and criticle in the logging module
#You will find the criticle in places where if you try to load from a text file and the file does not exist.
#debug was used when there was just a simple error in a try/accept statement.
#logging.debug("Test This")
#logging.critical("Failue")






#Grocery Class where all programs functions are scored
class Grocery:
    def __init__(self, name, rating, time):
        self.name = name
        self.rating= rating
        self.time = time
    



# Function that prints the menu
    def menu(self):
        print('*'.center(100, '*'))
        print(' Your Grocery List '.center(100, '*'))
        print('*'.center(100, '*'))
        print(f'Hello {name}!')
        print("""\n\nWelcome to Your Grocery List APP\n
         Main menu

         Press a Number to Choose Your Option

         1. View Grocery List
         2. Add an Item
         3. Delete an Item
         4. Exit Program
                    \n\n\n""")

        
# Logoff message function
    def programexit(self, time):
         print(f'Goodby {name}! You exited the program at {time}')


#function that defines each item as it's input in by the user.
    def iteminput(self):
        stopname = True
        stopsize = True
        stopqty = True
        stopprice = True
        item = {}
        name = ''
        size = ''
        qty = ''
        price = ''

        while stopname:
            name = input("Enter the Item Name: ")
            if name.isalpha():
                stopname = False
        while stopsize:
            size = input("Enter the Item Size: ")
            if size.isdigit():
                stopsize = False
        while stopqty:
            qty = input("Enter the Item Quantity: ")
            if qty.isdigit():
                stopqty = False
        while stopprice:
            price = input("Enter the Item Price: ")
            if price.isdigit():
                stopprice = False

        item['name'] = name
        item['size'] = size
        item['qty'] = qty
        item['price'] = price

        return item

#Viewlist function reads in data from data.text and allows the user to see what's in the
#Grocery list.
    def viewlist(self):
        try:
            empty = open("data.txt", "r")
            checkempty = empty.read()
            empty.close()
            if len(checkempty) == 0:
                print("""
                You currently have no items in your grocery list. Please
                Add New Items by pressing 2 on the main menu!
                
                Press Enter/Return to return to the Main Menu!
                """)
                input()
            view = open("data.txt", "r")
            z = 1
            
            for i in view.readlines():
                print(z, i)
                z += 1
            view.close()
        except:
            logging.critical("This is going to crash your app")




#funtion that writes the data to the list
    def addlist(self):
        newlist = [self.iteminput()]
        add = open("data.txt", "a")
        add.writelines(str(newlist))
        add.write("\n")
        add.close()

        print(newlist)

#removeitem is the function that deletes items from the list. 
    def removeitem(self):
        print("please press the number of the item you would like to remove \n\n")
        self.viewlist()
        find = open("data.txt", 'r')
        dellist = find.readlines()
        choice = int(input()) - 1
        dellist.remove(dellist[choice])
        remove = open("data.txt", 'w')
        for i in dellist:
            remove.writelines(i)

        remove.close()


# Main Program
currentTime = datetime.now()
control = -1
name = input("What is your Name? ")
rating = input("Rate This App From 1-5 ")
user = Grocery(name, rating,currentTime)
while control != 4:
    Grocery.menu(user)
    control = input()
    try:
        if not control.isalpha():
            if not int(control) >= 5 or int(control) <= 0:
                if int(control) == 1:
                    Grocery.viewlist(user)
                if int(control) == 2:
                    Grocery.addlist(user)
                if int(control) == 3:
                    Grocery.removeitem(user)
                if int(control) == 4:
                    user.programexit(currentTime)
                    control = 4
                    print(control)
            else:
                print(" Please enter a number between 1-4 Only ")
        else:
            print(" Please enter a number between 1-4 Only ")

    except:
        logging.debug("Nice Try but You can't Press That Key")

