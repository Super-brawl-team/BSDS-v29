from Classes.Messaging import Messaging
from Classes.Files.Classes.Locations import Locations
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Packets.Server.Battle.BattleEndMessage import BattleEndMessage

class AskForBattleEndMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.result = 0
        self.rank = 0
        self.gamemode = 0
        self.heroes = []

    def encode(self):
        pass

    def decode(self):
        self.readVInt() # idk
        self.result = self.readVInt()
        self.rank = self.readVInt()
        mapID = self.readDataReference()
        self.gamemode = Locations.getGamemodeVariation(mapID[1])
        heroesCount = self.readVInt()
        for i in range(heroesCount):self.heroes.append({"Brawler": {"ID": self.readDataReference(), "SkinID": self.readDataReference(), "Trophies": 0, "PowerLevel": 1}, "Team": self.readVInt(), "IsPlayer": self.readBoolean(), "PlayerID": [0,0], "PlayerName": self.readString(), "LegendaryTrophies": 0})
        return self

    def execute(message, calling_instance, cryptoInit):
        calling_instance.player.OwnedBrawlers = {int(k): v for k, v in calling_instance.player.OwnedBrawlers.items()}
        message.heroes[0]["Brawler"]["Trophies"] = calling_instance.player.OwnedBrawlers[message.heroes[0]["Brawler"]["ID"][1]]["Trophies"]
        message.heroes[0]["Brawler"]["PowerLevel"] = calling_instance.player.OwnedBrawlers[message.heroes[0]["Brawler"]["ID"][1]]["PowerLevel"]
        message.heroes[0]["PlayerID"] = [*calling_instance.player.ID]
        message.heroes[0]["LegendaryTrophies"] = calling_instance.player.LegendaryTrophies
        battleEndMessage = BattleEndMessage(b'')
        battleEndMessage.setGamemode(message.gamemode)
        battleEndMessage.setHeroes(message.heroes)
        battleEndMessage.setRank(message.rank)
        battleEndMessage.setResult(message.result)
        Messaging.sendMessage(battleEndMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14110

    def getMessageVersion(self):
        return self.messageVersion
