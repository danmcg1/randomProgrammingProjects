width: float = float(input("What is the width?: "))
length: float = float(input("What is the length?: ")) 

cost: float = float(input("How much does the material cost?: "))

area = width*length
total_cost = area * cost

print (f"{total_cost:.2f}")