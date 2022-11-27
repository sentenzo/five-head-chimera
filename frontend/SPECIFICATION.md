This document contains  detailed description of the **frontend** service as a part of the **User Feedback Processing System**. 

To read more about the system as a haul, see: `SPECIFICATION.md`.

# Frontend

Страница приема обращения гражданина, обязательные элементы:
- поле Фамилия (тип текст)
- поле Имя (тип текст)
- поле Отчество (тип текст)
- поле Телефон (тип телефон, для упрощения цифры)
- поле Обращение (тип большой текст)
- кнопка "Отправить" (инициализируется отправку данных на бэкенд)
Реализация: html, js(jQuery) или что-то максимально простое, формирование json(или другого представления данных)
и отправдка на бэкенд.