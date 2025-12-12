from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamCreateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        self.readVInt()
        fields["index"] = self.readVInt()
        fields["type"] = self.readVInt()
        super().decode(fields)

        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        calling_instance.player.TeamID = [0,1]
        Messaging.sendMessage(24124, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14350

    def getMessageVersion(self):
        return self.messageVersion