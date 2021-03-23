**Установка зависимостей**

```apt install nginx```

```pip install django```

```pip install gunicorn```

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
