from email.mime import text

raw = input("Digite o horario no formato (dia/hora/minuto/segundo) \n")
day, hour, minute, second = raw.split("/")

day = int(day)
hour = int(hour)
minute = int(minute)
second = int(second)

total = (day * 24 * 3600) + (hour * 3600) + (minute * 60) + second
print("Total de segundos: ", total, "segundos")