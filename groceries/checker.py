items = ["mlik", "bread", "eggs", "chips", "bacon"]

prices = [2.5, 3, 2.72, 1.5, 5]

def print_groceriy_list():
    for i in range(len(items)):
        print(f"{items[i]} - {prices[i]}")
        return i


print_groceriy_list()

def total_cost():
    cost = sum(prices)
    print(f"Total Cost: {cost}")

total_cost()

def most_expensive_item():
    for x in range(len(items)):
        expensive = max(prices)
        idn = prices.index(expensive)
        
        if (x == idn):
            print(f"Most Expensive Item: {items[x]}: ${expensive}")
 


most_expensive_item()


def feedback():
    for x in prices:
        if (x < 3):
            print("Great Deal!")
        elif (x >= 3 and x <= 5):
            print("Reasonable Price")
        else:
            print("Too Expensive")

    


#f = feedback() return x

def Display_Results():
 
    print(f"Grocery List: {items}")
    print(f"Total Cost: {total_cost()}")
    print(f"Most Expensive Item: {most_expensive_item()}")
    print(f"Price Feedback: {feedback()}")

Display_Results()