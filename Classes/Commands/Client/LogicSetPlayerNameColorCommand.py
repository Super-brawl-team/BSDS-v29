from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging

class LogicSetPlayerNameColorCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.targetNameColor = 0

    def encode(self):
        LogicCommand.encode(self)
        self.writeDataReference(self.targetNameColor)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.targetNameColor = calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        calling_instance.player.NameColor = self.targetNameColor[1]
        calling_instance.db.replaceValue("NameColor", self.targetNameColor[1], calling_instance.player)

    def getCommandType(self):
        return 527