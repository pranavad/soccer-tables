# Soccer-tables
Up to date association football league tables, made with Python

#Introduction

A simple python script which gets the current league table for various football leagues of the world. It uses the [football-data API](football-data.org).

# How to use
1. Run the script
2. Enter the required League ID
3. The League table for the selected league will be displayed.

# Requirements

* [Python 3](python.org)
* Python requests module


### How to install the required modules
1. Install Python.
2. Go to Command Line.
3. Run the following commands
<br>
```
$ py -m pip install requests
```
# Sample I/O

####Input
```
398
```
####Output
```
Position  Team Name                      Points    Goals Scored    Goals Conceded    Goal Difference
1         Arsenal FC                      43          37               21                16
2         Leicester City FC               43          38               25                13
3         Manchester City FC              40          39               21                18
4         Tottenham Hotspur FC            36          34               17                17
5         West Ham United FC              35          33               24                9
... 
```
###Supported Leagues

The script accesses the football-data.org API, and can only use their data for the leagues. 

Currently, the leagues supported are - 

* Bundesliga
* 2. Bundesliga
* Ligue 1
* Ligue 2
* Barclays Premier League
* Primera Division
* Segunda Division
* Serie A
* Primeira Liga
* 3. Bundesliga
* Eredivisie

The API used can be found [here](http://api.football-data.org/)

