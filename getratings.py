#! /usr/bin/env python3

import requests

#get current and max rating for a player and return average

with open('players', 'r') as f:
    players = [player.rstrip().lower() for player in f]


def getCurrentRating(player):
    r = requests.get(f'https://lichess.org/api/user/{player}').json()
    try:
        current_rating = r['perfs']['crazyhouse']['rating']
    except KeyError:
        return 0
    return current_rating

def getMaxRating(player):
    r = requests.get(f'https://lichess.org/api/user/{player}/rating-history').json()
    zh = next((variant for variant in r if variant['name'] == 'Crazyhouse'), None)
    history = zh['points']
    if history:
        max_rating = max(map(lambda x: x[3], history))
        return max_rating
    else:
        return 0


for player in players:
    print(player, (getCurrentRating(player) + getMaxRating(player)) / 2)
