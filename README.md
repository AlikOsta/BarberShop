# Барбершоп "Под Горшок"

Современный веб-сайт для барбершопа с системой онлайн-записи и управления клиентами.

## Основные возможности

- Онлайн-запись к мастерам
- Каталог услуг с ценами
- Профили мастеров с портфолио
- Система отзывов клиентов
- Административная панель для управления записями
- Интеграция с Telegram для уведомлений

## Технологии

- Python 3.11
- Django 5.0
- Bootstrap 5
- SQLite3
- python-telegram-bot

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/YourUsername/BarberShop.git
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Загрузите тестовые данные:
```bash
python manage.py loaddata fixtures/initial_data.json
```

6. Запустите сервер:
```bash
python manage.py runserver
```

## Структура проекта

```
BarberShop/
├── app/                    # Основное приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # Представления
│   ├── forms.py           # Формы
│   └── templates/         # Шаблоны
├── static/                # Статические файлы
├── media/                 # Загружаемые файлы
└── fixtures/              # Тестовые данные
```

## Разработка

- Для добавления новых функций создавайте отдельную ветку
- Следуйте PEP 8
- Пишите тесты для нового функционала

## Лицензия

MIT License

## Контакты

По всем вопросам обращайтесь: example@email.com
