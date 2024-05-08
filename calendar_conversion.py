from tamriel_data import tamriel_months, tamriel_weekdays, eras


def convert_to_tamriel_date(year, month, day, weekday):
    for era in eras:
        if year >= era["start"]:
            tamriel_year = year - era["start"] + 1
            tamriel_era = era["name"]
            break
    else:
        tamriel_year = year
        tamriel_era = "Долетописной эры"

    tamriel_month = tamriel_months.get(month, "Unknown Month")
    tamriel_weekday = tamriel_weekdays.get(weekday, "Unknown Day")

    return f"{tamriel_weekday}. {day} {tamriel_month}. {tamriel_year} год {tamriel_era}"
