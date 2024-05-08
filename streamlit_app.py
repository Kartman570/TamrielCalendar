import streamlit as st
from datetime import datetime
from calendar_conversion.py import convert_to_tamriel_date

st.title('Конвертер дат в стиле Тамриэля')

# Поле ввода даты
input_date = st.date_input('Введите текущую дату', datetime.today())

# Кнопка для конвертации
if st.button('Конвертировать'):
    # Конвертация даты
    converted_date = convert_to_tamriel_date(input_date.year, input_date.month, input_date.day, input_date.weekday())
    # Вывод результата
    st.write(f"Дата в стиле Тамриэля: {converted_date}")
