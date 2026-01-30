'''
Docstring for Week03.Q2

Question 2: Shopping Cart (Lists - Searching and Removal)
Concepts: index(), count(), remove(), pop(), in keyword

Create a shopping cart program
'''

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
num_apples = cart.count("apple")
milk_position = cart.index("milk")
cart.remove("apple")
removed_item = cart.pop()
banana_in_cart = "banana" in cart   

print(f"Number of apples: {num_apples}")
print(f"Position of milk: {milk_position}")
print(f"Removed item using pop: {removed_item}")
print(f"Is banana in cart? {banana_in_cart}")
print(f"Final cart: {cart}")