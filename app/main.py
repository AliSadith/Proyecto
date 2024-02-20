from fastapi import FastApi, request, response

app = FastAPI()






@app.get("/")
async def root():
    return {"message": "la aplicacion esta funcionando"}