from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from routes import moduleRouter;

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(moduleRouter.router, prefix="/api")

@app.get('/heart_beat')
async def heartBeat():
    return True;

if __name__ == "__main__":
    import uvicorn;
    port = 6080;
    uvicorn.run(app="main:app", host="0.0.0.0", port=port, reload=True, debug=True);