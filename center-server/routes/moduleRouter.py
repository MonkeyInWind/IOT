from fastapi import APIRouter;
from pydantic import BaseModel;

router = APIRouter();

class HT(BaseModel):
    temp: str
    humi: str

@router.post("/HT/update")
async def updateHT(data: HT):
    print(data)
    return {
        "result": True
    }