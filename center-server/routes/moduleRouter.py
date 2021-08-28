from fastapi import APIRouter;
from pydantic import BaseModel;

router = APIRouter();

class HT(BaseModel):
    temp: str
    humi: str

class HTData(BaseModel):
    macAddress: str
    data: HT

@router.post("/HT/update")
async def updateHT(data: HTData):
    print(data)
    return {
        "result": True
    }