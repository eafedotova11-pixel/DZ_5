import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_functions(start: float, end: float, step: float) -> plt.Figure:
    # Проверяем корректность введённых значений
    if step <= 0:
        raise ValueError('Шаг должен быть положительным.')

    if start >= end:
        raise ValueError('Начало диапазона должно быть меньше конца.')

    # Создаём массив значений X
    x = np.arange(start, end + step / 10, step)

    # Рассчитываем значения функций
    y1 = x ** 2
    y2 = x ** 3

    # Создаём фигуру размером 8 на 5 дюймов
    fig, ax = plt.subplots(figsize=(8, 5))

    # Строим график функции y = x^2
    ax.plot(x, y1, color='blue', linestyle='--', marker='o', label='y = x^2')

    # Строим график функции y = x^3
    ax.plot(x, y2, color='red', linestyle='-', marker='s', label='y = x^3')

    # Добавляем заголовок и подписи осей
    ax.set_title('Графики функций y = x^2 и y = x^3')
    ax.set_xlabel('Значения X')
    ax.set_ylabel('Значения Y')

    # Включаем сетку и добавляем легенду
    ax.grid(True)
    ax.legend(loc='upper left')

    return fig

def main() -> None:
    # Настраиваем страницу
    st.set_page_config(page_title='Графики функций', layout='centered')

    # Добавляем заголовок
    st.title('Графики функций')

    # Добавляем поля для ввода параметров
    st.sidebar.header('Параметры диапазона')

    start = st.sidebar.number_input('Начало диапазона', value=-3.0, step=0.5)
    end = st.sidebar.number_input('Конец диапазона', value=3.0, step=0.5)
    step = st.sidebar.number_input('Шаг', value=0.5, step=0.1)

    # Создаём кнопку построения графика
    if st.sidebar.button('Построить график'):
        try:
            fig = plot_functions(start, end, step)
            st.pyplot(fig)

        except ValueError as e:
            st.error(f'Ошибка ввода: {e}')

if __name__ == '__main__':
    main()

