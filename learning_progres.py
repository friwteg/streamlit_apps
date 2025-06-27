import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Страничка отслеживания прогресса обучения friwteg')
df = pd.read_csv('report.csv')
df.drop('project', axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df['task'] = df['task'].fillna('Другое')

task_progress = df.groupby(['date', 'task'])['minutes'].sum().unstack(fill_value=0)

# Создание графика
fig, ax = plt.subplots()

# Накопленные столбцы
bottom = np.zeros(len(task_progress.index))

for task in task_progress.columns:
    ax.bar(task_progress.index, task_progress[task], bottom=bottom, label=task)
    bottom += task_progress[task]

# Настройка графика
ax.set_title("Накопленный прогресс по задачам")
ax.set_xlabel("Дата")
ax.set_ylabel("Количество минут")
ax.legend(title="Задача", loc="upper left", bbox_to_anchor=(1, 1))  # Вынесение легенды за пределы графика

# Поворот подписей к оси X
plt.xticks(rotation=15)
st.pyplot(fig)


# для каждого дня сделать какую то доп визуализацию