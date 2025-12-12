from Classes.Packets.PiranhaMessage import PiranhaMessage

class BattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(BattleEndMessage.getGameModeType(fields["GameMode"])) # Battle End Game Mode (gametype)
        print("GameMode Type:", BattleEndMessage.getGameModeType(fields["GameMode"]))
        self.writeVInt(fields["Rank"]) # Result (Victory/Defeat/Draw/Rank Score)
        self.writeVInt(0)  # Coins Gained (?)
        self.writeVInt(0)  # Event Total Coins (if the 1st coins vint is>= total coins, then "all coins collected")
        self.writeVInt(0)  # First Win Coins Gained
        self.writeVInt(0)  # Battle Result
        self.writeVInt(0)  # Trophies Result
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeBoolean(False)  # Matchmaking Battle End
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeBoolean(False)  # Tutorial Battle End
        self.writeVInt(-1)
        self.writeBoolean(False)
        
        self.writeVInt(fields["HeroesCount"])
        for heroEntry in fields["Heroes"]:
            self.writeBoolean(heroEntry["IsPlayer"]) # Is Own Player
            self.writeBoolean(heroEntry["Team"] != fields["Heroes"][0]["Team"]) # Team
            self.writeBoolean(heroEntry["IsPlayer"]) # Is Star Player
            self.writeDataReference(heroEntry["Brawler"]["ID"][0], heroEntry["Brawler"]["ID"][1])
            self.writeDataReference(heroEntry["Brawler"]["SkinID"][0], heroEntry["Brawler"]["SkinID"][1])
            self.writeVInt(1250)
            self.writeVInt(0) # Power Play Points Gained
            self.writeVInt(10) # Power Level
            self.writeBoolean(heroEntry["IsPlayer"])
            if heroEntry["IsPlayer"]:
                self.writeLong(player.ID[0], player.ID[1])
            self.writeString(heroEntry["PlayerName"])
            self.writeVInt(0)
            self.writeVInt(28000000)
            self.writeVInt(43000000) # Name
            self.writeVInt(0) # Unknown
        # Player Entry Array End

        # Experience Entry Array
        self.writeVInt(2)  # Experience Reward Count
        self.writeVInt(0)  # Normal Experience ID
        self.writeVInt(0)  # Normal Experience Gained
        self.writeVInt(8)  # Star Player Experience ID
        self.writeVInt(0)  # Star Player Experience Gained
        # Experience Entry Array End

        # Milestone Rewards Array
        self.writeVInt(0)  # Milestones Count
        # Milestone Rewards Array End

        # Milestone Progress Array
        self.writeVInt(2)  # Milestone Progress Count
        self.writeVInt(1)  # Milestone ID
        self.writeVInt(0)  # Brawler Trophies
        self.writeVInt(0)  # Brawler Highest Trophies
        self.writeVInt(5)  # Milestone ID
        self.writeVInt(0)  # Player Experience Points
        self.writeVInt(0)  # Player Experience Points
        # Milestone Progress Array End
        self.writeDataReference(28, 0)
        self.writeBoolean(True)  # Play again Boolean
        if True:
            # Play again status 
            self.writeInt(0) # huh?
            self.writeVInt(3) # team 1 players
            for x in range(3):
                self.writeLong(0, x) # team 1 players id
            self.writeVInt(3) # team 2 players
            for x in range(3):
                self.writeLong(0, x) # team 2 players id
            self.writeInt(0) # huh?
            self.writeInt(0) # huh?
        self.writeBoolean(False)  # quests

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
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
    