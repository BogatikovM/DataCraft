# DataCraft
# FastAPI + MongoDB + Vue.js Project

## Описание
Этот проект представляет собой веб-приложение на основе **FastAPI**, использующее **MongoDB** в качестве базы данных. На фронтенде используется **Vue.js**, для упрощения разработки одностраничного приложения (SPA).

### Технологии
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Database: [MongoDB](https://www.mongodb.com/)
- Frontend: [Vue.js](https://vuejs.org/)
- Asynchronous MongoDB driver: [Motor](https://motor.readthedocs.io/en/stable/)

### Переменные окружения
Настройки для подключения к MongoDB и другим сервисам указаны в файле `.env`:

```bash
# Mongo settings
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=mydatabase

# FastAPI settings
APP_ENV=development
APP_HOST=127.0.0.1
APP_PORT=8000
APP_RELOAD=true
```

### Запуск


```bash
uvicorn app.main:app --reload
```
