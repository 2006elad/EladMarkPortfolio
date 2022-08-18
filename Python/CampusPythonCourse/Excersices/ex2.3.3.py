num = int(input("Please insert the total of breaks that pigs Collect: "))
total_breaks = num % 10
num = int(num / 10)
total_breaks += num % 10
total_breaks += int(num/10)
print("sum of breaks is:", total_breaks)
print("when we divide between them with same quantity", int(total_breaks/3))
print("module is: ", total_breaks % 3)
print((total_breaks % 3) == 0)


