from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters
from Classes.Packets.Server.Home.TeamMessage import TeamMessage

class LogicSelectCharacterCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.targetCharacter = []

    def encode(self):
        LogicCommand.encode(self)
        self.writeDataReference(self.targetCharacter)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.targetCharacter = calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        calling_instance.player.SelectedBrawler=self.targetCharacter[1]
        calling_instance.db.replaceValue("SelectedBrawler", self.targetCharacter[1], calling_instance.player)
        gadget = Cards.getBrawlerGadgets(self.targetCharacter[1])[0]
        starPower = Cards.getBrawlerStarpowers(self.targetCharacter[1])[0]
        calling_instance.player.TeamGadget = gadget
        calling_instance.player.TeamStarPower = starPower
        if calling_instance.player.TeamID[1] != 0:
            teamMessage = TeamMessage(b'')
            Messaging.sendMessage(teamMessage, calling_instance.client, cryptoInit, calling_instance)

    def getCommandType(self):
        return 525