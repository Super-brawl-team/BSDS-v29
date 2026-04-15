from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.BrawlTvChannelListMessage import BrawlTvChannelListMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class ListBrawlTvChannelsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeVInt(4294967295)
        self.writeBoolean(False)

    def decode(self):
        print(self.readVInt()) # Huge ass fucking number for some reason (4294967295)
        print(self.readBoolean())
        return self

    def execute(message, calling_instance, cryptoInit):
        brawlTvChannelListMessage = BrawlTvChannelListMessage(b'')
        Messaging.sendMessage(brawlTvChannelListMessage, calling_instance.client, cryptoInit)

    def getMessageType(self):
        return 14700

    def getMessageVersion(self):
        return self.messageVersion