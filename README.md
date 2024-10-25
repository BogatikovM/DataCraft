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
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=mydatabase
