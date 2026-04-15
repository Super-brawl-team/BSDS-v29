from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.TeamLeftMessage import TeamLeftMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamLeaveMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        return self

    def execute(message, calling_instance, cryptoInit):
        teamLeftMessage = TeamLeftMessage(b'')
        Messaging.sendMessage(teamLeftMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14353

    def getMessageVersion(self):
        return self.messageVersion