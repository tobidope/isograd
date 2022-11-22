def safe_area(lines):
    width_city, width_danger = [int(i) for i in lines]
    return width_city ** 2 - width_danger ** 2
