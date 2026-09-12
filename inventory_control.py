# Model with allowed shortages, instantaneous receipt, and gradual consumption.

import math
class InventoryControl:
    
    #calculating economic order quantity
    @staticmethod
    def calculate_EOQ(c , d , h , s):
        result = math.sqrt((2*c*d) / h) * math.sqrt((h+s) / s)
        return result
    
    
    #calculating Positive warehouse inventory level
    @staticmethod
    def calculate_q(s , h , EOQ : calculate_EOQ):
        result = (EOQ*s) / (h+s)
        return int(result)
    
    
    #calculating total order cost
    @staticmethod
    def calculate_TOC(c , d , EOQ : calculate_EOQ):
        result = c * (d/EOQ)
        return result
    
    
    #calculating total holding cost
    @staticmethod
    def calculate_THC(h , b , q : calculate_q , EOQ : calculate_EOQ):
        result = h * ((q**2) / (2*EOQ))
        return result
    
    
    #calculating total shortage cost
    @staticmethod
    def calculate_TSC(s , EOQ : calculate_EOQ , q : calculate_q):
        result = s * (((EOQ - q)**2) / (2*EOQ))
        return result
    
    
    #calculating total inventory cost
    @staticmethod
    def calculate_TIC(c , b , d , h , s , q : calculate_q , EOQ : calculate_EOQ):
        THC = InventoryControl.calculate_THC(h, b, q, EOQ)
        TOC = InventoryControl.calculate_TOC(c , d , EOQ)
        TSC = InventoryControl.calculate_TSC(s, EOQ, q)
        TIC = TOC + THC + TSC
        return TIC
    
    

    
    
    
    
    
    
