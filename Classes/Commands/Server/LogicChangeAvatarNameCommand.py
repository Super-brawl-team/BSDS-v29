from Classes.Commands.LogicServerCommand import LogicServerCommand


class LogicChangeAvatarNameCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.name = ""

    def encode(self, player):
        self.writeString(self.name)
        self.writeVInt(0)
        LogicServerCommand.encode(self)
        return self.messagePayload

    def decode(self, calling_instance):
        self.name = calling_instance.readString()
        calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance)

    def getCommandType(self):
        return 201
    
    def setName(self, name):
        self.name = name