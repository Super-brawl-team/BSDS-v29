class BattleEndManager:
    # Fideua brawl shitcode jumpscare bc laziness
    def getTrophies(trophies):
        # this should do the job
        reward = (
            8 if trophies < 800 else
            7 if trophies < 900 else
            6 if trophies < 1000 else
            5 if trophies < 1100 else
            4 if trophies < 1200 else
            3
        )

        loss = -min(12, max(0, (trophies - 1) // 100))

        return (reward, loss, 0)
    
    def getLegendaryTrophies(result):
        return [20,5,15][result]
    
    def getTrophiesBattleRoyale(trophies):
        trophy_ranges = [
            (0, 49, [0,10, 8, 7, 6, 4, 2, 2, 1, 0, 0]),
            (50, 99, [0,10, 8, 7, 6, 3, 2, 2, 0, -1, -2]),
            (100, 199, [0,10, 8, 7, 6, 3, 1, 0, -1, -2, -2]),
            (200, 299, [0,10, 8, 6, 5, 3, 1, 0, -2, -3, -3]),
            (300, 399, [0,10, 8, 6, 5, 2, 0, 0, -3, -4, -4]),
            (400, 499, [0,10, 8, 6, 5, 2, -1, -2, -3, -5, -5]),
            (500, 599, [0,10, 8, 6, 4, 2, -1, -2, -5, -6, -6]),
            (600, 699, [0,10, 8, 6, 4, 1, -2, -2, -5, -7, -8]),
            (700, 799, [0,10, 8, 6, 4, 1, -3, -4, -5, -8, -9]),
            (800, 899, [0,9, 7, 5, 2, 0, -3, -4, -7, -9, -10]),
            (900, 999, [0,8, 6, 4, 1, -1, -3, -6, -8, -10, -11]),
            (1000, 1099, [0,6, 5, 3, 1, -2, -5, -6, -9, -11, -12]),
            (1100, 1199, [0,5, 4, 1, 0, -2, -6, -7, -10, -12, -13]),
            (1200, float("inf"), [0,5, 3, 0, -1, -2, -6, -8, -11, -12, -13]),
        ]

        for low, high, rank_trophies in trophy_ranges:
            if low <= trophies <= high:
                return rank_trophies
        return [0] * 10
    
    def getTrophiesBattleRoyaleTeam(trophies):
        TROPHY_RANGES = [
            (0, 49),
            (50, 99),
            (100, 199),
            (200, 299),
            (300, 399),
            (400, 499),
            (500, 599),
            (600, 699),
            (700, 799),
            (800, 899),
            (900, 999),
            (1000, 1099),
            (1100, 1199),
            (1200, float("inf")),
        ]

        RANK_VALUES = [
            [0,9, 7, 4, 0, 0],
            [0,9, 7, 4, 0, -1],
            [0,9, 7, 3, -1, -2],
            [0,9, 7, 2, -2, -3],
            [0,9, 7, 1, -3, -4],
            [0,9, 7, 0, -4, -5],
            [0,9, 7, 0, -5, -6],
            [0,9, 7, 0, -6, -8],
            [0,9, 7, 0, -7, -9],
            [0,7, 6, -1, -8, -9],
            [0,7, 6, -3, -8, -10],
            [0,5, 4, -4, -9, -11],
            [0,5, 4, -6, -10, -12],
            [0,4, 2, -6, -10, -12],
        ]


        for i, (low, high) in enumerate(TROPHY_RANGES):
            if low <= trophies <= high:
                return RANK_VALUES[i][trophies]
        return 0
        
    def getTrophiesBalance(trophies, result, gamemodeType):
        if gamemodeType == 1:
            return BattleEndManager.getTrophies(trophies)[result]
        elif gamemodeType == 2:
            return BattleEndManager.getTrophiesBattleRoyale(trophies)[result]
        elif gamemodeType == 5:
            return BattleEndManager.getTrophiesBattleRoyaleTeam(trophies)[result]
        else:
            return 0
        
    def getExperienceBalance(gamemodeType, result, time, tickets):
        if gamemodeType == 1:
            return [20,10,15][result]
        elif gamemodeType == 2:
            return [0,34,28,22,16,12,8,6,4,2,1,1][result]
        elif gamemodeType == 5:
            return [0,32,20,8,4,0][result]
        else:
            if time<=19:
                return 12*tickets
            else:
                increase = (time-20)/9+1
                return min(12+increase,32)
            
    def getTokensBalance(gamemodeType, result, time, tickets):
        if gamemodeType == 1:
            return [10,0,5][result]
        elif gamemodeType == 2:
            return [0,15,12,9,6,5,4,2,1,0,0,0][result]
        elif gamemodeType == 5:
            return [0,14,8,4,2,0]
        else:
            if time<=19:
                return 12*tickets
            else:
                increase = (time-20)/9+1
                return min(12+increase,32)*tickets
            
    def applyRewards(calling_instance, exp, tokens, trophies, legendaryTrophies, selectedBrawler, starTokens):
        if calling_instance.config.brawlPassEnabled:
            calling_instance.player.BrawlPassDatas[str(calling_instance.config.brawlPassSeason)]["Progress"]+=starTokens
            calling_instance.db.replaceValue("BrawlPassDatas",calling_instance.player.BrawlPassDatas, calling_instance.player)
        else:
            calling_instance.player.StarTokens+=starTokens
            calling_instance.db.replaceValue("StarTokens", calling_instance.player.StarTokens, calling_instance.player)
        calling_instance.player.Trophies += trophies
        calling_instance.db.replaceValue("Trophies", calling_instance.player.Trophies, calling_instance.player)
        if calling_instance.player.Trophies>calling_instance.player.HighestTrophies:
            calling_instance.player.HighestTrophies=calling_instance.player.Trophies
            calling_instance.db.replaceValue("HighestTrophies", calling_instance.player.HighestTrophies, calling_instance.player)
        calling_instance.player.OwnedBrawlers[selectedBrawler]["Trophies"]+=trophies
        if calling_instance.player.OwnedBrawlers[selectedBrawler]["Trophies"]>calling_instance.player.OwnedBrawlers[selectedBrawler]["HighestTrophies"]:
            calling_instance.player.OwnedBrawlers[selectedBrawler]["HighestTrophies"]=calling_instance.player.OwnedBrawlers[selectedBrawler]["Trophies"]
        calling_instance.db.replaceValue("OwnedBrawlers", calling_instance.player.OwnedBrawlers, calling_instance.player)
        calling_instance.player.Tokens += tokens
        calling_instance.db.replaceValue("Tokens", calling_instance.player.Tokens, calling_instance.player)
        calling_instance.player.Experience += exp+10
        calling_instance.db.replaceValue("Experience", calling_instance.player.Experience, calling_instance.player)
        calling_instance.player.LegendaryTrophies += legendaryTrophies
        calling_instance.db.replaceValue("LegendaryTrophies", calling_instance.player.LegendaryTrophies, calling_instance.player)
        calling_instance.player.TokensDoubler = max(calling_instance.player.TokensDoubler-tokens, 0)
        calling_instance.db.replaceValue("TokensDoubler", calling_instance.player.TokensDoubler, calling_instance.player)
        calling_instance.player.GainedRessources["Tokens"] = tokens
        calling_instance.player.GainedRessources["Trophies"] = trophies
        calling_instance.player.GainedRessources["StarTokens"] = starTokens
        calling_instance.player.GainedRessources["LegendaryTrophies"] = legendaryTrophies   
        


        
        
    
    
