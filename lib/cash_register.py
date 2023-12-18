#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount / 100)
        return float(discounted_price)  


if __name__ == "__main__":
    
    product_instance = Product(price=100, discount=20)

    
    discounted_price = product_instance.apply_discount()
    print(f"Discounted Price: {discounted_price}")

  
