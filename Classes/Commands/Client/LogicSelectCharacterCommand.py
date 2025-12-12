from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging

class LogicSelectCharacterCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["TargetCharacter"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        calling_instance.player.SelectedBrawler=fields["TargetCharacter"][1]
        if calling_instance.player.TeamID[1] != 0:
            Messaging.sendMessage(24124, {"Socket": calling_instance.client}, cryptoInit, calling_instance.player)

    def getCommandType(self):
        return 525