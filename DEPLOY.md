Docker up without build:
```shell
docker compose -f docker-compose.prod.yaml up -d
```

Docker up with build:
```shell
docker compose -f docker-compose.prod.yaml up -d --build
```

Load backups (inside backend_web container):
```shell
# docker exec -it %container% sh
python3 ./manage.py loaddata --exclude auth.permission --exclude admin.logentry --exclude contenttypes ./manual_backups/12.04.24_10-30.json
```

Certbot for domain:
```shell
sudo certbot -d liderlife.ru
```

Nginx config (production):
```groovy
server {
        listen 80;
        server_name liderlife.ru;
        return 301 https://liderlife.ru$request_uri;
}

server {
    listen 443 ssl;
    server_name liderlife.ru;

    ssl_certificate /etc/letsencrypt/live/liderlife.ru/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/liderlife.ru/privkey.pem; # managed by Certbot

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';

    charset utf-8;

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

    location /image/ {
        # Проксирование запросов к изображениям Django
        proxy_pass http://localhost:1337/image/;
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