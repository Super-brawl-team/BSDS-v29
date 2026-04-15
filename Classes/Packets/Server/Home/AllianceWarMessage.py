from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceWarMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, calling_instance):
        player = calling_instance.player
        self.writeLong(0, 1) # Player ID
        self.writeVInt(1) # Your Club Faction
        

        # Club War Events Array
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(0)
            self.writeVInt(0) # Event Column Index
            self.writeVInt(0) # Event Row Index
            self.writeVInt(1) # Club Faction
            self.writeDataReference(15, 0) # War Location ID
            self.writeVInt(1) # War Node State
            self.writeVInt(0) # War Node State Time Left
            self.writeVInt(9) # Faction Score
            self.encodeIntList([]) 
        # Club War Events Array End
        

        # Club War Factions Array
        self.writeVInt(0) # Count
        for x in range(0):
            self.writeVInt(1) # Club Faction
            self.writeVInt(1) # Faction Score
        # Club War Factions Array End
        


    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24776

    def getMessageVersion(self):
        return self.messageVersion