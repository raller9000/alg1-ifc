#c to f

celsius = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = []
i = 0

print(f"Celsius\tFahrenheit")

while i < len(celsius):
    f = (celsius[i] * 9/5) + 32
    fahrenheit.append(f)
    i += 1

for i in range(len(celsius)):
    print(f"{celsius[i]}\t{fahrenheit[i]}")