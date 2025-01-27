# Используем официальный образ Python
FROM python:3.12-slim-buster

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы, необходимые Poetry для установки зависимостей
COPY poetry.lock pyproject.toml /app/

# Устанавливаем зависимости с помощью Poetry (без dev-зависимостей)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Копируем все файлы приложения в контейнер
COPY . /app/

# Указываем команду для запуска приложения
CMD ["poetry", "run", "python", "main.py"]
