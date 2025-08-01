from fastapi import FastAPI
app=FastAPI()
@app.get("/ew")
def w():
    return{
        "message":"Hellp ya Mahmoud"
    }
