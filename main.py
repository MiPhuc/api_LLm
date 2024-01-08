from fastapi import FastAPI
from models import *
from functions import *
import uvicorn
import logging


app = FastAPI()
open_api_key = "openai_key"
logging.basicConfig(
    filename='api.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


@app.post("/prompt", response_model = response_json)
async def root(prompt_request : request_json):
    logging.info(f'content: {prompt_request.content}')
    out = generate(prompt_request.content, open_api_key)
    out = [c.message.content for c in out]
    text_out = ' '.join(out)
    logging.info(f'answer: {text_out}')
    return response_json(answer = out)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)