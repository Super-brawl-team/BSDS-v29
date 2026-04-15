from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.SeasonRewardsMessage import SeasonRewardsMessage
from Classes.Packets.Server.Home.DailyEventsMessage import DailyEventsMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class GetSeasonRewardsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.type = 0

    def encode(self):
        self.writeVInt(self.type)

    def decode(self):
        self.type = self.readVInt()
        return self

    def execute(message, calling_instance, cryptoInit):
        seasonRewardsMessage = SeasonRewardsMessage(b'')
        seasonRewardsMessage.setType(message.type)
        Messaging.sendMessage(seasonRewardsMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14277

    def getMessageVersion(self):
        return self.messageVersion