from fastapi import FastAPI

router = FastAPI()

@router.get("/")
async def index():
    return {"message": "Hello World"}
