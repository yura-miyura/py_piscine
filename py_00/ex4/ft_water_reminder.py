def ft_water_reminder():
    days_ago = int(input("Days since last watering: "))
    if days_ago > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
