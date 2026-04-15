from Classes.Logic.LogicCommandManager import LogicCommandManager

from Classes.Packets.PiranhaMessage import PiranhaMessage


class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.commands = []

    def encode(self):
        pass

    def decode(self):
        self.readBoolean()
        self.readVInt() # tick
        self.readVInt() # checksum
        for i in range(self.readVInt()):
            self.commands.append({"ID": self.readVInt()})
            if LogicCommandManager.commandExist(self.commands[i]["ID"]):
                command = LogicCommandManager.createCommand(self.commands[i]["ID"])
                print("Command", LogicCommandManager.getCommandsName(self.commands[i]["ID"]))
                if command is not None:
                    command.decode(self)
                    self.commands[i]["Instance"] = command
        return self

    def execute(message, calling_instance, cryptoInit):
        for command in message.commands:
            if "Instance" not in command.keys():
                return

            if hasattr(command["Instance"], 'execute'):
                command["Instance"].execute(calling_instance, cryptoInit)

    def getMessageType(self):
        return 14102

    def getMessageVersion(self):
        return self.messageVersion