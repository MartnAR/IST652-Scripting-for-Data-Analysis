# Create the stock and prices dictionaries
stock = {"banana":6,"apple":0,"orange":32,"pear":15}
prices = {"banana":4,"apple":2,"orange":1.5,"pear":3}

# 1. Show the expression that gets the value of the stock dictionary at the key "orange". Add another item to the dictionary ("cherry", 14)
stock["orange"]
stock["cherry"] = 14

# 2. Write the code for a loop that iterates over the stock dictionary and prints each key and value.
for k, v in stock.items():
    print(k, v) 
