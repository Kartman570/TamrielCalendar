import streamlit as st
from datetime import datetime, date, timedelta
from calendar_conversion import convert_to_tamriel_date

st.title('Григорианско-Тамриэльский переводчик дат')
min_date = date(1, 1, 1)

input_date = st.date_input('Введите текущую дату', value=datetime.today(), min_value=min_date)

converted_date = convert_to_tamriel_date(input_date.year, input_date.month, input_date.day, input_date.weekday())
st.write(f"Дата по Тамриэльскому календарю: ")
st.title(converted_date)
