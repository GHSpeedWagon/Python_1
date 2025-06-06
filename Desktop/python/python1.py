a = int(input("Введіть ціле число a: "))
b = float(input("Введіть дробове число b: "))
c = int(input("Введіть ціле число c: "))
d = float(input("Введіть дробове число d: "))

results = []
results.append(a + b)         
results.append(c - d)         
results.append(a * c)         
results.append(d / b)        
results.append(a ** 2)       
results.append(c // a)         
results.append(int(b) % a)  

print("\nКількість елементів у списку:", len(results))
print("Парні елементи списку:")
for item in results:
    if isinstance(item, int) and item % 2 == 0:
        print(item)

results[1], results[4] = results[4], results[1]
print("\nСписок після обміну 2-го і 5-го елементів:")
print(results)

name = input("\nВведіть ваше прізвище та ім’я: ")
print("\nВиконавець лабораторної роботи:")
print(name)
print("У ході роботи було виконано:")
print("- Введення чисел з клавіатури")
print("- Арифметичні операції над змінними")
print("- Робота зі списками")
print("- Вивід парних елементів та зміна списку")