import  requests
def main():
    print("394 : Bundesliga")
    print("395 : 2. Bundesliga")
    print("396 : Ligue 1")
    print("397 : Ligue 2")
    print("398 : Barclays Premier League")
    print("399 : Primera Division")
    print("400 : Segunda Division")
    print("401 : Serie A")
    print("402 : Primeira Liga")
    print("403 : 3. Bundesliga")
    print("404 : Eredivisie")

    #Taking the league ID for the League Table to be checked

    league_id = input("\nEnter League ID to get league table")



    r = requests.get("http://api.football-data.org/v1/soccerseasons/" + league_id + "/leagueTable")

    # Checking if the League IDs are available or not. Displaying an error message if League IDs are wrong

    if r.status_code == 200:
        r = r.json()

        #Getting the current league standings for the League and setting it to the variable standing

        standing = r["standing"]
        print("\nPosition ","Team Name ","                    Points","   Goals Scored","   Goals Conceded","   Goal Difference")

        # Printing every position in the standings along with team name, points, etc

        for x in standing:
             team = str(x["position"])+ "         " + x["teamName"]
             spaces = " "
             nospace = 40 - len(team)
             spaces = spaces * nospace
             print(team,spaces, x["points"],"        ",x["goals"],"             ",x["goalsAgainst"],"              ",x["goalDifference"])
    else:
        print("Please enter proper League IDs")

if __name__ == "__main__":
    main()

