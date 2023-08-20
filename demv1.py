from transformers import pipeline

checkpoint = "../LaMini-T5-61M"

model = pipeline('text2text-generation', model = checkpoint)

myinput=input("Enter your query here - ")


def resp_fun(myinput):
    input_prompt = myinput
    generated_text = model(input_prompt, max_length=512, do_sample=True)[0]['generated_text']
    print("Response", generated_text)

resp_fun(myinput)