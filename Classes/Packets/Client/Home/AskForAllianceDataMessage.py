from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.AllianceDataMessage import AllianceDataMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class AskForAllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.targetID = []

    def encode(self):
        pass

    def decode(self):
        self.targetID = self.readLong()
        if self.readBoolean():
            self.targetID = self.readLong()
        return self

    def execute(message, calling_instance, cryptoInit):
        allianceDataMessage = AllianceDataMessage(b'')
        allianceDataMessage.setTargetID(message.targetID)
        Messaging.sendMessage(allianceDataMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14302

    def getMessageVersion(self):
        return self.messageVersion