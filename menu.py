# showing the menu
def show_menu():
    print("1>EOQ : calculate enonomic order quantity")
    print("2>THC : calculate total holding cost")
    print("3>TOC : calculate total order cost")
    print("4>TIC : calculate total inventory cost")
    print('5>TSC : calculate total shortage cost')
    print('6>q   : calculate Positive warehouse inventory level')
    print('0> exit')
    

#getting the correct menu from user
def get_menu(prompt):
    while True:
        menu = input(prompt)
        if not menu.isnumeric():
            print('you should enter number')
            continue
        return int(menu)


#getting the correct input in order to calculate in function
def get_input(prompt):
    while True:
        number = input(prompt)
        if number.isalpha():
            print('you should enter integer')
            continue
        return int(number)
    
    
    