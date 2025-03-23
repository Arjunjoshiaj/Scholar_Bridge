from fastapi import FastAPI
from database import create_db, get_scholarships

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to ScholarBridge API"}

@app.get("/scholarships/")
def list_scholarships():
    return get_scholarships()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
  
