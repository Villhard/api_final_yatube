# api_final

### Описание
Yatube - это платформа для блогов

### Установка
1. Клонируйте репозиторий на локальный компьютер
```bash
git clone https://github.com/Villhard/api_final_yatube.git
```
2. Перейдите в папку с проектом
```bash
cd api_final_yatube
```
3. Создайте виртуальное окружение
windows:
```bash
python -m venv venv
```
linux/macOS:
```bash
python3 -m venv venv
```
4. Активируйте виртуальное окружение
windows:
```bash
source venv/Scripts/activate
```
linux/macOS:
```bash
source venv/bin/activate
```
5. Установите зависимости
```bash
pip install -r requirements.txt
```
6. Примените миграции
```bash
python manage.py migrate
```
7. Запустите сервер
```bash
python manage.py runserver
```