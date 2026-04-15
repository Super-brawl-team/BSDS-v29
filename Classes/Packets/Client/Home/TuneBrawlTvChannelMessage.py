from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.BrawlTvChannelNextUpMessage import BrawlTvChannelNextUpMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class TuneBrawlTvChannelMessage(PiranhaMessage):
    """Wanna have fun ? send instead BrawlTvChannelListMessage and it's going to spam the fuck out"""
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeVInt(4294967295)
        self.writeVInt(4294967295)

    def decode(self):
        print(self.readVInt()) # Huge ass fucking number for some reason (4294967295)
        print(self.readVInt()) # Same here
        return self

    def execute(message, calling_instance, cryptoInit):
        brawlTvChannelNextUpMessage = BrawlTvChannelNextUpMessage(b'')
        Messaging.sendMessage(brawlTvChannelNextUpMessage, calling_instance.client, cryptoInit)

    def getMessageType(self):
        return 14701

    def getMessageVersion(self):
        return self.messageVersion