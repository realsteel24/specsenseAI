from config import API_KEY, GEMINI_MODEL, OLLAMA_MODEL, TEMPERATURE
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from typing import List, Literal
import os
import pandas as pd
from langchain_ollama import ChatOllama
import json
from utils.prompts import prompt_generator
from utils.pydantic import get_parser 


# Read data
product = pd.read_csv(r'./data/product_catalog.csv')
userdata = pd.read_csv(r'./data/user_profiles.csv')
## Test data
# data = product.head(1).to_json(orient='records')
data = product[product['category']=='Laptop'].head(10)

# Get Parser
parser, format_instructions = get_parser()
if not isinstance(format_instructions, str):
    format_instructions = json.dumps(format_instructions)

# Initialize prompt
assembled_prompt = prompt_generator(data, format_instructions)

# Building Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", assembled_prompt),
    ("system", "{json_data}"),
    ("system", "{format_instructions}"),
    ("user", "{input}")
])

# formatted_prompt = prompt.format_messages(
#     json_data=data,
#     format_instructions=format_instructions,
#     input="I need a big phone with excellent camera quality and long battery life.",
# )
# print(formatted_prompt)


llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL, api_key=API_KEY, temperature=TEMPERATURE)
llm = ChatOllama(model=OLLAMA_MODEL, temperature=TEMPERATURE)

# Chaining actions
chain = prompt | llm | parser

# Invoke chain
response = chain.invoke({
    "input": "I want to buy a gaming laptop which is budget friendly and is light weight. It SHOULD HAVE GOOD Cooling",
    "json_data": data,
    "format_instructions": format_instructions    
})

print(f"Recommendation: {response.reason} \n User Needs - \n Hard Specs: {response.hard_spec} \n Soft Specs: {response.soft_needs}")
print(response)