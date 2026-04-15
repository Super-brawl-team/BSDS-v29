from random import choice
from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Entries.ChronosTextEntry import ChronosTextEntry
from Classes.Entries.ChronosFileEntry import ChronosFileEntry
from Classes.Logic.URLBuilder import URLBuilder
from Classes.Files.Classes.Locations import Locations
from Classes.Notifications.BaseNotification import BaseNotification

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, calling_instance):
        player = calling_instance.player
        config = calling_instance.config
        brawlers = player.OwnedBrawlers
        skins = []
        for x in brawlers.values():
            skins+=x["Skins"]
        gadgets = []
        for x in brawlers.values():
            gadgets+=x["Gadgets"]
        starPowers = []
        for x in brawlers.values():
            starPowers+=x["StarPowers"]
        self.writeVInt(2018 * 1000 + 0)  # Current Year and Day
        self.writeVInt(6974)  # Time Remaining For Next Day
        self.writeVInt(player.Trophies)  # Player Trophies
        self.writeVInt(player.HighestTrophies)  # Player Highest Trophies
        self.writeVInt(player.TrophyRoadTier)  # Player Reached Ranking Trophies
        self.writeVInt(player.TrophyRoadTier)  # trophy road collected
        self.writeVInt(player.Experience)  # Player Experience Points
        self.writeDataReference(28, player.Thumbnail)  # Player Profile Icon
        self.writeDataReference(43, player.NameColor)  # Player Name Color

        # Played Game Modes Array
        self.writeVInt(20)  # Game Modes Count
        for x in range(20):
            self.writeVInt(x)  # Played Game Mode
        # Played Game Modes Array End

        # Selected Skins Array
        self.writeVInt(len(player.SelectedSkins))  # Skins Count
        for x in player.SelectedSkins.values():
            self.writeDataReference(29, x)  # Selected Skin
        
            
        
        # Selected Skins Array End

        # Unlocked Skins Array
        self.writeVInt(len(skins))  # Skins Count
        for x in skins:
            self.writeDataReference(29, x)  # Unlocked Skin
        # Unlocked Skins Array End
        
        self.writeVInt(0) # New tag

        for x in range(0):
            self.writeDataReference(23, x) # Cards.sv: works, Skins.csv: doesn't show but there is the "new" thingy in brawlers

        
        self.writeVInt(0) # Leaderboard Region
        self.writeVInt(player.HighestTrophies) # today's highest trophies
        self.writeVInt(0) # used tokens
        self.writeBoolean(False)  # Daily Band Created
        self.writeVInt(0)  # Remaining Token Doubler
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)  # Tokens Doubler
        self.writeVInt(52) 
        self.writeVInt(53)
        self.writeVInt(660)  # Brawl Pass Season Timer
        # Forced Drops Entry
        self.writeVInt(0)  # Unknown
        self.writeVInt(0)  # Unknown
        self.writeVInt(0)  # Unknown array
        for x in range(0):
            self.writeVInt(0)
        # Forced Drops Entry End
        self.writeBoolean(True)
        self.writeBoolean(False)  # Timed Offer Array
        self.writeBoolean(False) # Timed Offer Array 2
        self.writeBoolean(True) # Token Doubler
        self.writeVInt(2) # Related To Shop Token Doubler
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(0) # Name Change Cost
        self.writeVInt(0) # Name Change Timer
        self.writeVInt(1) # Shop Offers Array
        for x in range(1):
            self.writeVInt(1) # Gem Offers Array
            for y in range(1):
                self.writeVInt(1)  # Offer Item ID (0: FREE BOX, 1: COINS, 2: Random Brawler, 3: NEW BRAWLER, 4: NEW SKIN, 5: STAR POWER, 6: BRAWL BOX, 7: TICKETS, 8: POWER POINTS, 9: TOKEN DOUBLER, 10: MEGA BOX, 11: crash (keys?), 12: POWER POINTS (on any brawler), 13: crash (event slot?), 14: BIG BOX, 15: BRAWL BOX, 16: GEMS, 17+: crash (end of ids))
                self.writeVInt(1)  # Offer Amount
                self.writeDataReference(0, 0)  # Offer Data Reference
                self.writeVInt(0)  # Offer Skin ID / Rarity
            self.writeVInt(0)  # Offer Type (0: gems, 1: coins, 2: watch an ad, 3+: nothing)
            self.writeVInt(0)  # Offer Cost (if you set to 0 it will be free no matter what currency u put)
            self.writeVInt(0)  # Offer Timer
            self.writeVInt(1)
            self.writeVInt(1)   
            self.writeBoolean(False)  # Offer Purchased
            self.writeVInt(1) # new vint
            self.writeBoolean(False)  # Offer Daily
            self.writeVInt(0)  # Offer Cost Before Reduction
            chronosTextEntry = ChronosTextEntry()
            chronosTextEntry.setTextEntry("HII")
            chronosTextEntry.encode(self)  # Offer Title text
            self.writeBoolean(False)  # Offer Is Seen
            self.writeStringReference("offer_legendary")  # Offer Background Image
            self.writeVInt(0)
            self.writeBoolean(False)
        self.writeVInt(0) # array
        self.writeVInt(player.TokensLeft) # Battle Tokens
        self.writeVInt(660) # Time Till Next Battle Token
        self.writeVInt(0) # array
        self.writeVInt(player.Tickets) # Tickets
        self.writeVInt(51)
        self.writeDataReference(16,player.SelectedBrawler) # selected brawler
        self.writeString(player.Region) # Location
        self.writeString(player.ContentCreator) # Supporter Creator Code
        
        self.writeVInt(8) # Int Value Entry
        # TODO
        self.writeInt(3)
        self.writeInt(player.GainedRessources.get("Tokens", 0)) # Tokens Rewarded
        
        self.writeInt(4)
        self.writeInt(player.GainedRessources.get("Trophies", 0)) # Trophies Rewarded
        
        self.writeInt(5)
        self.writeInt(player.GainedRessources.get("StarTokens", 0)) # Star tokens rewarded
        
        self.writeInt(6)
        self.writeInt(int(player.DisableNotifs)) # disable notifs
        
        self.writeInt(7)
        self.writeInt(int(player.InvitesBlocked)) # Do Not Disturb
        
        self.writeInt(8)
        self.writeInt(player.GainedRessources.get("StarPoints", 0)) # Star Points Rewarded
        
        self.writeInt(10)
        self.writeInt(player.GainedRessources.get("LegendaryTrophies", 0)) # Power Play Trophies Rewarded
        
        self.writeInt(15)
        self.writeInt(int(player.AskAge)) # ask the age
        
        player.GainedRessources = {}
        
        self.writeVInt(0) # CoolDown Entry
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(16, 0)
            self.writeVInt(0)
        
        self.writeVInt(len(player.BrawlPassDatas)) # BP
        for index, x in player.BrawlPassDatas.items():
            self.writeVInt(index) # season ID
            self.writeVInt(x["Progress"]) # season progress
            self.writeVInt(x["PaidPassTier"]) # paid pass rewards claimed
            self.writeVInt(x["FreePassTier"]) # rewards claimed (if 0 or less collecting a reward crashes the game)
            self.writeBoolean(x["PassPurchased"]) # has brawl pass
            
        self.writeVInt(1) # ProLeagueSeasonData Array
        for x in range(1):
            self.writeVInt(1) # season
            self.writeVInt(player.LegendaryTrophies) # Points
            
        self.writeBoolean(True) # Quest Array
        self.writeVInt(len(player.Quests))
        for index, x in player.Quests.items():
            """Thats a damn fucking lot of useless data"""
            self.writeVInt(index) # Possibly the quest index but whatever
            self.writeVInt(x["Season"]) # Season (Unused)
            self.writeVInt(x["Type"]) # Type (0: Brawlers, 1+: Gamemodes)
            self.writeVInt(x["Progress"]) # Progress
            self.writeVInt(x["Goal"]) # Goal
            self.writeVInt(x["Reward"]) # Reward (Unused)
            self.writeBoolean(x["BrawlPassExclusive"]) # IsBrawlPassExclusive (Unused)
            self.writeBoolean(x["Seen"]) # Seen (Unused)
            self.writeDataReference(16,x["Target"]) # Targetted Char
            self.writeVInt(x["TargetGamemode"]) # Targetted Gamemode
            self.writeVInt(1) # Progrress..? (Unused)
            
        # Shop Offers Array End
        # Logic Daily Data End

        # Logic Conf Data
        self.writeVInt(2018 * 1000 + 0)  # Shop Current Year and Day
        self.writeVInt(100)  # Brawl Box Keys
        self.writeVInt(10)  # Shop Brawl Box Cost
        self.writeVInt(50)  # Shop Big Box Cost
        self.writeVInt(10)  # Shop Big Box Multipler
        self.writeVInt(80)  # Shop Mega Box Cost
        self.writeVInt(1000)  # Key Doubler Ammount
        self.writeVInt(40)  # Coins Doubler Cost
        self.writeVInt(1000)  # Coins Doubler Amount
        self.writeVInt(999900)  # Key Limit Amount
        self.writeVInt(180)
        self.writeVInt(190)
        ByteStreamHelper.encodeIntList(self, [0, 30, 80, 170, 350, 0])  # Boxes With Guaranteed Brawlers Cost

        # Event Slots Array
        self.writeVInt(23)  # Event Slots Count (1 : gem grab, 2: showdown, 3: daily events, 4: team events, 5: duo showdown, 6: team events, 7: special events, 8: solo events, 9: power play, 21: challenge)
        for x in range(23):
            self.writeVInt(x + 1)  # Event Index
        # Event Slots Array End

        # Logic Events Array
        EventLocations = {"1": choice(Locations.getAllMapsWithGamemodes([0])), "2": choice(Locations.getAllMapsWithGamemodes([6])), "3": choice(Locations.getAllMapsWithGamemodes([2,3])), "5": choice(Locations.getAllMapsWithGamemodes([9])), "4": choice(Locations.getAllMapsWithGamemodes([5,11,14,15,0])), "6":choice(Locations.getAllMapsWithGamemodes([7,10])), "9": choice(Locations.getAllMapsWithGamemodes([2,3,5,11,14,15,0])), "20": 52, "21":132, "22":132}
        self.writeVInt(len(EventLocations))  # Event Slots Count
        for index, EventLocation in EventLocations.items():
            self.writeVInt(int(index)) # Event Index
            self.writeVInt(int(index))  # Event Index
            self.writeVInt(0)  # New Event Timer
            self.writeVInt(0)  # Event Timer
            self.writeVInt(10)  # New Event Keys
            self.writeDataReference(15, EventLocation)  # Location ID
            self.writeBoolean(True)  # Is Event Active
            self.writeBoolean(True)  # Is Event New
            self.writeString()  # Event Custom Entry
            self.writeVInt(0)  # Event Tickets Amount
            self.writeVInt(0) # Power Play Games Played
            self.writeVInt(player.powerPlayGamesLeft) # Power Play Games Left
            modifiers = [] #1,2,3,5]*50 + [4]*3
            self.writeVInt(len(modifiers)) # modifiers array
            for x in modifiers:
                self.writeVInt(x)
            self.writeVInt(0) 
            self.writeVInt(1) # Championship type (0: esport, 1:psg)
        # Logic Events Array End

        # Coming Up Events Array
        EventLocation = []
        self.writeVInt(len(EventLocation))  # Event Slots Count
        for x in range(len(EventLocation)):
            self.writeVInt(0) # Event Index
            self.writeVInt(x + 1)  # Event Index
            self.writeVInt(0)  # New Event Timer
            self.writeVInt(0)  # Event Timer
            self.writeVInt(10)  # New Event Keys
            self.writeDataReference(15, x)  # Location ID
            self.writeBoolean(False)  # Is Event Active
            self.writeBoolean(False)  # Is Event New
            self.writeString()  # Event Custom Entry
            self.writeVInt(0)  # Event Tickets Amount
            self.writeVInt(0) # Power Play Games Played
            self.writeVInt(player.powerPlayGamesLeft) # Power Play Games Left
            modifiers = []#[1,2,3,5]*50 + [4]*3
            self.writeVInt(len(modifiers)) # modifiers array
            for x in modifiers:
                self.writeVInt(x)
            self.writeVInt(0) 
            self.writeVInt(0)
        # Coming Up Events Array End

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250])  # Brawler Coins Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [1, 2, 3, 4, 5, 10, 15, 20])  # Tickets Prices
        ByteStreamHelper.encodeIntList(self, [10, 30, 80])  # Event Tickets Cost
        ByteStreamHelper.encodeIntList(self, [6, 20, 60])  # Event Tickets Amount
        ByteStreamHelper.encodeIntList(self, [20, 50, 140])  # Coin Packs Cost
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200])  # Coin Packs Amount

        self.writeVInt(2)  # ?
        
        self.writeVInt(200)  # Max Battle Tokens
        self.writeVInt(20)  # Battle Tokens Refresh Amount
        self.writeVInt(690)  # ?
        self.writeVInt(10)  # ?
        self.writeVInt(5)  # ?
        self.writeBoolean(config.unlockedAllEvents) # enable all event slots (no need trophy road)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        self.writeVInt(100)  # ?
        self.writeVInt(10000)  # ?
        self.writeBoolean(True) # Boxes Enabled In Shop
        
        self.writeVInt(0)  # Cooldown entry
        self.writeVInt(25)  # IntValue Entry
        self.writeInt(1)
        self.writeInt(41000000 + config.currentTheme) # Theme ID
        self.writeInt(3)
        self.writeInt(0) # max players for team
        self.writeInt(5)
        self.writeInt(0) # shop disabled
        self.writeInt(6)
        self.writeInt(0) # isGachaDisabled
        self.writeInt(7)
        self.writeInt(0) # bool related to OfferBundleItem::getForcedBounds
        self.writeInt(11)
        self.writeInt(255) # max length for club mails
        self.writeInt(12)
        self.writeInt(0) # disable skins shop
        self.writeInt(13)
        self.writeInt(0) # disable star points skins shop
        self.writeInt(14)
        self.writeInt(1) # token double event enabled
        self.writeInt(15)
        self.writeInt(0) # support creator disabled
        self.writeInt(16)
        self.writeInt(0) # cn stuffs related bool
        self.writeInt(17)
        self.writeInt(69) # idk
        self.writeInt(18)
        self.writeInt(0) # bool related to gamemode
        self.writeInt(19)
        self.writeInt(0) # related to skins in shop
        self.writeInt(20)
        self.writeInt(0) # bool related to skins in shop
        self.writeInt(21)
        self.writeInt(0) # guaranteed hero boxes enabled?!!
        self.writeInt(22)
        self.writeInt(69) # idk
        self.writeInt(24)
        self.writeInt(0) # bool related to buttons
        self.writeInt(25)
        self.writeInt(0) # bool related to skins in shop
        self.writeInt(26)
        self.writeInt(int(config.brawlPassEnabled)) # isBrawlPassEnabled
        self.writeInt(28)
        self.writeInt(4) # challenge life count
        self.writeInt(29)
        self.writeInt(0) # related to skins in shop
        self.writeInt(30)
        self.writeInt(0) # search players disabled
        self.writeInt(31)
        self.writeInt(1) # coinShowerEnabled
        self.writeInt(34)
        self.writeInt(7) # mimum power level for gadget :skull: why the fuck can we edit it from there
        
        
        
        self.writeVInt(1) # idk array
        for x in range(1):
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
        # Logic Conf Data End
        
        self.writeLong(*player.ID)  # Home ID

        self.writeVInt(1)  # Notification Factory
        
        self.writeVInt(83)
        baseNotification = BaseNotification()
        baseNotification.setMessage("Pour")
        baseNotification.encode(self)
        chronosTextEntry = ChronosTextEntry()
        chronosTextEntry.setTextEntry("Welcome to BSDS v26")
        chronosTextEntry.encode(self)  # Primary Text Entry
        chronosTextEntry = ChronosTextEntry()
        chronosTextEntry.setTextEntry("This server has been codded by Jordi")
        chronosTextEntry.encode(self)  # Secondary Text Entry
        chronosTextEntry = ChronosTextEntry()
        chronosTextEntry.setTextEntry("DISCORD")
        chronosTextEntry.encode(self)  # Button Text Entry
        chronosFileEntry = ChronosFileEntry()
        chronosFileEntry.setFilePath("b2d704b22b95a4d70f66e89da867a64b")
        chronosFileEntry.setFileSHA("3a35620676c1d08d12086257a5ae03eb612452d8") # use sha1 please
        chronosFileEntry.encode(self) # Background
        self.writeStringReference(URLBuilder.encode(config.advertisedURL)) # Redirect
        self.writeVInt(0)
        
        
        self.writeVInt(0)  # ?
        self.writeBoolean(False)
        
        self.writeVInt(0)  # ?
        self.writeVInt(0)  # ?
        # Logic Client Home End

        # Logic Client Avatar
        self.writeVLong(*player.ID)  # ID
        self.writeVLong(0, 0)  # Account ID
        self.writeVLong(0, 0)  # Home ID
        self.writeString(player.Name)  # Player Name
        self.writeBoolean(player.Registered)  # Registered Name State
        self.writeInt(-1)
        self.writeVInt(8)  # Commodity Count

        # Unlocked Brawler and Resources Array

        self.writeVInt(len(brawlers)+4) # Items Count
        for hero in brawlers.values():
            self.writeDataReference(23, hero["CardID"])  # Item ID
            self.writeVInt(1)  # Item Data

        self.writeDataReference(5, 1)  # Resource ID
        self.writeVInt(player.Tokens)  # Keys Amount
        self.writeDataReference(5, 8)  # Resource ID
        self.writeVInt(player.Coins)  # Coins Amount
        self.writeDataReference(5, 9)  # Resource ID
        self.writeVInt(player.StarTokens)  # Star Tokens Amount
        self.writeDataReference(5, 10)  # Resource ID
        self.writeVInt(player.StarPoints)  # Star Points Amount
        # Unlocked Brawlers and Resources Array End

        # Brawlers Trophies Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for i, x in brawlers.items():
            self.writeDataReference(16, i)  # Brawler ID
            self.writeVInt(x["Trophies"])  # Brawler Trophies
        # Brawlers Trophies Array End

        # Brawlers Highest Trophies Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for i, x in brawlers.items():
            self.writeDataReference(16, i)  # Brawler ID
            self.writeVInt(x["HighestTrophies"])  # Brawler Highest Trophies
        # Brawlers Highest Trophies Array End

        # Highest Resources Amount Array
        self.writeVInt(0)  # Resources Count
        for x in range(0):
            self.writeDataReference(5, 0)  # Resource ID
            self.writeVInt(0)  # Resource Amount
        # Highest Resources Amount Array End

        # Brawlers Power Points Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for i,x in brawlers.items():
            self.writeDataReference(16, i)  # Brawler ID
            self.writeVInt(x["PowerPoints"])  # Brawler Power Points Amount
        # Brawlers Power Points Array End

        # Brawlers Level Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for i,x in brawlers.items():
            self.writeDataReference(16, i)  # Brawler ID
            self.writeVInt(x["PowerLevel"]-1)  # Brawler Power Level
        # Brawlers Level Array End

        # Brawlers Star Power Array
        selected = []
        for x in player.SelectedStarPowers.values():
            selected.append(x)
        for x in player.SelectedGadgets.values():
            selected.append(x)
        self.writeVInt(len(starPowers) + len(gadgets))  # Items Count
        for x in starPowers + gadgets:
            self.writeDataReference(23, x)  # Item ID
            self.writeVInt(2 if x in selected else 1)  # 2 if selected else 1
        # Brawlers Star Power Array End

        # Brawlers Seem State Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for i, x in brawlers.items():
            self.writeDataReference(16, i)  # Brawler ID
            self.writeVInt(x["State"])  # Brawler Seem State
        # Brawlers Seem State Array End

        self.writeVInt(player.Gems)  # Player Gems
        self.writeVInt(0)  # Player Free Gems
        self.writeVInt(1)  # Player Experience Level
        self.writeVInt(0)  # Cumulative Purchased Gems
        self.writeVInt(0)  # Battles Count
        self.writeVInt(0)  # Win Count
        self.writeVInt(0)  # Lose Count
        self.writeVInt(0)  # Win/Loose Streak
        self.writeVInt(0)  # Npc Win Count
        self.writeVInt(0)  # Npc Lose Count
        self.writeVInt(2)  # Tutorial State
        # Logic Client Avatar End
        self.writeVInt(2)  # Current Time

        

    def decode(self):
        return self

    def execute(message, calling_instance):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion