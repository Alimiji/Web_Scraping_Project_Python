import requests
from bs4 import BeautifulSoup
import module_scraping as ms
import module_creation_csv as m_csv
import csv
# Le but de ce programme est d'extraire les 18 premieres statistiques des joueurs
# de chaque équipe de baseball de la page d'url: https://www.espn.com/mlb/stats/player
# et de stocker les données dans un fichier csv
# Glossaire des 18 statistiques de chaque joueur
"""
POS:Position
GP:Games Played
AB:At Bats
R:Runs
H:Hits
AVG:Batting Average
2B:Doubles
3B :Triples
HR:Home Runs
RBI:Runs Batted In
TB:Total Bases
BB:Walks
K:Strikeouts
SB:Stolen Bases
OBP:On Base Percentage
SLG:Slugging Percentage
OPS:OPB Pct + SLG Pct
WAR:Wins Above Replacement

"""
mainPage = requests.get("https://www.espn.com/mlb/stats/player")
# Extraction de tous les balises y compris leur contenus de la page principale
soup = BeautifulSoup(mainPage.content)
# recupération de tous les balises select et de tous les balises contenues
# dans la balise select de la page principale
selects = soup.find_all("select")
# Recuperation de tous les balises options y compris leur contenu
# dans la premiere balise select
options = selects[0].find_all("option")

#print(selects)
#Stockage de tout les urls de chaque equipe de base baseball

urls = ["https://www.espn.com" + option['data-url'] for option in options][1:]
#print(urls)
data_V1 = [] # Liste de tous les données sous forme de dictionnaire

data_V2 = [] # Liste de tous les données sous forme de tuples

#print(ms.team_players_stats(urls[2]))

# Stockage de la liste des données sous forme de liste de dictionnaires
for url in urls:

    #print(ms.team_players_stats(url))
    
    data_V1.append(ms.team_players_stats_V1(url))


#print(data_V1)

# Stockage de la liste des tuples (nom de l'équipe, liste des joueurs, liste des statistiques de chaque joueur)

for url in urls:

    # print(ms.team_players_stats(url))

    data_V2.append(ms.team_players_stats_V2(url))

print(len(data_V2[0][1]))

#print(data_V2)



m_csv.data_fichier_csv(data_V2)

