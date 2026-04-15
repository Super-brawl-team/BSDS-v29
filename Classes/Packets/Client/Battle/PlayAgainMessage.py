from Classes.Messaging import Messaging
from Classes.Packets.Server.Battle.PlayAgainStatusMessage import PlayAgainStatusMessage
from Classes.Packets.Server.Battle.MatchMakingStatusMessage import MatchMakingStatusMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class PlayAgainMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeBoolean(False)

    def decode(self):
        self.readBoolean()
        return self

    def execute(message, calling_instance, cryptoInit):
        playAgainStatusMessage = PlayAgainStatusMessage(b'')
        Messaging.sendMessage(playAgainStatusMessage, calling_instance.client, cryptoInit)
        

    def getMessageType(self):
        return 14177

    def getMessageVersion(self):
        return self.messageVersion