# Это работа по «Программной инженерии»
# Студент: Леушкин Виталий Владимирович
# Группа: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №9. Веб-приложения с бибилиотекой streamlit
# Вариант 7: "Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass,
# указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."

import matplotlib.pyplot as pit
import streamlit as st


def get_avg(lines: [], sibsp: int):
    pclass_summ = {'1': 0, '2': 0, '3': 0}
    pclass_count = {'1': 0, '2': 0, '3': 0}
    for i, line in enumerate(lines):
        if i == 0:
            continue
        data = line.split(',')
        if data[6] != "" and int(data[7]) == sibsp:
            pclass_summ[data[2]] += float(data[6])
            pclass_count[data[2]] += 1
    return \
        [
           round(pclass_summ['1']/pclass_count['1'] if pclass_count['1'] > 0 else 0.0,2),
           round(pclass_summ['2']/pclass_count['2'] if pclass_count['2'] > 0 else 0.0,2),
           round(pclass_summ['3']/pclass_count['3'] if pclass_count['3'] > 0 else 0.0,2)
        ]


def get_AVG_age(sibsp: int):
    with open('data.csv') as file:
        lines = file.readlines()
    return get_avg(lines, sibsp)


st.image('titanic.jpg')
st.header('Данные пассажиров Титаника')
st.write('Для просмотра данных о среднем возрасте пассажиров по каждому классу обслуживания в соответствии с количеством братьев, сестер, сводных братьев, сводных сестер, супругов на борту,выберите соответствующий пункт из списка')

ss = st.number_input('Значение поля SibSp:', 0, 8, 0, 1)
avg_age = get_AVG_age(ss)
pclass = ['1 класс', '2 класс', '3 класс']

data = {'Класс обслуживания': pclass, 'Средний возраст': avg_age}
mt = st.table(data)

fig = pit.figure(figsize=(10, 5))
pit.bar(pclass, avg_age)
pit.xlabel('Значение поля Pclass')
pit.ylabel('Возраст (поле Age)')
pit.title('Средний возраст пассажиров по классам обслуживания')
st.pyplot(fig)