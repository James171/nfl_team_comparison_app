import os
import time
import json
import pdb

from flask import Flask, flash, jsonify, redirect, render_template, request, session

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import lookup, usd, lookup_stats

# Configure application
app = Flask(__name__)



# Custom filter
app.jinja_env.filters["usd"] = usd


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/match_up", methods=["GET", "POST"])

def match_up():
    # Function to pull stats from Team1 and Team2
    if request.method == "POST":
        team_stats_1 = lookup_stats(request.form.get("team_1"))

        time.sleep(2)

        team_stats_2 = lookup_stats(request.form.get("team_2"))

        time.sleep(2)

        # Comparing team2 and team1 stats in order to get disparity 

        comparison = {"Total Rush yds" : team_stats_2['record']['rushing']['yards'] - team_stats_1['record']['rushing']['yards'],
        "Avg Rush yds" : team_stats_2['record']['rushing']['avg_yards'] - team_stats_1['record']['rushing']['avg_yards'],
        "Total Rush TDs" : team_stats_2['record']['rushing']['touchdowns'] - team_stats_1['record']['rushing']['touchdowns'],
        "Total Pass yds" : team_stats_2['record']['passing']['yards'] - team_stats_1['record']['passing']['yards'],
        "Avg Pass yds" : team_stats_2['record']['passing']['avg_yards'] - team_stats_1['record']['passing']['avg_yards'],
        "Passing Cmp pct" : team_stats_2['record']['passing']['cmp_pct'] - team_stats_1['record']['passing']['cmp_pct'],
        "Passing Touchdowns" : team_stats_2['record']['passing']['touchdowns'] - team_stats_1['record']['passing']['touchdowns'],
        "Passer Rating" : team_stats_2['record']['passing']['rating'] - team_stats_1['record']['passing']['rating'],
        "Passer Sacked" : team_stats_2['record']['passing']['sacks'] - team_stats_1['record']['passing']['sacks'],
        "Int Thrown" : team_stats_2['record']['passing']['interceptions'] - team_stats_1['record']['passing']['interceptions'],
        "Team Penalties" : team_stats_2['record']['penalties']['penalties'] - team_stats_1['record']['penalties']['penalties'],
        "Team Penaly yds" : team_stats_2['record']['penalties']['yards'] - team_stats_1['record']['penalties']['yards'],
        "Field Goals Made" : team_stats_2['record']['field_goals']['made'] - team_stats_1['record']['field_goals']['made'],
        "Field Goals attempts" : team_stats_2['record']['field_goals']['attempts'] - team_stats_1['record']['field_goals']['attempts'],
        "Third down efficiency" : team_stats_2['record']['efficiency']['thirddown']['pct'] - team_stats_1['record']['efficiency']['thirddown']['pct'],
        "Redzone efficiency" : team_stats_2['record']['efficiency']['redzone']['pct'] - team_stats_1['record']['efficiency']['redzone']['pct'],
        "Goal-To-Go efficiency" : team_stats_2['record']['efficiency']['goaltogo']['pct'] - team_stats_1['record']['efficiency']['goaltogo']['pct'],
        "QB hurries" : team_stats_2['record']['defense']['hurries'] - team_stats_1['record']['defense']['hurries'],
        "QB Hits" : team_stats_2['record']['defense']['qb_hits'] - team_stats_1['record']['defense']['qb_hits'],
        "QB Sacks" : team_stats_2['record']['defense']['sacks'] - team_stats_1['record']['defense']['sacks'],
        "Interceptions" : team_stats_2['record']['defense']['interceptions'] - team_stats_1['record']['defense']['interceptions'],
        "Forced Fumbles" : team_stats_2['record']['defense']['forced_fumbles'] - team_stats_1['record']['defense']['forced_fumbles']}

        list2 = sorted(comparison.values())
        list1 = sorted(comparison, key=comparison.__getitem__)

        return render_template("information.html", team_stats_1=team_stats_1, team_stats_2=team_stats_2, list1=list1, list2=list2)
        
    
    else:
    
    
        # create a dict matching team name to ID
        team_dict={}

        data = lookup(request.form.get("symbol"))
        # Traversing API to get Team IDs
        for j in data["conferences"]:
                for i in j["divisions"]:
                    for s in i["teams"]:
                        team_dict[s['id']] = s['name']

        return render_template("match_up.html", data=team_dict)


