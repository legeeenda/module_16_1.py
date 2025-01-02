from fastapi import FastAPI, Query, Path, HTTPException
from typing import Optional

app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user")
async def read_user_with_query(
    username: str = Query(..., description="Имя пользователя"),
    age: int = Query(..., description="Возраст пользователя")
):
    return {"message": str(f"Информация о пользователе. Имя: {username}, Возраст: {age}")}


@app.get("/user/{user_id}")
async def read_user_by_id(user_id: str = Path(..., description="ID пользователя")):
    if user_id == "admin":
        raise HTTPException(status_code=404, detail="Пользователь 'admin' не допустим здесь")
    return {"message": str(f"Вы вошли как пользователь № {user_id}")}
