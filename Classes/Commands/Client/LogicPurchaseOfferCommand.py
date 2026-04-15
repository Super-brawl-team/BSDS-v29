from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Packets.Server.Authentification.OutOfSyncMessage import OutOfSyncMessage

class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.offerIndex = 0

    def encode(self):
        LogicCommand.encode(self)
        self.writeVInt(self.offerIndex)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.offerIndex = calling_instance.readVInt()
        calling_instance.readDataReference()
        return self

    def execute(self, calling_instance, cryptoInit):
        if self.offerIndex == 0:
            outOfSyncMessage = OutOfSyncMessage(b'')
            Messaging.sendMessage(outOfSyncMessage, calling_instance.client, cryptoInit)

    def getCommandType(self):
        return 519