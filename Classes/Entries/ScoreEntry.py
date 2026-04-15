class ScoreEntry:
    def __init__(self):
        self.brawler = 0
        self.brawlerTrophies = 0
        self.trophiesLost = 0
        self.gainedStarPoints = 0

    def encode(self, byteStream):
        byteStream.writeVInt(16000000+self.brawler) # brawler
        byteStream.writeVInt(self.brawlerTrophies) # brawler trophies
        byteStream.writeVInt(self.trophiesLost) # trophies lost
        byteStream.writeVInt(self.gainedStarPoints) # gained star points

    def decode(calling_instance, byteStream):
        calling_instance.brawler = byteStream.readVInt()-16000000
        calling_instance.brawlerTrophies = byteStream.readVInt()
        calling_instance.trophiesLost = byteStream.readVInt()
        calling_instance.gainedStarPoints = byteStream.readVInt()
        return calling_instance

    def setBrawler(self, brawler):
        self.brawler = brawler
        
    def setBrawlerTrophies(self, brawlerTrophies):
        self.brawlerTrophies = brawlerTrophies
        
    def setTrophiesLost(self, trophiesLost):
        self.trophiesLost = trophiesLost
        
    def setGainedStarPoints(self, gainedStarPoints):
        self.gainedStarPoints = gainedStarPoints