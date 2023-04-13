from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/order/<string:order_id>/gender', methods=['GET'])
def get_gender(order_id):
    count_men = 0
    count_women = 0
    men_products = {'beers coolers', 'hot dogs bacon sausage', 'frozen meals',
                    'frozen meat seafood', 'chips pretzels', 'nuts seeds dried fruit', 'popcorn jerky', 'energy sports drinks', 
                    'spirits', 'red wines', 'white wines', 'specialty wines champagnes', 
                    'bulk dried fruits vegetables', 'bulk grains rice dried goods'}

    women_products = {'beauty', 'body lotions soap', 'deodorants', 'facial care', 
                      'feminine care', 'hair care', 'oral hygiene', 'skin care', 
                      'vitamins supplements', 'yogurt', 'fresh fruits', 'fresh vegetables', 
                      'fresh herbs', 'fresh pasta', 'packaged produce', 'packaged cheese', 
                      'packaged meat', 'packaged poultry', 'packaged seafood', 'canned fruit applesauce', 
                      'canned jarred vegetables', 'cereal', 'granola', 'hot cereal pancake mixes', 
                      'baking ingredients', 'baking supplies decor', 'air fresheners candles', 
                      'cleaning products', 'laundry', 'paper goods', 'trash bags liners'}

    # In a real implementation, you would query a database or other data source to get the products associated with the order
    # Here, we're using a hardcoded example
    order_df = pd.read_csv("orders.csv", index_col="order_id").astype('int')
    # Check if the order exists
    if int(order_id) not in order_df.index:
        return f"Order {order_id} not found", 404
    order_id = int(order_id)
    record = order_df.loc[order_id]

    # Count the number of products associated with each gender
    for p in men_products:
        if p in record.index:
            count_men += record[p]
    for p in women_products:
        if p in record.index:
            count_women += record[p]

    # Determine the gender associated with the order
    if count_men > count_women:
        return 'male'
    elif count_women > count_men:
        return 'female'
    else:
        return 'unknown'

