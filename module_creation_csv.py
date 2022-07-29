# Cette fonction permet d'importer les données extraites dans un fichier csv

def data_fichier_csv(data):

    with open("data.csv", "w", newline="") as f:
        f.truncate(0) # fonction permettant de reinitialiser le fichier
        f.seek(0) # Fonction permettant de se positionner en début du fichier

        # Ecriture du glossaire des statistiques de chaque joueur
        f.write("\n \n GLOSSAIRE DES STATISTIQUES \n \n")
        f.write("POS:Position \n GP:Games Played \n AB:At Bats \n R:Runs \n H:Hits \n AVG:Batting Average \n 2B:Doubles\n")
        f.write("3B :Triples \n  HR:Home Runs \n RBI:Runs Batted In \n TB:Total Bases \n BB:Walks \n K:Strikeouts \n SB:Stolen Bases \n")
        f.write("OBP:On Base Percentage \n SLG:Slugging Percentage \n OPS:OPB Pct + SLG Pct \n WAR:Wins Above Replacement \n \n")

        f.write("STATISTIQUES DES SERIES ELIMINATOIRES 2021 DE TOUS LES JOUEURS DE BATON (BASEBALL) DE TOUTES LES DIVISIONS \n \n")

        for d in data:
            entete = "Nom des joueurs;" + ";".join(d[2])
            f.write(d[0].upper() + "\n \n" + entete + "\n")
            for i in range(len(d[1])):
                f.write(d[1][i] + ";" + ";".join(d[3][i]) + "\n")

            f.write("\n \n")