from Classes.Packets.PiranhaMessage import PiranhaMessage


class AvailableServerCommandMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.command = None

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeVInt(self.command.getCommandType())
        self.messagePayload += self.command.encode(player)

    def decode(self):
        return {}

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24111

    def getMessageVersion(self):
        return self.messageVersion
    
    def setCommand(self, command):
        self.command = command