import csv


class Locations:
    def getAllMaps():
        Maps = []
        with open('Classes/Files/assets/csv_logic/locations.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[0] == "":
                        continue
                    if Locations.getGamemodeVariation(line_count - 2)!= "Tutorial":
                        line_count += 1
                    if row[1].lower() != 'true':
                            Maps.append(line_count - 2)
            return Maps
        
    def getGamemodeVariation(ID):
        with open('Classes/Files/assets/csv_logic/locations.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    
                    if row[0] == "":
                        continue
                    if line_count - 2 == ID:
                        return Locations.getGamemodeID(row[10])
                    line_count += 1
    
    def getGamemodeID(gamemodeVariation):
        if gamemodeVariation == "CoinRush":
            return 0
        elif gamemodeVariation == "Campaign":
            return 1
        elif gamemodeVariation == "AttackDefend":
            return 2
        elif gamemodeVariation == "BountyHunter":
            return 3
        elif gamemodeVariation == "Artifact":
            return 4
        elif gamemodeVariation == "LaserBall":
            return 5
        elif gamemodeVariation == "BattleRoyale":
            return 6
        elif gamemodeVariation == "BossFight":
            return 7
        elif gamemodeVariation == "Survival":
            return 8
        elif gamemodeVariation == "BattleRoyaleTeam":
            return 9
        elif gamemodeVariation == "Raid":
            return 10
        elif gamemodeVariation == "RoboWars":
            return 11
        elif gamemodeVariation == "Tutorial":
            return 12
        elif gamemodeVariation == "Training":
            return 13
        elif gamemodeVariation == "BossRace":
            return 14
        elif gamemodeVariation == "SoloBounty":
            return 15
        elif gamemodeVariation == "CaptureTheFlag":
            return 16
        elif gamemodeVariation == "KingOfHill":
            return 17
        elif gamemodeVariation == "Raid_TownCrush":
            return 18
        else:
            print("Wrong game mode!")
            return -1