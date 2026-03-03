def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    message = seed_type.capitalize() + " seeds: "
    if unit == "packets":
        message += "{} packets avaliable"
    elif unit == "grams":
        message += "{} grams total"
    elif unit == "area":
        message += "covers {} square meters"
    else:
        message += "Unknown unit type"
    print(message.format(quantity))
