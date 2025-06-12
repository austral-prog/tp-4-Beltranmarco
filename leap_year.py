def leap_year():
    year = int(input(""))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"el año {year} no es biciesto")
    else: 
        print(f"el año {year} no es biciesto")
