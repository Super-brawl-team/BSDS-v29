from Classes.ByteStream import ByteStream
from Classes.Entries.GachaDrop import GachaDrop

class DeliveryUnit:
    def __init__(self):
        self.type = 100
        self.gachaDrops = []

    def encode(self, byteStream : ByteStream):
        byteStream.writeVInt(self.type)
        byteStream.writeVInt(len(self.gachaDrops))
        for gachaDrop in self.gachaDrops:
            gachaDrop.encode(byteStream)

    def decode(calling_instance, byteStream : ByteStream):
        calling_instance.type = byteStream.readVInt()
        calling_instance.gachaDrops = []
        for x in range(byteStream.readVInt()):
            gachaDrop = GachaDrop()
            gachaDrop.decode(byteStream)
            calling_instance.gachaDrops.append(gachaDrop)
        return calling_instance

    def setType(self, type):
        self.type = type

    def setGachaDrops(self, gachaDrops):
        self.gachaDrops = gachaDrops