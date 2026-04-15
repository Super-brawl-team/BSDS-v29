from Classes.Messaging import Messaging
from Classes.Packets.Server.Authentification.OutOfSyncMessage import OutOfSyncMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage


class StartGameMessage(PiranhaMessage):
    """Seriously supercell? This packet has same id as MatchmakeRequestMessage and use unused..."""
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self):
        self.writeInt(0)

    def decode(self):
        self.readInt()
        return self

    def execute(message, calling_instance, cryptoInit):
        outOfSyncMessage = OutOfSyncMessage(b'')
        Messaging.sendMessage(outOfSyncMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14103

    def getMessageVersion(self):
        return self.messageVersion
