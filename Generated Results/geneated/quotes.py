import os
import groq

groq_api_key = "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"
groq_client = groq.Groq(api_key=groq_api_key)

def generate_lovely_quote(customer_name):
    prompt = f"Generate a lovely quote for {customer_name}"
    response = groq_client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.1-70b-versatile")
    return response

print(generate_lovely_quote("John Doe"))