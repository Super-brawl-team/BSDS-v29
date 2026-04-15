from Classes.ByteStream import ByteStream


class LogicCommand(ByteStream):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.messageBuffer = commandData
        self.messagePayload = commandData

    def encode(self):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVLong(0, 0)

    def decode(calling_instance):
        calling_instance.readVInt() #TickWhenGiven
        calling_instance.readVInt() #ExecuteTick
        calling_instance.readVLong() #ExecutorAccountID
        return calling_instance
