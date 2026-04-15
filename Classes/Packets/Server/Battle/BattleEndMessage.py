from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Managers.BattleEndManager import BattleEndManager

class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.result = 0
        self.rank = 0
        self.gamemode = 0
        self.heroes = []

    def encode(self, calling_instance):
        player = calling_instance.player
        time = int(player.ticketEventTime)-7
        gamemodetype = BattleEndMessage.getGameModeType(self.gamemode)
        starTokens = 0
        win = False
        completedQuest = False
        if player.isInPowerPlay:
            trophies = 0
            legendaryTrophies = BattleEndManager.getLegendaryTrophies(self.rank)
            player.powerPlayGamesLeft-=1
            calling_instance.db.replaceValue("powerPlayGamesLeft", player.powerPlayGamesLeft, player)
        else:
            trophies = BattleEndManager.getTrophiesBalance(self.heroes[0]["Brawler"]["Trophies"],self.rank,gamemodetype)
            legendaryTrophies = 0
            if gamemodetype == 1 and self.rank==0:
                starTokens += 1
                win=True
            elif gamemodetype == 2 and self.rank<=4:
                starTokens += 1
                win=True
            elif gamemodetype == 5 and self.rank<=2:
                starTokens+=1
                win=True
            elif gamemodetype in [3,4,6]:
                starTokens += 1
                win=True
        completed = []
        for index, Quest in player.Quests.items():
            if self.heroes[0]["Brawler"]["ID"][0] == Quest["Target"] or self.gamemode == Quest["TargetGamemode"]:
                starTokens+=1
                completedQuest=True
                Quest["Progress"]+=1
                if Quest["Progress"]>=Quest["Goal"]:
                    completed.append(index)
        for x in completed:
            player.Quests.pop(x)
        calling_instance.db.replaceValue("Quests", player.Quests, player)
        exp = BattleEndManager.getExperienceBalance(gamemodetype, self.rank,time, player.selectedTickets)
        tokens = BattleEndManager.getTokensBalance(gamemodetype, self.rank,time, player.selectedTickets)
        self.writeVInt(gamemodetype) # Battle End Game Mode (gametype)
        self.writeVInt(self.rank) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVInt(tokens)  # Tokens Gained
        self.writeVInt(trophies)  # Trophies Gained (NOTE: If you have any underdog trophy, dont orget to add it there otherwise bad things will happen)
        self.writeVInt(legendaryTrophies)  # PowerPlay points Gained
        self.writeVInt(tokens)  # Doubled Tokens
        self.writeVInt(0)  # Double  Tokens Event
        self.writeVInt(player.TokensDoubler) # Token Doubler Left
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Power Play Epic Score
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Unk
        self.writeVInt(0) # Coin Shower
        self.writeVInt(0) # Underdog Trophies 
        self.writeBoolean(win)  #  Star Token
        self.writeBoolean(False)  # Experience Exhausted
        self.writeBoolean(False)  # Tokens Exhausted
        self.writeBoolean(False)  #  IsTutorialFirstGame 
        self.writeBoolean(player.isInRealGame and not player.isInPowerPlay)  # GainsTrophies
        self.writeBoolean(False)  #  IsTutorialFirstGame
        self.writeBoolean(player.isInPowerPlay)  # isPowerPlay
        self.writeVInt(1) # Challenge related
        self.writeBoolean(True) # Useless
        self.writeBoolean(completedQuest) # Quest Completed
        
        self.writeVInt(len(self.heroes))
        for heroEntry in self.heroes:
            self.writeBoolean(heroEntry["IsPlayer"]) # Is Own Player
            self.writeBoolean(heroEntry["Team"] != self.heroes[0]["Team"]) # Team
            self.writeBoolean(heroEntry["IsPlayer"]) # Is Star Player
            self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
            self.writeVInt(heroEntry["Brawler"]["Trophies"])
            self.writeVInt(heroEntry["LegendaryTrophies"]) # Power Play Points Gained
            self.writeVInt(heroEntry["Brawler"]["PowerLevel"]) # Power Level
            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(*heroEntry["PlayerID"])
            self.writeString(heroEntry["PlayerName"])
            self.writeVInt(0)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
        # Player Entry Array End

        # Experience Entry Array
        self.writeVInt(2)  # Experience Reward Count
        self.writeVInt(0)  # Normal Experience ID
        self.writeVInt(exp)  # Normal Experience Gained
        self.writeVInt(8)  # Star Player Experience ID
        self.writeVInt(10)  # Star Player Experience Gained
        # Experience Entry Array End

        # Milestone Rewards Array
        self.writeVInt(0)  # Milestones Count
        for x in range(0):
            self.writeDataReference(49, x)  # Milestone Reward ID
        # Milestone Rewards Array End

        # Milestone Progress Array
        self.writeVInt(2)  # Milestone Progress Count
        self.writeVInt(1)  # Milestone ID
        self.writeVInt(self.heroes[0]["Brawler"]["Trophies"])  # Brawler Trophies
        self.writeVInt(player.OwnedBrawlers[self.heroes[0]["Brawler"]["ID"][1]]["HighestTrophies"])  # Brawler Highest Trophies
        self.writeVInt(5)  # Milestone ID
        self.writeVInt(player.Experience)  # Player Experience Points
        self.writeVInt(player.Experience)  # Player Highest Experience Points
        # Milestone Progress Array End
        self.writeDataReference(28, player.Thumbnail)
        self.writeBoolean(True)  # Play again Boolean
        if True:
            # Play again status 
            self.writeInt(6) # huh?
            self.writeVInt(3) # team 1 players
            for x in range(3):
                self.writeLong(0, x) # team 1 players id
            self.writeVInt(3) # team 2 players
            for x in range(3):
                self.writeLong(0, x) # team 2 players id
            self.writeInt(5) # huh?
            self.writeInt(4) # huh?
        self.writeBoolean(True) # Quest Array
        self.writeVInt(len(player.Quests))
        for index, x in player.Quests.items():
            """Thats a damn fucking lot of useless data"""
            self.writeVInt(index) # Possibly the quest index but whatever
            self.writeVInt(x["Season"]) # Season (Unused)
            self.writeVInt(x["Type"]) # Type (0: Brawlers, 1+: Gamemodes)
            self.writeVInt(x["Progress"]) # Progress
            self.writeVInt(x["Goal"]) # Goal
            self.writeVInt(x["Reward"]) # Reward (Unused)
            self.writeBoolean(x["BrawlPassExclusive"]) # IsBrawlPassExclusive (Unused)
            self.writeBoolean(x["Seen"]) # Seen (Unused)
            self.writeDataReference(16,x["Target"]) # Targetted Char
            self.writeVInt(x["TargetGamemode"]) # Targetted Gamemode
            self.writeVInt(1) # Progrress..? (Unused)
        player.isInRealGame = False
        player.isInPowerPlay = False
        BattleEndManager.applyRewards(calling_instance, exp, tokens, trophies, legendaryTrophies, self.heroes[0]["Brawler"]["ID"][1], starTokens)
        

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 23456

    def getMessageVersion(self):
        return self.messageVersion
    
    def getGameModeType(type):
        if type == 6 or type == 15 or type == 14:
            return 2
        elif type == 8:
            return 3
        elif type == 7:
            return 4
        elif type == 9:
            return 5
        elif type == 10 or type == 18:
            return 6
        else:
            return 1
        
    def setResult(self, result):
        self.result = result
        
    def setRank(self, rank):
        self.rank = rank
        
    def setGamemode(self, gamemode):
        self.gamemode = gamemode
        
    def setHeroes(self, heroes):
        self.heroes = heroes
    