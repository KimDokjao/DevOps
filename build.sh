#!/bin/bash

# Установка зависимостей
pip install -r requirements.txt

# Запуск тестов
pytest

# Проверка форматирования кода
flake8 app.py test_app.py