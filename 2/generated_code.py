import pandas as pd
def answer():
    df_cleaned = pd.read_csv('sales_data_cleaned.csv')
    res = df_cleaned.groupby('PRODUCTCODE')['SALES'].sum().sort_values(ascending=False).head(1)
    return res