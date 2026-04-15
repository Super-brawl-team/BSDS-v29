from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.TeamMessage import TeamMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Files.Classes.Cards import Cards

class TeamCreateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        self.readVInt() # index
        self.readVInt() # index
        self.readVInt() # type
        return self

    def execute(message, calling_instance, cryptoInit):
        gadget = Cards.getBrawlerGadgets(calling_instance.player.SelectedBrawler)[0]
        starPower = Cards.getBrawlerStarpowers(calling_instance.player.SelectedBrawler)[0]
        calling_instance.player.TeamGadget = gadget
        calling_instance.player.TeamStarPower = starPower
        calling_instance.player.TeamID = [0,1]
        teamMessage = TeamMessage(b'')
        Messaging.sendMessage(teamMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14350

    def getMessageVersion(self):
        return self.messageVersion