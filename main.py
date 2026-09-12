from inventory_control import InventoryControl
from menu import show_menu , get_menu , get_input


c = get_input('enter order cost :')
d = get_input('enter consumption rate :')
h = get_input('enter holding cost :')
b = get_input('enter safety stock level :')
s = get_input('enter Cost unit associated with shortage :')
while True:
    show_menu()
    number = get_menu('enter either 1 or 2 or 3 or 4 or 0 :')
    match number:
        case 1:
            EOQ = InventoryControl.calculate_EOQ(c, d, h, s)
            print("{0} : {1}".format('economic order quantity' , EOQ))
        case 2:
            THC = InventoryControl.calculate_THC(h, b, InventoryControl.calculate_q(s, h, InventoryControl.calculate_EOQ(c, d, h, s)) , InventoryControl.calculate_EOQ(c, d, h , s))
            print("{0} : {1}".format('total holding cost' , THC))
        case 3:
            TOC = InventoryControl.calculate_TOC(c, d, InventoryControl.calculate_EOQ(c, d, h, s))
            print("{0} : {1}".format('total order cost' , TOC))                                                                                                     
        case 4:
            TIC = InventoryControl.calculate_TIC(c, b, d, h, s, InventoryControl.calculate_EOQ(c, d, h , s) , InventoryControl.calculate_q(s, h, InventoryControl.calculate_EOQ(c, d, h, s)))
            print("{0} : {1}".format('total inventory cost' , TIC))
        case 0:
            break
        case 5:
            TSC = InventoryControl.calculate_TSC(s, InventoryControl.calculate_EOQ(c, d, h, s), InventoryControl.calculate_q(s, h, InventoryControl.calculate_EOQ(c, d, h, s)))
            print("{0} : {1}".format('total shortage cost' , TSC))
        case 6:
            q = InventoryControl.calculate_q(s, h, InventoryControl.calculate_EOQ(c, d, h, s))
            print("{0} : {1}".format('Positive warehouse inventory level' , q))
        case _:
            print('invalid number!')
















































