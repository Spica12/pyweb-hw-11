from fastapi import FastAPI


app = FastAPI()


@app.get("/healthchecker")
async def healthchecker():
    return {'message': 'Hello World!'}
