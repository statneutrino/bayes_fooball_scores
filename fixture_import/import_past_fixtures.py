import requests
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
import os
import json
import yaml
from datetime import datetime


# For instanitate api_import class
# # Read YAML file
# with open("settings.yaml", 'r') as stream:
#     api_settings = yaml.safe_load(stream)


def save_api_fixtures(league, season, save_dir="data", filename = None):

    # Read YAML file
    with open("settings.yaml", 'r') as stream:
        api_settings = yaml.safe_load(stream)

    # Use yaml settings for API call settings
    url = api_settings['api']['base_url'] + 'fixtures'
    querystring = {"league":str(league),"season":str(season)}
    headers = {
        'x-rapidapi-host': api_settings['api']['host'],
        'x-rapidapi-key': api_settings['api']['key']
    }
    # GET fixture response
    response = requests.request("GET", url, headers=headers, params=querystring)

    # Save file
    if filename is None:
        now = datetime.now()
        ingested_date = now.strftime("%y-%m-%d")
        filename = "fixtures_{}_{}_{}.json".format(league, season, ingested_date)
    
    save_path = os.path.join(os.getcwd(), save_dir, filename)
    with open(save_path, 'w') as f:
        f.write(response.text)
    
    return "Complete"


if __name__ == "__main__":
    league = 39
    season = 2021
    x = save_api_fixtures(league, season)
    print(x)
