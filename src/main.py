from routers import items, users
from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/{fake_id}")
def read_fake_id(fake_id: int):
    return {"msg": fake_id}


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='localhost', log_level='info', reload=True
    )