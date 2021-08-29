from fastapi import APIRouter;
from pydantic import BaseModel;
import json;
from db import database;

router = APIRouter();
insertHT = database.insertHT;

class HT(BaseModel):
    temp: str
    humi: str

class HTData(BaseModel):
    macAddress: str
    data: HT

@router.post("/HT/update")
async def updateHT(data: HTData):
    macAddress = data.macAddress;
    ht = data.data;
    insertHT({
        "macAddress": macAddress,
        "temp": ht.temp,
        "humi": ht.humi
    });
    return {
        "result": True
    }