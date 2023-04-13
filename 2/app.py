import openai
import pandas as pd
from flask import Flask, request, jsonify

openai.api_key = "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"

df_cleaned = pd.read_csv('sales_data_cleaned.csv')

app = Flask(__name__)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    query = request.json['query']
    response = process_query(query)

    file_name = "generated_code.py"
    generate_python_code(file_name, response)
    from generated_code import answer
    return answer()

def process_query(query):
    prompt = f"Given a dataframe(df_cleaned) with columns 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER','SALES', 'ORDERDATE','STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID', 'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'ADDRESSLINE1', 'CITY''COUNTRY', 'DEALSIZE', understand the following query: {query} and write pandas code for it(code only, no text)"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        timeout=10,
    )
    return response.choices[0].text.strip()


def generate_python_code(file_name, code_string):
    code = """
import pandas as pd
def answer():
    df_cleaned = pd.read_csv('sales_data_cleaned.csv')
    res = {}
    return res
    """.format(code_string)
    with open(file_name, 'w') as file:
        file.write(code)


