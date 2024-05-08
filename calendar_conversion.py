from tamriel_data import tamriel_months, tamriel_weekdays, eras

def convert_to_tamriel_date(year, month, day, weekday):
    # Определение эры и года в этой эре
    for era in eras:
        if year >= era["start"]:
            tamriel_year = year - era["start"] + 1  # Год в эре
            tamriel_era = era["name"]
            break
    else:
        tamriel_year = year  # Если дата до первой эры, используем текущий год
        tamriel_era = "доисторическая эра"

    # Получение названия месяца
    tamriel_month = tamriel_months.get(month, "Unknown Month")

    # Получение названия дня недели
    tamriel_weekday = tamriel_weekdays.get(weekday, "Unknown Day")

    # Формирование тамриэльской даты
    return f"{tamriel_weekday}, {day}-го {tamriel_month}, {tamriel_year}-й год {tamriel_era}"
