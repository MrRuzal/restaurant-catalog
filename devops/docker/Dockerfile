# Используем Python 3.12 в качестве базового образа
FROM python:3.12-slim AS builder

# Устанавливаем системные зависимости
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем всю директорию requirements/
COPY requirements/ /app/requirements/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /app/requirements/dev.txt

# Финальный образ
FROM python:3.12-slim
WORKDIR /app

# Копируем зависимости из builder-образа
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12

# Копируем весь исходный код приложения
COPY . /app

# Копируем .env файл
COPY .env /app/.env

# Открываем порт
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]