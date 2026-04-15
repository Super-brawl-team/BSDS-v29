import json
import random
import string


class Player:
    ClientVersion = "0.0.0"
    GainedRessources = {}
    lastConnected=0
    ID = [0, 1]
    Registered = False
    Token = ""
    Name = "Brawler"
    Thumbnail = 0
    NameColor = 0
    ticketEventTime = 0
    bannedTimer = 0
    Region = "CAT"
    ContentCreator = "BSDS-v26"
    AllianceID = [0,1]
    TeamID = [0,0]
    selectedTickets = 0
    isInPowerPlay = False
    Coins = 0
    TokensLeft = 200
    InvitesBlocked = False
    ChatMuted = False
    AskAge = False
    DisableNotifs = False
    TeamStarPower = 0
    TeamGadget = 0
    LegendaryTrophies = 0
    SelectedStarPowers = {}
    SelectedGadgets = {}
    powerPlayGamesLeft = 3
    Gems = 0
    isInRealGame = False
    StarPoints = 0
    Trophies = 0
    HighestTrophies = 0
    Tickets = 0
    BrawlPassDatas = {"0": {"FreePassTier": 1, "PaidPassTier": 1, "Progress": 0, "PassPurchased": True}, "1": {"FreePassTier": 1, "PaidPassTier": 1, "Progress": 0, "PassPurchased": True}}
    Quests = {"0": {"Season": 1, "Type": 0, "Progress": 0, "Goal": 10, "Reward":1, "BrawlPassExclusive": False, "Seen": False, "Target": 0, "TargetGamemode": 0}}
    TrophyRoadTier = 1
    Experience = 0
    Level = 500
    Tokens = 0
    StarTokens = 0
    TokensDoubler = 1000
    
    SelectedMap = 0
    SelectedSkins = {}
    SelectedBrawler = 0
    OwnedThumbnails = []
    OwnedBrawlers = {
        0: {'CardID': 0, 'Skins': [29, 52], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2, 'Gadgets': [], 'StarPowers': []}
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 or lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawler': self.SelectedBrawler,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
        
    def fromJSON(self, jsonData):
        for key,data in jsonData.items():
            setattr(self, key, data)