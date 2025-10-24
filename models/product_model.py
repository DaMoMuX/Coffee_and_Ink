from datetime import datetime 

class product:
    
    def __init__(self, id, barcode, name, brand, cost, price, stock, area, expiration_date, created_at):
        self.id = id
        self.barcode = barcode
        self.name = name
        self.brand = brand
        self.cost = cost
        self.price = price
        self.profit = price - cost
        self.stock = stock
        self.area = area
        self.expiration_date = expiration_date
        self.created_at = created_at or datetime.now()



