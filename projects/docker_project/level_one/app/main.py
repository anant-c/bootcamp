from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "Hello!!"}

@app.get("/status")
def display_status():
    return {"status": "Server is up!!"}