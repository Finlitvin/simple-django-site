**Установка зависимостей**
Для разворачивания Django приложения на базе веб-сервера Nginx необходимо открыть терминал линукс-системы, например, введя комбинацию клавиш ctrl+alt+t,и установить все необходимые для запуска зависимости. Это сам Nginx, который устанавливается посредством использования утилиты apt, доступной в большинстве основанных на debian линукс дистрибутивов.

```apt install nginx```

Затем следует установить зависимости для Python. При этом используется менеджер пакетов самого языка python. При этом сам python как правило уже 

```pip3 install django```

```pip3 install gunicorn```

**Загрузка проекта**


```git clone git@github.com:Finlitvin/simple-django-site.git```

**Разворачиваение самого веб-приложения(без Nginx)**

```cd [путь к проекту]/src/simplesite/```

```python manage.py runserver```

**Конфигурирование Nginx для разворачивания веб-приложения**

```sudo nano etc/nginx/sites-available/default```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                include proxy_params;
                proxy_pass http://127.0.0.1:8000;

        } }

**Запуск веб-приложения**

```gunicorn simplesite.wsgi```
