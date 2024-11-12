from flask import Flask, request, jsonify, make_response, render_template, send_from_directory
from flask_cors import CORS
import numpy as np
import pandas as pd
from flask_caching import Cache
import os

app = Flask(__name_ _)
CORS(app)  # Enable CORS
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

def load_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

df = load_excel('not_null_data_value_new.xlsx')

def piecewise_function(x):
    if x < -2000:
        return 95 - 15 * np.exp(0.0001 * x)
    elif -2000 <= x <= 0:
        return 70 + 10 * (1 - np.exp(np.log(0.1) / -1999 * x))
    elif 0 < x <= 2000:
        return 28.62 * np.exp(-0.00665 * x) + 40
    else:
        return 100 * np.exp(-0.000278 * x) + 1

def calculate_qualitative(x):
    if 70 <= x <= 99:
        return 'Khoshbinane'
    elif 40 <= x < 70:
        return 'normal'
    elif 0 <= x < 40:
        return 'bad_binane'

def convert_group_name_to_numeric(group_name):
    group_name_mapping = {
        "انسانی": 1,
        "ریاضی": 2,
        "تجربی": 3,
        "هنر": 4,
        "زبان": 5
    }
    return group_name_mapping.get(group_name, group_name)

@cache.memoize(timeout=28800)
def tmp(quota_rank, quota_number, group_name, reshte_name_new, type_new, cities, states):
    if df is None:
        return []
    
    group_name = convert_group_name_to_numeric(group_name)
    
    results = []    
    quota_column = f'region_{quota_number}_quota_rank'

    filtered_df = df[df['group_name_new'] == group_name]

    if reshte_name_new:
        filtered_df = filtered_df[filtered_df['reshte_name_new'].isin(reshte_name_new)]
    if type_new:
        filtered_df = filtered_df[filtered_df['type_new'].isin(type_new)]
    if cities:
        filtered_df = filtered_df[filtered_df['city_new'].isin(cities)]
    if states:
        filtered_df = filtered_df[filtered_df['state_new'].isin(states)]

    for index, row in filtered_df.iterrows():
        code = row['digits']
        result = {
            'reshte_code': code,
            'reshte_name': row['reshte_name'],
            'university': row['university'],
            'state': row['state'],
            'city': row['city'],
            'type': row['type'],
            'probability_percentage': None,
            'qualitative_probability': '',
            'group_name': group_name
        }

        quota_value = row[quota_column]
        if pd.isna(quota_value):
            continue
        else:
            difference = int(quota_rank) - quota_value
            probability_percentage = piecewise_function(difference)
            qualitative_probability = calculate_qualitative(probability_percentage)
            result['probability_percentage'] = probability_percentage
            result['qualitative_probability'] = qualitative_probability
            results.append(result)
    
    return results

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    quota_rank = data['quota_rank']
    quota_number = data['quota_number']
    group_name = data['group_name']
    reshte_name_new = data.get('reshte_name_new', [])
    type_new = data.get('type_new', [])
    cities = data.get('city_new', [])
    states = data.get('state_new', [])

    results = tmp(quota_rank, quota_number, group_name, reshte_name_new, type_new, cities, states)
    
    response = make_response(jsonify(results))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# تعریف تابع clear_cache
def clear_cache():
    cache.clear()           
    print("Cache successfully cleared")

if __name__ == '__main__':
    clear_cache()
    app.run(host='0.0.0.0', port=5000, debug=True)
