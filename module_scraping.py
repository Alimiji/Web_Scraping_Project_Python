import requests
from bs4 import BeautifulSoup

# Cette fonction permet de d'extraire les données d'une équipe à partir d'une url correspondante
def team_players_stats_V1(url):
    mainPage = requests.get(url)
    soup = BeautifulSoup(mainPage.content)
    # Extraction des noms
    table = soup.find("tbody", "Table__TBODY")
    #print(urls[0])
    nom_equipe = []
    nom_equipe.append(url.split("/")[-1])
    nom_equipe[0] = " ".join(nom_equipe[0].split("-"))

    trs = table.find_all("tr")
    tds = []
    for elmt in trs:
        tds.append(elmt.find("a"))


    Names = []

    for elmt in tds[:-2]:
        v = str(elmt).rstrip("</a>").split(">")
        Names.append(v[1])

    Names = nom_equipe + Names
    # extraction des statistiques

    # extraction des noms des stats

    # tr = soup.find("tr","Table__TR Table__even")

    theads = soup.find_all("thead", "Table__header-group Table__THEAD")

    thead_stat_name = theads[1]

    As = thead_stat_name.find_all("a")

    stat_names = []  # Liste des attributs
    for elmt in As:
        stat_names.append(elmt.text)

    stats_players = []  # Liste des statistiques par joueur

    trs = soup.find_all("tr", "Table__TR Table__TR--sm Table__even")

    for tr in trs:

        spans = tr.find_all("span")
        stats_player = []  # Liste des satistiques d'un joueur
        for elmt in spans:
            stats_player.append(elmt.text)

        stats_players.append(dict(zip(stat_names, stats_player)))

    Names.append("TOTAL")

    stats_players = stats_players[len(Names) + 1:2 * len(Names)]

    Names_stats_players = dict()

    Names_stats_players[Names[0]] = dict(zip(Names[1:], stats_players))

    return(Names_stats_players)

def team_players_stats_V2(url):
    mainPage = requests.get(url)
    soup = BeautifulSoup(mainPage.content)
    # Extraction des noms
    table = soup.find("tbody", "Table__TBODY")
    #print(urls[0])
    nom_equipe = []
    nom_equipe.append(url.split("/")[-1])
    nom_equipe[0] = " ".join(nom_equipe[0].split("-"))

    trs = table.find_all("tr")
    tds = []
    for elmt in trs:
        tds.append(elmt.find("a"))


    Names = []

    for elmt in tds[:-2]:
        v = str(elmt).rstrip("</a>").split(">")
        Names.append(v[1])

    Names = nom_equipe + Names
    # extraction des statistiques

    # extraction des noms des stats

    # tr = soup.find("tr","Table__TR Table__even")

    theads = soup.find_all("thead", "Table__header-group Table__THEAD")

    thead_stat_name = theads[1]

    As = thead_stat_name.find_all("a")

    stat_names = []  # Liste des attributs
    for elmt in As:
        stat_names.append(elmt.text)

    stats_players = []  # Liste des statistiques par joueur

    trs = soup.find_all("tr", "Table__TR Table__TR--sm Table__even")

    for tr in trs:

        spans = tr.find_all("span")
        stats_player = []  # Liste des satistiques d'un joueur
        for elmt in spans:
            stats_player.append(elmt.text)

        stats_players.append(stats_player)

    Names.append("TOTAL")

    stats_players = stats_players[len(Names) + 1:2 * len(Names)]

    #Names_stats_players = dict()

    #Names_stats_players[Names[0]] = dict(zip(Names[1:], stats_players))

    return(Names[0], Names[1:], stat_names, stats_players)


