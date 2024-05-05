# Это работа по «Программной инженерии»
# Студент: Леушкин Виталий Владимирович
# Группа: 2023-ФГиИБ-ПИ-1см
# Практическое занятие №9. Веб-приложения с бибилиотекой streamlit
# Вариант 7: "Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass,
# указав количество братьев, сестер... (столбец SibSp): [0, …, 8]."

import matplotlib.pyplot as pit
import streamlit as st

def f_ds_init():
    return {
                'PassengerId': [],
                'Survived': [],
                'Pclass': [],
                'Name': [],
                'Sex': [],
                'Age': [],
                'SibSp': [],
                'Parch': [],
                'Ticket': [],
                'Fare': [],
                'Cabin': [],
                'Embarked': []
            }


def f_ds_copy(ds_src: {}, ds_dst: {}, counts: int):
    ds_dst['PassengerId'].append(ds_src['PassengerId'][counts])
    ds_dst['Survived'].append(ds_src['Survived'][counts])
    ds_dst['Pclass'].append(ds_src['Pclass'][counts])
    ds_dst['Name'].append(ds_src['Name'][counts])
    ds_dst['Sex'].append(ds_src['Sex'][counts])
    ds_dst['Age'].append(ds_src['Age'][counts])
    ds_dst['SibSp'].append(ds_src['SibSp'][counts])
    ds_dst['Parch'].append(ds_src['Parch'][counts])
    ds_dst['Ticket'].append(ds_src['Ticket'][counts])
    ds_dst['Fare'].append(ds_src['Fare'][counts])
    ds_dst['Cabin'].append(ds_src['Cabin'][counts])
    ds_dst['Embarked'].append(ds_src['Embarked'][counts])
    return ds_dst


def f_ds_append(ds_dst: {},
                v_passengerid: int,
                v_survived: bool,
                v_pclass: int,
                v_name: str,
                v_sex: str,
                v_age: float,
                v_sibsp: int,
                v_parch: int,
                v_ticket: str,
                v_fare: float,
                v_cabin: str,
                v_embarked: str
                ):
    ds_dst['PassengerId'].append(v_passengerid)
    ds_dst['Survived'].append(v_survived)
    ds_dst['Pclass'].append(v_pclass)
    ds_dst['Name'].append(v_name)
    ds_dst['Sex'].append(v_sex)
    ds_dst['Age'].append(v_age)
    ds_dst['SibSp'].append(v_sibsp)
    ds_dst['Parch'].append(v_parch)
    ds_dst['Ticket'].append(v_ticket)
    ds_dst['Fare'].append(v_fare)
    ds_dst['Cabin'].append(v_cabin)
    ds_dst['Embarked'].append(v_embarked)
    return ds_dst


def f_get_dataset(filename: str):
    v_ds_fgd = f_ds_init()
    with open(filename) as file:
        v_counts = 0
        for line in file:
            if v_counts > 0:
                data = line.split(',')
                f_ds_append(v_ds_fgd,
                            int(data[0]),
                            False if data[1] == 0 else True,
                            int(data[2]),
                            f'{data[3][1:]}, {data[4][:-1]}',
                            data[5],
                            0 if data[6] == '' else float(data[6]),
                            int(data[7]),
                            int(data[8]),
                            data[9],
                            float(data[10]),
                            data[11],
                            data[12]
                            )
            v_counts += 1
    return v_ds_fgd


def f_get_pclass_filtered(ds_src: {}, pclass: str):
    v_ds_fgpf = f_ds_init()
    v_counts = 0
    for data in ds_src['Pclass']:
        if data == pclass:
            f_ds_copy(ds_src, v_ds_fgpf, v_counts)
        v_counts += 1
    return v_ds_fgpf

def f_get_sibsp_filtered(ds_src: {}, ss: int):
    v_ds_fgpf = f_ds_init()
    v_counts = 0
    for data in ds_src['SibSp']:
        if data == ss:
            f_ds_copy(ds_src, v_ds_fgpf, v_counts)
        v_counts += 1
    return v_ds_fgpf

def f_get_age_normalized(ds_src: {}):
    v_ds_fgaf = f_ds_init()
    v_counts = 0
    for data in ds_src['Age']:
        if data != 0:
            f_ds_copy(ds_src, v_ds_fgaf, v_counts)
        v_counts += 1
    return v_ds_fgaf


def f_get_max_min_avg(ds_src: {}, pclass: str, ss: int):
    ds = f_get_pclass_filtered(ds_src, pclass)
    ds = f_get_sibsp_filtered(ds, ss)
    d = f_get_age_normalized(ds)
    s = sum(d['Age'])
    l= len(d['Age'])
    if l > 0:
        v_avg = s / l
    else:
        v_avg = 0
    return v_avg


def get_AVG_age(ss: int):
    v_ds = f_get_dataset('data.csv')
    v_class = list(set(v_ds['Pclass']))
    v_class.sort()
    avg = []
    for c in v_class:
        avg.append(f_get_max_min_avg(v_ds, c, ss))
    return avg



st.image('titanic.jpg')
st.header('Данные пассажиров Титаника')
st.write('Для просмотра данных о среднем возрасте пассажиров по каждому классу пассажиров в соответствии с количеством братьев, сестер, сводных братьев, сводных сестер, супругов на борту,выберите соответствующий пункт из списка')

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