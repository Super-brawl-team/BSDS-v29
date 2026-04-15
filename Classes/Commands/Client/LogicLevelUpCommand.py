from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters
from Classes.Packets.Server.Home.TeamMessage import TeamMessage

class LogicLevelUpCommand(LogicCommand):
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
        calling_instance.player.OwnedBrawlers = {int(k): v for k, v in calling_instance.player.OwnedBrawlers.items()}
        prices = [20, 35, 75, 140, 290, 480, 800, 1250]
        if calling_instance.player.OwnedBrawlers[self.targetCharacter[1]]["PowerLevel"] <9:
            calling_instance.player.Coins-=prices[calling_instance.player.OwnedBrawlers[self.targetCharacter[1]]["PowerLevel"]-1]
            calling_instance.player.OwnedBrawlers[self.targetCharacter[1]]["PowerLevel"]+=1
            calling_instance.db.replaceValue("OwnedBrawlers", calling_instance.player.OwnedBrawlers, calling_instance.player)
            calling_instance.db.replaceValue("Coins", calling_instance.player.Coins, calling_instance.player)

    def getCommandType(self):
        return 520