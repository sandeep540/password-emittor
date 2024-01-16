from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/")
async def root(request: Request):
    """Prints 'Hello, world!' to the console."""
    data = await request.json()
    print(data)
    return {"message": "Hello, world!"}



