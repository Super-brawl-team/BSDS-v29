from Classes.ByteStream import ByteStream


class GachaDrop:
    def __init__(self):
        self.amount = 0
        self.characterDataReference = [0,-1]
        self.type = 7
        self.skinDataReference = [0,-1]
        self.extraDataRefence = [0,-1]

    def encode(self, byteStream):
        byteStream.writeVInt(self.amount)
        byteStream.writeDataReference(self.characterDataReference[0], self.characterDataReference[1])
        byteStream.writeVInt(self.type)
        byteStream.writeDataReference(self.skinDataReference[0], self.skinDataReference[1])
        byteStream.writeDataReference(self.extraDataRefence[0], self.extraDataRefence[1])
        byteStream.writeVInt(0) # i fuckin dont know

    def decode(calling_instance, byteStream):
        calling_instance.amount = byteStream.readVInt()
        calling_instance.characterDataReference = byteStream.readDataReference()
        calling_instance.type = byteStream.readVInt()
        calling_instance.skinDataReference = byteStream.readDataReference()
        calling_instance.extraDataRefence = byteStream.readDataReference()
        byteStream.readVInt() # i fuckin dont know
        return calling_instance

    def setAmount(self, amount):
        self.amount = amount
        
    def getAmount(self):
        return self.amount

    def setCharacterDataReference(self, characterDataReference):
        self.characterDataReference = characterDataReference

    def setType(self, type):
        self.type = type

    def setSkinDataReference(self, skinDataReference):
        self.skinDataReference = skinDataReference

    def setExtraDataRefence(self, extraDataRefence):
        self.extraDataRefence = extraDataRefence