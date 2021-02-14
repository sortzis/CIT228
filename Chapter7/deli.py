sandwich_orders = ["Italian","Reuben","Club","Veggie","Turkey","BLT"]
finished_sandwiches = []
counter = 0
print("Sandwiches Ordered:")
for sammy in sandwich_orders:
    print(sammy)
print("We are out of Italian")
while "Italian" in sandwich_orders:
    sandwich_orders.remove("Italian")
print("New Sandwich Orders:")
for sammy in sandwich_orders:
    print(sammy)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("Sandwiches made: ")
for sammy in finished_sandwiches:
    print(sammy)