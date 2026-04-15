from Classes.Messaging import Messaging
from Classes.Packets.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class CancelMatchmakingMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        pass

    def decode(self):
        return self

    def execute(message, calling_instance, cryptoInit):
        matchMakingCancelledMessage = MatchMakingCancelledMessage(b'')
        Messaging.sendMessage(matchMakingCancelledMessage, calling_instance.client, cryptoInit)

    def getMessageType(self):
        return 14177

    def getMessageVersion(self):
        return self.messageVersion