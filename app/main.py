def get_human_age(cat_age: int, dog_age: int) -> list:
    """
    Convert cat and dog ages to human years.

    Rules:
    Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
    Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1

    Args:
        cat_age: Cat's age in cat years
        dog_age: Dog's age in dog years

    Returns:
        List with [cat_human_age, dog_human_age]

    Examples:
        get_human_age(0, 0) == [0, 0]
        get_human_age(15, 15) == [1, 1]
        get_human_age(24, 24) == [2, 2]
    """

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        raise TypeError("Ages must be integers")

    if cat_age < 0 or dog_age < 0:
        raise ValueError("Ages cannot be negative")

    result = [0, 0]

    for year in [15, 9, 4]:
        if year == 4:
            result[0] += cat_age // year
            break
        if cat_age - year >= 0:
            result[0] += 1
        else:
            break
        cat_age -= year

    for year in [15, 9, 5]:
        if year == 5:
            result[1] += dog_age // year
            break
        if dog_age - year >= 0:
            result[1] += 1
        else:
            break
        dog_age -= year

    return result
