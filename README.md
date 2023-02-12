
[//]: # (### Залитый проект)

[//]: # ()
[//]: # (Залитый проект: https://)

[//]: # ()
[//]: # (Admin panel находиться по ссылке "/admin"  )

[//]: # (Данные для входа:)

[//]: # (- Login: "admin")

[//]: # (- Password: "admin")



#### Клонирование проекта
```
git clone https://github.com/fakel-ast/django-stripe.git
```

#### Настройка вирт. окржения.  
Написать команду рядом с requirements.txt файлом

- Создать виртуальное окружение:
  - Для windows: 
    - В папке conf прописать команду: ```python -m venv venv```
  - Для linux:
    - В папке conf прописать команду: ```python3 -m venv venv```
- Активировать его:
  - Для windows: 
    - В папке conf прописать команду: ```venv\Scripts\activate```
  - Для linux:
    - В папке conf прописать команду: ```source venv/bin/activate```
- Установить нужные пакеты:
  В папке conf прописать команду: ```pip install -r requirements.txt```

- Сделать миграции в где лежит manage.py командой: ```python manage.py makemigration & python manage.py migrate```
- Запустить django проложение, прописав: ```python manage.py runserver```
