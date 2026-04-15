from Classes.ByteStream import ByteStream

class ChronosTextEntry:
    def __init__(self):
        self.textType = 0
        self.textEntry = ""

    def encode(self, byteStream:ByteStream):
        byteStream.writeInt(self.textType)
        byteStream.writeStringReference(self.textEntry)

    def decode(calling_instance, byteStream:ByteStream):
        calling_instance.textType = byteStream.readInt()
        calling_instance.textEntry = byteStream.readStringReference()
        return calling_instance

    def setTexttype(self, textType):
        self.textType = textType

    def setTextEntry(self, textEntry):
        self.textEntry = textEntry