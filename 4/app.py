from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route('/recommendation/<int:order_hour_of_day>', methods=['GET'])
def recommendation(order_hour_of_day):
    # Load the data and group by hour of day
    order_df4 = pd.read_csv("orders.csv")
    grouped_data = order_df4.groupby("order_hour_of_day")["days_since_prior_order"].mean()

    # Check for trend or anomaly
    avg_days_since_prior_order = grouped_data.loc[order_hour_of_day]
    if avg_days_since_prior_order > 15:
        recommendation = f"Customers tend to order less frequently at {order_hour_of_day}:00. Consider running a promotion or offering discounts during these times."
    else:
        recommendation = f"No significant trend or anomaly at {order_hour_of_day}:00."
        
    return recommendation