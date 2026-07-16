from fastapi import FastAPI 
import uvicorn

app=FastAPI()




def start():
    uvicorn.run("git_demos.main:app",
                host="127.0.0.1",
                port=9089,
                reload=True)