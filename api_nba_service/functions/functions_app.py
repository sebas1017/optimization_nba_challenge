import json
import requests


def search(target_sum):
    response = requests.get("https://mach-eight.uc.r.appspot.com/")

    if response.status_code == 200:
        data = json.loads(response.text)
        players = data["values"]
        idx_map = {}  
        response_final = []

        for idx, p in enumerate(players):
            h_in = int(p['h_in'])
            if target_sum - h_in in idx_map.keys():  
                p1 = players[idx_map[target_sum - h_in]]  
                p2 = players[idx]
                response_final.append((p1, p2))  
            idx_map[h_in] = idx  
    else:
        response_final = False
    return response_final
        


def get_player_data(player):
    return f"{player['first_name']} {player['last_name']} ({player['h_in']})"


def main_calculus(target_sum):
    try:
        target_sum = int(target_sum)
        result = search(target_sum)
        if result == False:
            return {"message": " NBA player external API error please run later"}
        else: 
            results = []
            for pair in result:
                results.append ( ( f"Player {get_player_data(pair[0])}", f"Player {get_player_data(pair[1])}" )   )
            if len(results) == 0:
                return {"message": "Not match found"}
            else:
                return results           
    except ValueError:
        return  {"error_message": "please insert integer value"}


