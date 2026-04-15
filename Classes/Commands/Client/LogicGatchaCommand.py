from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Milestones import Milestones
from Classes.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Logic.LogicHomeChangeListener import LogicHomeChangeListener
from Classes.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Classes.Entries.DeliveryUnit import DeliveryUnit
from Classes.Entries.GachaDrop import GachaDrop
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Characters import Characters

class LogicGatchaCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.boxID = 0

    def encode(self):
        LogicCommand.encode(self)
        self.writeVInt(self.boxID)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.boxID = calling_instance.readVInt()
        return self

    def execute(self, calling_instance, cryptoInit):
        if not self.canExecute(calling_instance):
            return
        availableServerCommandMessage = AvailableServerCommandMessage(b'')
        logicGiveDeliveryItemsCommand = LogicGiveDeliveryItemsCommand(b'')
        deliveryUnit = DeliveryUnit()
        chestType = self.getChestType(self.boxID)
        deliveryUnit.setType(chestType)
        gachaDrops = LogicHomeChangeListener.gacha(calling_instance.player, calling_instance.db, chestType)
        deliveryUnit.setGachaDrops(gachaDrops)
        logicGiveDeliveryItemsCommand.setDeliveryUnits([deliveryUnit])
        availableServerCommandMessage.setCommand(logicGiveDeliveryItemsCommand)
        Messaging.sendMessage(availableServerCommandMessage, calling_instance.client, cryptoInit, calling_instance)

    def getChestType(self, a2):
        result = 11
        if a2 != 3:
            result = 10
            if a2 == 1:
                result = 12
            if a2 == 4:
                return 12
        return result
    
    def canExecute(self, calling_instance):
        if self.boxID == 1:
            if calling_instance.player.Gems <= 50:
                return False
            calling_instance.player.Gems -= 50
            calling_instance.db.replaceValue("Gems", calling_instance.player.Gems, calling_instance.player)
        elif self.boxID == 3:
            if calling_instance.player.Gems <= 80:
                return False
            calling_instance.player.Gems -= 80
            calling_instance.db.replaceValue("Gems", calling_instance.player.Gems, calling_instance.player)
        elif self.boxID == 4 and not calling_instance.serverConnection.config.brawlPassEnabled:
            if calling_instance.player.StarTokens <= 10:
                return False
            calling_instance.player.StarTokens -= 10
            calling_instance.db.replaceValue("StarTokens", calling_instance.player.StarTokens, calling_instance.player)
        elif self.boxID == 5:
            if calling_instance.player.Tokens <= 100:
                return False
            calling_instance.player.Tokens -= 100
            calling_instance.db.replaceValue("Tokens", calling_instance.player.Tokens, calling_instance.player)
        else:
            return False
        return True

        

    def getCommandType(self):
        return 500