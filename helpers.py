import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

# Hide API Key from viewers
api_key = os.environ['API_KEY']



# Lookup function to to get hierarchy api information and team ID
def lookup(symbol):
    

    # Contact API
    try:
        response = requests.get(f"http://api.sportradar.us/nfl/official/trial/v5/en/league/hierarchy.json?api_key={api_key}")
        # print(response.headers)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        data = response.json()
        return data


    except (KeyError, TypeError, ValueError):
        return None

def lookup_stats(team_id):


    # Contact API
    try:
        response = requests.get(f"http://api.sportradar.us/nfl/official/trial/v5/en/seasons/2019/REG/teams/{team_id}/statistics.json?api_key={api_key}")
        # print(response.headers)
        print(response)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        data_stats = response.json()
        return data_stats


    except (KeyError, TypeError, ValueError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
