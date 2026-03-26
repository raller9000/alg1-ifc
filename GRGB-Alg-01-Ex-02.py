total = int(input("Digite uma quantia de segundos \n"))

days, remainder = divmod(total, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{days}d/{hours}h/{minutes}m/{seconds}s \n")