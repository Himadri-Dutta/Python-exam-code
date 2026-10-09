'''
Online Mobile Store An online store maintains a list of mobile prices.
Write a function to display all mobiles costing more than ₹20,000,
calculate the total inventory value, and find the most expensive mobile price.
  
 '''


def mobile_store(mob:list):
    print("Mobiles costing more than ₹20,000:")
    for price in mob:
        if price > 20000:
            print(price)
    total_value = sum(mob)
    most_expensive = max(mob)
    print(f"Total inventory value: ₹{total_value}")
    print(f"Most expensive mobile price: ₹{most_expensive}")

mobile_store([10000,20000,30000,40000,22000])