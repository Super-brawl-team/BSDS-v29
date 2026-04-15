from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.name = ""
        self.nameSetByUser = False

    def encode(self):
        self.writeString(self.name)
        self.writeBoolean(self.nameSetByUser)

    def decode(self):
        self.name = self.readString()
        self.nameSetByUser = self.readBoolean()
        return self

    def execute(message, calling_instance, cryptoInit):
        calling_instance.player.Name = message.name
        calling_instance.player.Registered = True
        availableServerCommandMessage = AvailableServerCommandMessage(b'')
        logicChangeAvatarNameCommand = LogicChangeAvatarNameCommand(b'')
        logicChangeAvatarNameCommand.setName(message.name)
        availableServerCommandMessage.setCommand(logicChangeAvatarNameCommand)
        Messaging.sendMessage(availableServerCommandMessage, calling_instance.client, cryptoInit, calling_instance)
        calling_instance.db.createAccount(calling_instance.player)

    def getMessageType(self):
        return 10212

    def getMessageVersion(self):
        return self.messageVersion