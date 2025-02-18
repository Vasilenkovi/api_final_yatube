# api_final
api final
## Документация
Полная документация API доступна по адресу `/redoc/` после запуска сервера.
```

### 8. Выполнение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Тестирование API
- Получение токена: `/api/v1/jwt/create/`
- Создание поста: `/api/v1/posts/`
- Подписка на автора: `/api/v1/follow/`

