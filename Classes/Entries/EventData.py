from Classes.ByteStream import ByteStream

class EventData:
    def __init__(self):
        self.index = 0
        self.timer = 0
        self.keys = 10
        self.location = 0
        self.gamesPlayed = 0
        self.gamesLeft=3
        self.modifiers = []
        self.difficulty = 0
        self.challengeType=0

    def encode(self, byteStream:ByteStream):
        byteStream.writeVInt(self.index) # Event Index
        byteStream.writeVInt(self.index)  # Event Index
        byteStream.writeVInt(self.timer)  # New Event Timer
        byteStream.writeVInt(self.timer)  # Event Timer
        byteStream.writeVInt(self.keys)  # New Event Keys
        byteStream.writeDataReference(15, self.location)  # Location ID
        byteStream.writeBoolean(True)  # Is Event Active
        byteStream.writeBoolean(True)  # Is Event New
        byteStream.writeString()  # Event Custom Entry
        byteStream.writeVInt(0)  # Event Tickets Amount
        byteStream.writeVInt(self.gamesPlayed) # Power Play Games Played
        byteStream.writeVInt(self.gamesLeft) # Power Play Games Left
        byteStream.writeVInt(len(self.modifiers)) # modifiers array
        for x in self.modifiers:
            byteStream.writeVInt(x)
        byteStream.writeVInt(self.difficulty) 
        byteStream.writeVInt(self.challengeType) # Championship type (0: esport, 1:psg)

    def decode(calling_instance, byteStream:ByteStream):
        calling_instance.index = byteStream.readVInt() # Event Index
        calling_instance.index = byteStream.readVInt()  # Event Index
        calling_instance.timer = byteStream.readVInt()  # New Event Timer
        calling_instance.timer = byteStream.readVInt(0)  # Event Timer
        calling_instance.keys = byteStream.readVInt()  # New Event Keys
        calling_instance.location = byteStream.readDataReference()[1]  # Location ID
        byteStream.readBoolean()  # Is Event Active
        byteStream.readBoolean()  # Is Event New
        byteStream.readString()  # Event Custom Entry
        byteStream.readVInt()  # Event Tickets Amount
        calling_instance.gamesPlayed = byteStream.readVInt() # Power Play Games Played
        calling_instance.gamesLeft = byteStream.readVInt() # Power Play Games Left
        for x in range(byteStream.readVInt()):
            calling_instance.modifiers.append(byteStream.readVInt())
        calling_instance.difficulty = byteStream.readVInt() 
        calling_instance.challengeType = byteStream.readVInt() # Championship type (0: esport, 1:psg)
        return calling_instance

    def setIndex(self, index):
        self.index = index
        
    def setTimer(self, timer):
        self.timer = timer
        
    def setKeys(self, keys):
        self.keys = keys
        
    def setLocation(self, location):
        self.location = location
        
    def setGamesPlayed(self, gamesPlayed):
        self.gamesPlayed = gamesPlayed
        
    def setGamesLeft(self, gamesLeft):
        self.gamesLeft = gamesLeft
        
    def addModifier(self, modifier):
        self.modifiers.append(modifier)
        
    def increaseDifficulty(self):
        self.difficulty+=1
        
    def setChallengeType(self, type):
        self.challengeType = type