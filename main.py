from fastapi import FastAPI
from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware
#from pydantic import BaseModel
#from app.conversation import conversation
from transformers import pipeline


checkpoint = "../LaMini-T5-61M"

model = pipeline('text2text-generation', model = checkpoint)

#myinput=input("Enter your query here - ")
myinput = "who is prime minister on usa"

# class Input(BaseModel):
#     human_input: str

# class Output(BaseModel):
#     output: str

app=FastAPI()

@app.post("/conversation")
async def resp_fun(myinput):
    input_prompt = myinput
    generated_text = model(input_prompt, max_length=512, do_sample=True)[0]['generated_text']
    return generated_text

origins = [
    "<http://localhost>",
    "<http://localhost:5173>",
        "...Your Domains..."
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

