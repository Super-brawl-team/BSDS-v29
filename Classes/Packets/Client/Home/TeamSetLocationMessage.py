from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamSetLocationMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["location"] = self.readDataReference()
        super().decode(fields)

        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        calling_instance.player.SelectedMap = fields["location"][1]
        Messaging.sendMessage(24124, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14363

    def getMessageVersion(self):
        return self.messageVersion