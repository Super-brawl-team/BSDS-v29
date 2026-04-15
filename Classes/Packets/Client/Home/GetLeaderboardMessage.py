from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.LeaderboardMessage import LeaderboardMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Instances.Classes.Alliance import Alliance


class GetLeaderboardMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.isLocal = False
        self.type = 0
        self.target = []
        self.season = 0

    def encode(self):
        self.writeBoolean(self.isLocal)
        self.writeVInt(self.type)
        self.writeDataReference(*self.target)
        self.writeVInt(self.season) # season?

    def decode(self):
        self.isLocal = self.readBoolean()
        self.type = self.readVInt()
        self.target = self.readDataReference()
        self.season = self.readVInt() # season ?
        return self

    def execute(message, calling_instance, cryptoInit):
        leaderboardMessage = LeaderboardMessage(b'')
        entries = []
        if message.type != 2:
            allPlayers = calling_instance.db.getAllPlayers()
            entries+= allPlayers
            if message.type == 0:
                for entry in entries:
                    entry.OwnedBrawlers = {int(k): v for k, v in entry.OwnedBrawlers.items()}
                entries = [entry for entry in entries if message.target[1] in entry.OwnedBrawlers]
                entries.sort(key = lambda entry : entry.OwnedBrawlers[message.target[1]]["Trophies"], reverse=True)
            elif message.type == 3:
                entries.sort(key = lambda entry : entry.LegendaryTrophies, reverse=True)
            else:
                entries.sort(key = lambda entry : entry.Trophies, reverse=True)
        else:
            entries.append(Alliance())
            entries.sort(key = lambda entry : entry.Trophies)
        leaderboardMessage.setIsLocal(message.isLocal)
        leaderboardMessage.setType(message.type)
        leaderboardMessage.setTarget(message.target)
        leaderboardMessage.setSeason(message.season)
        leaderboardMessage.setEntries(entries)
        Messaging.sendMessage(leaderboardMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14403

    def getMessageVersion(self):
        return self.messageVersion