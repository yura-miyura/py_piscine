def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    message = "Plant "
    if age > 60:
        message += "is ready to harvest!"
    else:
        message += "needs more time to grow."
    print(message)
