from fastapi import FastAPI
import random

app =FastAPI()

@app.get("/")
async def root():
    return {'example': "Test example", "data": 10}

@app.get("/random")
async def get_random():
    rn: int = random.randint(0,100)
    return {"number": rn, "limit": 100 }

## Custom Limit 
@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(0,limit)
    return {"number": rn, "limit": limit}
    

import uvicorn

if __name__ == "__main__":
    uvicorn.run("your_app:app", host="0.0.0.0", port=8000, log_level="debug", reload=True)



