from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.TeamMessage import TeamMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamSetLocationMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.targetLocation = []

    def encode(self):
        pass

    def decode(self):
        self.targetLocation = self.readDataReference()
        return self

    def execute(message, calling_instance, cryptoInit):
        calling_instance.player.SelectedMap = message.targetLocation[1]
        teamMessage = TeamMessage(b'')
        Messaging.sendMessage(teamMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14363

    def getMessageVersion(self):
        return self.messageVersion