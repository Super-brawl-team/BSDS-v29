from Classes.ByteStream import ByteStream

class ChronosFileEntry:
    def __init__(self):
        self.filePath = ""
        self.fileSHA = ""

    def encode(self, byteStream:ByteStream):
        byteStream.writeStringReference(self.filePath)
        byteStream.writeStringReference(self.fileSHA)

    def decode(calling_instance, byteStream:ByteStream):
        calling_instance.filePath = byteStream.readStringReference()
        calling_instance.fileSHA = byteStream.readStringReference()
        return calling_instance

    def setFilePath(self, filePath):
        self.filePath = filePath

    def setFileSHA(self, fileSHA):
        self.fileSHA = fileSHA