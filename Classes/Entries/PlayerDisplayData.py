class PlayerDisplayData:
    def __init__(self):
        self.player = None

    def encode(self, byteStream):
        byteStream.writeString(self.player.Name)# name
        byteStream.writeVInt(100) # unknown
        byteStream.writeVInt(28000000+self.player.Thumbnail)  #Player Profile Icon
        byteStream.writeVInt(43000000+self.player.NameColor)  #Player Name Color

    def decode(calling_instance, byteStream):
        calling_instance.player.Name = byteStream.readString()
        byteStream.readVInt()
        calling_instance.player.Thumbnail = 28000000-byteStream.readVInt()
        calling_instance.player.NameColor = 43000000-byteStream.readVInt()
        return calling_instance

    def setPlayer(self, player):
        self.player = player