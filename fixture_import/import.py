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


def get_most_recent_fixtures(league, season, data_dir='data'):
    try:
        filenames = os.listdir(os.path.join(os.getcwd(), data_dir))
        prefix = "fixtures_{}_{}_".format(league, season)
        fixture_data_files = [x for x in filenames if x.startswith(prefix)]
        assert len(fixture_data_files) >= 1, "No file found with expected prefix {}".format(prefix)
    except AssertionError as error:
        raise error
    
    if len(fixture_data_files) > 1:
        dates = [x[len(prefix):-len('.json')] for x in fixture_data_files]

        dates = map(lambda x: datetime.strptime(x, '%y-%m-%d').date(), dates)
        most_recent_date = max(dates)
        source_filename = prefix + str(most_recent_date) + '.json'

    else:
        source_filename = fixture_data_files[0]
    return source_filename
    



if __name__ == "__main__":
    league = 39
    season = 2021
    # x = save_api_fixtures(league, season)
    # print(x)
    x = get_most_recent_fixtures(league, season)
    print(x)