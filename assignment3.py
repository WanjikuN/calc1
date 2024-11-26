#BDD
#Input
# 200,50%
# 200, 10%
#Output
# 100
# 200
#Behaviour
# takes in price and discount and returns the final price
# If the discount is 20% or higher, apply the discount;
# Otherwise, return the original price

#Pseudo Code
# Create a fxn calculate_discount(price, discount)
# Conditionally render the discount
# If the discount is >= 20%, apply it
# If the discount <20%, return the original price
def calculate_discount(price, discount='0'):
  try:
        new_discount = int(discount.strip('%'))
  except ValueError:
        return price
  if new_discount >= 20:
    return price - (price * new_discount // 100)
  else:
    return price

# print(calculate_discount(200, '50%'))
# print(calculate_discount(200, '10%'))
# User Prompt1
price = input('Enter the Price:')
discount = input('Enter the Discount:')

print(calculate_discount(int(price), discount))
