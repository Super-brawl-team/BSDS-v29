from Classes.Commands.LogicCommand import LogicCommand


class LogicServerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def addCommand(self):
        self.writeVInt(0)
        LogicCommand.encode(self)

    def decode(calling_instance):
        calling_instance.readVInt() # command ID
        return LogicCommand.decode(calling_instance)
