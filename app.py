from config import api_key, gemini_model, ollama_model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from typing import List, Literal
import os
import pandas as pd
from langchain_ollama import ChatOllama
import json
from utils.prompts import prompt_generator
from utils.pydantic import SpecItem, get_parser 


# Read data
product = pd.read_csv(r'./data/product_catalog.csv')
userdata = pd.read_csv(r'./data/user_profiles.csv')

# Get Parser
parser, format_instructions = get_parser()

# Initialize prompt
assembled_prompt = prompt_generator(userdata.to_json(orient='records'))

# Confirm parser works
prompt = ChatPromptTemplate.from_messages([{"system",assembled_prompt},
                                           {"system": format_instructions},
                                           {"user": "{input}"}])

# llm = ChatGoogleGenerativeAI(model=gemini_model, api_key=api_key, temperature=0.7)
llm = ChatOllama(model=ollama_model, temperature=0.7)

# Chaining actions
chain = prompt | llm | parser

# Invoke chain
chain.invoke()
