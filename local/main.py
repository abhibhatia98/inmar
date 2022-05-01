import uvicorn
from dotenv import load_dotenv
load_dotenv(".env.bakery")
from bakery_api import app

if __name__ == "__main__":
    # uvicorn.run("bakery_api:app", host="0.0.0.0", port=8000)
    uvicorn.run(app, host="0.0.0.0", port=8003)
