import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# строим графики y = x^2, y = x^3 на заданном диапазоне значений Х
# start - начало диапазона, end - конец, step - шаг изменения значений
# возвращает обхект Figure с построенными графиками или ошибка, если введены некорректные параметры диапазона 

def plot_functions(start: float, end: float, step: float) -> plt.Figure: 
    #шаг должен быть положительным, а начало -меньше конца
    if step <= 0:
        raise ValueError('Шаг должен быть положительным.')

    if start >= end:
        raise ValueError('Начало диапазона должно быть меньше конца.')

    # создаем массив значений X
    x = np.arange(start, end + step / 10, step)

    # вычисляем значения функций для каждой точки массива Х
    y1 = x ** 2
    y2 = x ** 3

    # создаем фигуру размером 8 на 5 дюймов
    fig, ax = plt.subplots(figsize=(8, 5))

    # строим график функции y = x^2, где синий пунктир, круглые маркеры
    ax.plot(x, y1, color='blue', linestyle='--', marker='o', label='y = x^2')

    # строим график функции y = x^3, где красная сплошная линия и квадратные маркеры
    ax.plot(x, y2, color='red', linestyle='-', marker='s', label='y = x^3')

    # добавляем заголовок и подписи осей, сетку, легенду
    ax.set_title('Графики функций y = x^2 и y = x^3')
    ax.set_xlabel('Значения X')
    ax.set_ylabel('Значения Y')

    # Включаем сетку и добавляем легенду
    ax.grid(True)
    ax.legend(loc='upper left')

    return fig

def main() -> None:
    # настраиваем страницу
    st.set_page_config(page_title='Графики функций', layout='centered')

    # добавляем заголовок
    st.title('Графики функций')

    # добавляем поля для ввода параметров
    st.sidebar.header('Параметры диапазона')

    # пользователь вводит начало и конец диапазона, а также шаг изменения значения Х
    start = st.sidebar.number_input('Начало диапазона', value=-3.0, step=0.5) # начало диапазона
    end = st.sidebar.number_input('Конец диапазона', value=3.0, step=0.5) # конец диапазона
    step = st.sidebar.number_input('Шаг', value=0.5, step=0.1) # шаг

    # создаем кнопку построения графика
    if st.sidebar.button('Построить график'):
        try:
            fig = plot_functions(start, end, step)
            st.pyplot(fig)
    # если параметры некорректны, выводит сообщение об ошибке
        except ValueError as e: 
            st.error(f'Ошибка ввода: {e}')

if __name__ == '__main__':
    main()

