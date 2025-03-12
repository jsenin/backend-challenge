from fastapi import FastAPI

app = FastAPI()


@app.post("/request_assistance")
def post():
    return {"message": "Requested!"}
