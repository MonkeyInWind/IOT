from fastapi import APIRouter;
from pydantic import BaseModel;
import time, datetime;
from scripts import ht;

router = APIRouter();

@router.get("/HT/today")
async def getTodayHT():
    todayStart = int(time.mktime(datetime.date.today().timetuple()) * 1000);
    data = ht.getHT(todayStart, time.time() * 1000);
    return {
        "result": True,
        "data": data
    }