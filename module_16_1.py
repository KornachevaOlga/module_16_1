from fastapi import FastAPI
# Создаем экземпляр приложения FastAPI
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": f"Главная страница"}

@app.get("/user/admin")
async def welcome() -> dict:
    return {"message": f"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def news(user_id: int) -> dict:
    return {"message": f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def data_page(username: str, age: int) -> dict:
    return {'Информация о пользователе. Имя' : username,  'Возраст': age}
