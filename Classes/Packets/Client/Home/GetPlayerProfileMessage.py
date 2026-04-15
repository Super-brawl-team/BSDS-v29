from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class GetPlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.targetID = []

    def encode(self):
        self.writeLong(*self.targetID)

    def decode(self):
        self.targetID = self.readLong()
        return self

    def execute(message, calling_instance, cryptoInit):
        playerProfileMessage = PlayerProfileMessage(b'')
        playerProfileMessage.setTargetID(message.targetID)
        Messaging.sendMessage(playerProfileMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14113

    def getMessageVersion(self):
        return self.messageVersion