import csv
from Classes.Logic.LogicMilestone import LogicMilestone

class Milestones:

    def createMilestone(Index):
        with open('Classes/Files/assets/csv_logic/milestones.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    
                    if row[0] == "":
                        continue
                    if line_count - 2 == Index:
                        logicMilestone = LogicMilestone()
                        logicMilestone.setType(row[1])
                        logicMilestone.setIndex(row[2])
                        logicMilestone.setProgressStart(row[3])
                        logicMilestone.setProgress(row[4])
                        logicMilestone.setLeague(row[5])
                        logicMilestone.setTier(row[6])
                        logicMilestone.setSeason(row[7])
                        logicMilestone.setSeasonEndRewardKeys(row[8])
                        logicMilestone.setPrimaryLvlUpRewardType(int(row[9]))
                        logicMilestone.setPrimaryLvlUpRewardCount(int(row[10]))
                        logicMilestone.setPrimaryLvlUpRewardExtraData(row[11])
                        logicMilestone.setPrimaryLvlUpRewardHero(row[12])
                        logicMilestone.setPrimaryLvlUpRewardSkin(row[13])
                        logicMilestone.setSecondaryLvlUpRewardType(row[14])
                        logicMilestone.setSecondaryLvlUpRewardCount(row[15])
                        logicMilestone.setSecondaryLvlUpRewardExtraData(row[16])
                        logicMilestone.setSecondaryLvlUpRewardHero(row[17])
                        return logicMilestone
                    line_count += 1
                    
    def getAllMilestonesWithType(type, season = -1):
        milestones = []
        with open('Classes/Files/assets/csv_logic/milestones.csv', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    
                    if row[0] == "":
                        continue
                    if int(row[1]) == type and (season == -1 or int(row[7]) == season):
                        milestones.append(Milestones.createMilestone(line_count-2))
                    line_count += 1
        return milestones
           
        