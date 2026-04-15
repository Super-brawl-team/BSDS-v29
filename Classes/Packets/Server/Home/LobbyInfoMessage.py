from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeVInt(ClientsManager.GetCount())
        self.writeString("Project BSDS \n"f"Version: {player.ClientVersion}")
        self.writeVInt(0)

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion