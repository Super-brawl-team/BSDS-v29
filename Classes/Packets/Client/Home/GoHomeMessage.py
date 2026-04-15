from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class GoHomeMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeBoolean(False)
        pass

    def decode(self):
        self.readBoolean()
        return self

    def execute(message, calling_instance, cryptoInit):
        ownHomeDataMessage = OwnHomeDataMessage(b'')
        Messaging.sendMessage(ownHomeDataMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14101

    def getMessageVersion(self):
        return self.messageVersion