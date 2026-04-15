from Classes.Packets.PiranhaMessage import PiranhaMessage


class DailyEventsMessage(PiranhaMessage):
    """OK WHAT THE FUCK SUPERCELL why it has the same id as SeasonRewardsMessage (is this thing used)"""
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.type = 0

    def encode(self, calling_instance):
        self.writeVInt(self.type) # type
        self.writeVInt(1) # challenge type I guess
        self.writeVInt(3)
        for x in range(3):
            self.writeVInt(20+x) # Event Index
            self.writeVInt(20+x)  # Event Index
            self.writeVInt(0)  # New Event Timer
            self.writeVInt(0)  # Event Timer
            self.writeVInt(10)  # New Event Keys
            self.writeDataReference(15, 0)  # Location ID
            self.writeBoolean(True)  # Is Event Active
            self.writeBoolean(True)  # Is Event New
            self.writeString()  # Event Custom Entry
            self.writeVInt(0)  # Event Tickets Amount
            self.writeVInt(0) # Power Play Games Played
            self.writeVInt(3) # Power Play Games Left
            modifiers = [] #1,2,3,5]*50 + [4]*3
            self.writeVInt(len(modifiers)) # modifiers array
            for x in modifiers:
                self.writeVInt(x)
            self.writeVInt(0) 
            self.writeVInt(1) # Championship type (0: esport, 1:psg)
        

    def decode(self):
        self.type = self.readVInt()
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24123

    def getMessageVersion(self):
        return self.messageVersion
    
    def setType(self, type):
        self.type = type