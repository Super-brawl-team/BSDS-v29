from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Cards import Cards
from Classes.Packets.Server.Home.TeamMessage import TeamMessage

class LogicSelectStarPowerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.targetCard = []

    def encode(self):
        LogicCommand.encode(self)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.targetCard = calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        SelectedBrawler = Cards.getOwner(self.targetCard[1])
        if Cards.isStarPower(self.targetCard[1]):
            calling_instance.player.SelectedStarPowers[SelectedBrawler] = self.targetCard[1]
            if calling_instance.player.TeamID[1] != 0:
                calling_instance.player.TeamStarPower = self.targetCard[1]
        else:
            calling_instance.player.SelectedGadgets[SelectedBrawler] = self.targetCard[1]
            if calling_instance.player.TeamID[1] != 0:
                calling_instance.player.TeamGadget = self.targetCard[1]
        if calling_instance.player.TeamID[1] != 0:
            teamMessage = TeamMessage(b'')
            Messaging.sendMessage(teamMessage, calling_instance.client, cryptoInit, calling_instance)


    def getCommandType(self):
        return 529