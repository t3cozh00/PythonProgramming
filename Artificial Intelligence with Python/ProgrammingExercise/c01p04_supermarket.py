# 20241222

prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
total_sum = 0
print("Supermarket\n===========")

while True:
	product_number = int(input("Please select product (1-10) 0 to Quit:"))
	
	if product_number == 0:		
		break
	
	if 1<= product_number <= 10:
		price = prices[product_number - 1]
		total_sum += price
		print(f"Product: {product_number} Price: {price}")

print(f"Total: {total_sum}")

payment = float(input("Payment: "))
change = payment - total_sum
print(f"Change: {int(change)}")