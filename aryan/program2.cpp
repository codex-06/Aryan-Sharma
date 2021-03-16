houses = [range(1, 10**9+1)]
position = 1
address = (input("house number for deliveries").split(" "))
address = list(map(int, address))
address.sort()
print(address)
skips = []
for house in address:
    house = int(house)
    skip = house - position
    skips.append(skip)
    position = house
print(f"the skip sequence is {skips}")


