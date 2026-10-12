import uvicorn
from fastapi import FastAPI
from app.routers.api import router as api_router

app = FastAPI()

# Подключаем импортированный роутер
app.include_router(api_router)

if __name__ == "__main__":
    # Запуск сервера с автоперезагрузкой
    uvicorn.run("run:app",
                host="0.0.0.0",
                port=8000,
                reload=True)

#http://localhost:8000/