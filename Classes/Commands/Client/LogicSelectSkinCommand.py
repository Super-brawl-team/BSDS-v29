from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Skins import Skins
from Classes.Packets.Server.Home.TeamMessage import TeamMessage

class LogicSelectSkinCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.targetSkin = []

    def encode(self):
        LogicCommand.encode(self)
        self.writeDataReference(self.targetSkin)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.targetSkin = calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        SelectedBrawler = Skins.getBrawlerBySkin(self.targetSkin[1])
        calling_instance.player.SelectedSkins[SelectedBrawler] = self.targetSkin[1]
        if calling_instance.player.TeamID[1] != 0:
            teamMessage = TeamMessage(b'')
            Messaging.sendMessage(teamMessage, calling_instance.client, cryptoInit, calling_instance)


    def getCommandType(self):
        return 506