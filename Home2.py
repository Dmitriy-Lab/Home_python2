# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z

print("x | y | z | ¬(X ∧ Y) ∨ Z")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            sum = not(x and y) or z
            print(f"{x} | {y} | {z} | {int(sum)}")