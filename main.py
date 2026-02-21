from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def home():
    return {"Message": "Hello World"}

@app.get("/about")
def about():
    return {"Page": "About"}

@app.get("/user/{user_id}")
def user(user_id: str):
    return {"Username": user_id}