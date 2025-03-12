from fastapi import FastAPI

app = FastAPI()


@app.get("/request_assistance")
def get():
    return {"message": "Requested!"}
