from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Commands.Server.LogicBrawlPassUnlockedCommand import LogicBrawlPassUnlockedCommand
from Classes.Commands.Server.LogicDiamondsAddedCommand import LogicDiamondsAddedCommand

class TeamChatMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.content = ""

    def encode(self):
        self.writeString(self.content)

    def decode(self):
        self.content = self.readString()
        return self

    def execute(message, calling_instance, cryptoInit):
        if message.content == "/buyPass":
            availableServerCommandMessage = AvailableServerCommandMessage(b'')
            logicBrawlPassUnlockedCommand = LogicBrawlPassUnlockedCommand(b'')
            availableServerCommandMessage.setCommand(logicBrawlPassUnlockedCommand)
            Messaging.sendMessage(availableServerCommandMessage, calling_instance.client, cryptoInit, calling_instance)
            availableServerCommandMessage = AvailableServerCommandMessage(b'')
            logicDiamondsAddedCommand = LogicDiamondsAddedCommand(b'')
            logicDiamondsAddedCommand.setIsActionFromDebug(True)
            logicDiamondsAddedCommand.setAddedDiamonds(-180)
            availableServerCommandMessage.setCommand(logicDiamondsAddedCommand)
            Messaging.sendMessage(availableServerCommandMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 14359

    def getMessageVersion(self):
        return self.messageVersion