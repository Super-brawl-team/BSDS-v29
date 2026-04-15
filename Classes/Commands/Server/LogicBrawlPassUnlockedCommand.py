from Classes.Commands.LogicServerCommand import LogicServerCommand

class LogicBrawlPassUnlockedCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, player):
        self.writeVInt(1) # Season
        LogicServerCommand.encode(self)
        return self.messagePayload

    def decode(self, calling_instance):
        calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance)

    def getCommandType(self):
        return 219
    