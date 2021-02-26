initial_quantity = int(input())  # 4
final_quantity = int(input())  # 3
half_life = 0

while initial_quantity > final_quantity:
    initial_quantity = initial_quantity // 2
    half_life += 1
    pass

life = 12 * half_life
print(life)

