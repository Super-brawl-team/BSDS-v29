from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Cards import Cards
class LogicSelectStarPowerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["TargetCard"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        SelectedBrawler = Cards.getOwner(fields["TargetCard"][1])
        print(calling_instance.player.TeamID)
        if Cards.isStarPower(fields["TargetCard"][1]):
            calling_instance.player.SelectedStarPowers[SelectedBrawler] = fields["TargetCard"][1]
            if calling_instance.player.TeamID[1] != 0:
                calling_instance.player.TeamStarPower = fields["TargetCard"][1]
        else:
            calling_instance.player.SelectedGadgets[SelectedBrawler] = fields["TargetCard"][1]
            if calling_instance.player.TeamID[1] != 0:
                calling_instance.player.TeamGadget = fields["TargetCard"][1]
        if calling_instance.player.TeamID[1] != 0:
            Messaging.sendMessage(24124, {"Socket": calling_instance.client}, cryptoInit, calling_instance.player)

    def getCommandType(self):
        return 529