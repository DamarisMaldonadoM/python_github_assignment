print("ദ്ദി(ᵔᗜᵔ) Hi, welcome to my python program °‧ 𓆝 𓆟 𓆞 ·｡")
#This prints out a welcome message to the user.

quantity = input("How many cupcakes did you sell today? ")
#This opens up a box so user can iput the number of cupcakes sold.

try:
    quantity = float(quantity) #this converts the inputed amount which is a string into a float.
except ValueError:
    print("Please enter a valid number for the quantity of cupcakes sold.")
    exit()
#This helps remind users to input a valid number for the input with a message.
#This also goes after the input.

price = 3.50 #We want to know how much a single cupcake is
Total_sales = price * quantity #This calculates a total sale so it multiplys the price of $3.50  by the input in float form.

print(f"Your total sales for cupcake sales is ${Total_sales:.2f} today. 𓆝 𓆟 𓆞 ")
#This prints a messages saying the total sales is [blank] since each input could be different.

