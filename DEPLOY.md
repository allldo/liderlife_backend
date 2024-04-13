Nginx config:
```
server {
    listen 80;
    server_name test-liderlife.tw1.ru;

    location / {
        # Проксирование запросов к приложению Vue.js
        proxy_pass http://localhost:8080;
    }

    location /static/ {
        # Проксирование запросов к статическим файлам Vue.js
        proxy_pass http://localhost:1337/static/;
    }

    location /media/ {
        # Проксирование запросов к медиа-файлам Django
        proxy_pass http://localhost:1337/media/;
    }

    location /images/ {
        # Проксирование запросов к изображениям Django
        proxy_pass http://localhost:1337/images/;
    }

    location /admin/ {
        # Проксирование запросов к админ-панели Django
        proxy_pass http://localhost:1337/admin/;
    }

    location /api/v1/ {
        # Проксирование запросов к API Django
        proxy_pass http://localhost:1337/api/v1/;
    }
}
```