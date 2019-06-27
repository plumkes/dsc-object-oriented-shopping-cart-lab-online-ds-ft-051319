import numpy as np
class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
      self.total = total
      self.employee_discount = employee_discount
      self.items = items
    def add_item(self, name, price, quantity=1):
       self.name = name
       self.price = price
       self.quantity = quantity
       if quantity == 1:
          self.items.append({'name':name, 'price':price})
       else:
          for x in range(quantity):
            self.items.append({'name':name, 'price':price})
       subtotal =  price * quantity
       self.total += subtotal
       return self.total
    def mean_item_price(self):
       no_items = len(self.items)
       total = sum([i['price'] for i in self.items])
       return total/no_items

    def median_item_price(self):
       ordered = (sorted([i['price'] for i in self.items]))
       if len(ordered) %2 != 0:
          odd =  len(ordered) // 2
          return ordered[odd]
       else:
          even1 = ((len(ordered)/2) + 1)
          even2 = ((len(ordered)/2) - 1)
          return (ordered[even1]+ordered[even2]) / 2

    def apply_discount(self):
       if self.employee_discount != None:
          return self.employee_discount


    def void_last_item(self):
       if len(self.items) != 0:
         price_to_remove = self.items[-1]['price']
         self.items.pop(-1)
         self.total = self.total - price_to_remove
       else:
          return "There are no items in your cart!"
       