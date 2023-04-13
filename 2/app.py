import openai
import pandas as pd
import os

openai.api_key = "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"

df_cleaned = pd.read_csv('sales_data_cleaned.csv')

def process_query(query):
    prompt = f"Given a dataframe(df_cleaned) with columns 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER','SALES', 'ORDERDATE','STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID', 'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'ADDRESSLINE1', 'CITY''COUNTRY', 'DEALSIZE', understand the following query: {query} and write pandas code for it(code only, no text)"
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        timeout=10,
    )
    print(response)
    return response.choices[0].text.strip()

res = process_query("What is my top earning sale item?")
print(res)
exec(res)