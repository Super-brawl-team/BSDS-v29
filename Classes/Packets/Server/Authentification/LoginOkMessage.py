from Classes.Packets.PiranhaMessage import PiranhaMessage

class LoginOkMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 1

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeLong(*player.ID)
        self.writeLong(*player.ID)
        self.writeString(player.Token)
        self.writeString()
        self.writeString()
        self.writeInt(26)
        self.writeInt(185)
        self.writeInt(1)
        self.writeString("dev")
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString("CAT")
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeInt(2)
        self.writeString('https://game-assets.brawlstarsgame.com')
        self.writeString('http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com')
        self.writeInt(2)
        self.writeString('https://event-assets.brawlstars.com')
        self.writeString('https://24b999e6da07674e22b0-8209975788a0f2469e68e84405ae4fcf.ssl.cf2.rackcdn.com/event-assets')
        self.writeVInt(0)
        self.writeCompressedString(b'')
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString('https://play.google.com/store/apps/details?id=com.supercell.brawlstars') # App Store Link
        self.writeString()
        self.writeBoolean(False)

        self.writeBoolean(False)
        if False:
            self.writeString()

        self.writeBoolean(False)
        if False:
            self.writeString()

        self.writeBoolean(False)
        if False:
            self.writeString()

        self.writeBoolean(False)
        if False:
            self.writeString()


    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 20104

    def getMessageVersion(self):
        return self.messageVersion