deposit = int(input())
year = 0
while deposit <= 700000:
    deposit = deposit + (deposit * 71) / 1000
    year = year + 1
print(year)
