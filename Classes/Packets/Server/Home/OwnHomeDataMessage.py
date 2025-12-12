from random import choice
from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.ChronosTextEntry import ChronosTextEntry
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Emotes import Emotes
from Classes.Files.Classes.Locations import Locations

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        skins = Skins.getSkinsID()
        brawlers = Characters.getBrawlersID()
        brawlersUnlockID = Cards.getBrawlersUnlockID()
        gadgets = Cards.getGadgetsID()
        starPowers = Cards.getStarpowersID()
        emotes = Emotes.getEmotesID()
        locations = Locations.getAllMaps()
        self.writeVInt(2018 * 1000 + 0)  # Current Year and Day
        self.writeVInt(0)  # Time Remaining For Next Day
        self.writeVInt(player.Trophies)  # Player Trophies
        self.writeVInt(player.HighestTrophies)  # Player Highest Trophies
        self.writeVInt(125)  # Player Reached Ranking Trophies
        self.writeVInt(600)  # trophy road collected
        self.writeVInt(player.Experience)  # Player Experience Points
        self.writeDataReference(28, player.Thumbnail)  # Player Profile Icon
        self.writeDataReference(43, player.Namecolor)  # Player Name Color

        # Played Game Modes Array
        self.writeVInt(20)  # Game Modes Count
        for x in range(20):
            self.writeVInt(x)  # Played Game Mode
        # Played Game Modes Array End

        # Selected Skins Array
        print(player.SelectedSkins)
        self.writeVInt(len(player.SelectedSkins))  # Skins Count
        for x in player.SelectedSkins.values():
            self.writeDataReference(29, x)  # Selected Skin
            
        
        # Selected Skins Array End

        # Unlocked Skins Array
        self.writeVInt(len(skins))  # Skins Count
        for x in skins:
            self.writeDataReference(29, x)  # Unlocked Skin
        # Unlocked Skins Array End
        
        self.writeVInt(len(player.SelectedStarPowers) + len(player.SelectedGadgets))

        for x in list(player.SelectedStarPowers.values()) + list(player.SelectedGadgets.values()):
            self.writeDataReference(23, x)

        
        self.writeVInt(0) # Leaderboard Region
        self.writeVInt(player.HighestTrophies) # today's highest trophies
        self.writeVInt(0) # used tokens
        self.writeVInt(0)
        self.writeBoolean(True)  # Daily Band Created
        self.writeVInt(0)  # Remaining Token Doubler
        self.writeVInt(0)  # Trophy Season Timer
        self.writeVInt(0) 
        self.writeVInt(0)  # Brawl Pass Season Timer
        # Forced Drops Entry
        self.writeVInt(0)  # Unknown
        self.writeVInt(0)  # Unknown
        self.writeVInt(0)  # Unknown array
        for x in range(0):
            self.writeVInt(0)
        # Forced Drops Entry End
        self.writeBoolean(False)  # Timed Offer Array
        self.writeBoolean(False) # Timed Offer Array 2
        self.writeBoolean(True)  # Key Limit Reached
        self.writeBoolean(False)
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
            ChronosTextEntry().encode(self, [0, "Hiii"])  # Offer Title text
            self.writeBoolean(False)  # Offer Is Seen
            self.writeStringReference("offer_legendary")  # Offer Background Image
            self.writeVInt(0)
            self.writeBoolean(False)
            self.writeVInt(2)
            self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(200) # Battle Tokens
        self.writeVInt(0) # Time Till Next Battle Token
        self.writeVInt(0)
        self.writeVInt(6969) # Tickets
        self.writeVInt(0)
        self.writeDataReference(16,player.SelectedBrawler) # selected brawler
        self.writeString(player.Region) # Location
        self.writeString(player.ContentCreator) # Supporter Creator Code
        self.writeVInt(5) # Int Value Entry
        
        self.writeInt(3)
        self.writeInt(0) # Tokens Rewarded
        
        self.writeInt(4)
        self.writeInt(0) # Trophies Rewarded
        
        self.writeInt(7)
        self.writeInt(0) # Do Not Disturb
        
        self.writeInt(8)
        self.writeInt(0) # Star Points Rewarded
        
        self.writeInt(10)
        self.writeInt(0) # Power Play Trophies Rewarded
        
        self.writeVInt(0) # CoolDown Entry
        for x in range(0):
            self.writeVInt(0)
            self.writeDataReference(16, 0)
            self.writeVInt(0)
            
        self.writeVInt(1) # BP
        for x in range(1):
            self.writeVInt(2) # season ID
            self.writeVInt(0) # season progress
            self.writeBoolean(True) # has brawl pass
            self.writeVInt(0) # season rewards claimed
            self.writeBoolean(False)
            self.writeBoolean(False)
            
        self.writeVInt(1) # ProLeagueSeasonData Array
        for x in range(1):
            self.writeVInt(2)
            self.writeVInt(0) # Points
            
        self.writeBoolean(True) # Quest Array
        self.writeVInt(1)
        for x in range(1):
            self.writeVInt(0) # Unk
            self.writeVInt(2) # Season
            self.writeVInt(0) # Type
            self.writeVInt(30) # Progress
            self.writeVInt(69) # Goal
            self.writeVInt(2000) # Reward
            self.writeVInt(0)
            self.writeVInt(0) # Current Level (for event)
            self.writeVInt(0) # Max Level
            self.writeVInt(0) # Expiration Timer
            self.writeBoolean(False) # IsBrawlPassExclusive
            self.writeBoolean(False) # Seen
            self.writeDataReference(16,0) # Targetted Char
            self.writeVInt(0) # Targetted Gamemode
            self.writeVInt(0) # Progrress..?
            self.writeVInt(0)
            
        self.writeBoolean(True)
        self.writeVInt(len(emotes)) # Emotes Array
        for x in emotes:
            self.writeDataReference(52, x)
            self.writeVInt(0)
        # Shop Offers Array End
        # Logic Daily Data End

        # Logic Conf Data
        self.writeVInt(2018 * 1000 + 0)  # Shop Current Year and Day
        self.writeVInt(100)  # Brawl Box Keys
        self.writeVInt(10)  # Shop Brawl Box Cost
        self.writeVInt(80)  # Shop Big Box Cost
        self.writeVInt(10)  # Shop Big Box Multipler
        self.writeVInt(50)  # Key Doubler Cost
        self.writeVInt(1000)  # Key Doubler Ammount
        self.writeVInt(500)  # Minimum Brawler Trophies For Season Reset
        self.writeVInt(50)  # Brawler Trophy Loss Percentage in Season Reset
        self.writeVInt(999900)  # Key Limit Amount
        self.writeVInt(0)
        self.writeVInt(0)
        ByteStreamHelper.encodeIntList(self, [0, 30, 80, 170, 350, 0])  # Boxes With Guaranteed Brawlers Cost

        # Event Slots Array
        self.writeVInt(100)  # Event Slots Count (1 : gem grab, 2: showdown, 3: daily events, 4: team events, 5: duo showdown, 6: team events, 7: special events, 8: solo events, 9: power play, 21: challenge)
        for x in range(100):
            self.writeVInt(x + 1)  # Event Index
        # Event Slots Array End

        # Logic Events Array
        EventLocation = [choice(locations), choice(locations), choice(locations), choice(locations), choice(locations), choice(locations), choice(locations)]
        self.writeVInt(len(EventLocation))  # Event Slots Count
        for x in range(len(EventLocation)):
            self.writeVInt(0) # Event Index
            self.writeVInt(x + 1)  # Event Index
            self.writeVInt(0)  # New Event Timer
            self.writeVInt(0)  # Event Timer
            self.writeVInt(10)  # New Event Keys
            self.writeDataReference(15, EventLocation[x])  # Location ID
            self.writeBoolean(False)  # Is Event Active
            self.writeBoolean(False)  # Is Event New
            self.writeString()  # Event Custom Entry
            self.writeVInt(0)  # Event Tickets Amount
            self.writeVInt(0) # Power Play Games Played
            self.writeVInt(3) # Power Play Games Left
            modifiers = []#[1,2,3,5]*50 + [4]*3
            self.writeVInt(len(modifiers)) # modifiers array
            for x in modifiers:
                self.writeVInt(x)
            self.writeVInt(0) 
            self.writeVInt(0)
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
            self.writeVInt(3) # Power Play Games Left
            modifiers = []#[1,2,3,5]*50 + [4]*3
            self.writeVInt(len(modifiers)) # modifiers array
            for x in modifiers:
                self.writeVInt(x)
            self.writeVInt(0) 
            self.writeVInt(0)
        # Coming Up Events Array End

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250])  # Brawler Coins Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [1, 2, 3, 4, 5, 10, 15, 20])  # Highstakes Rewards
        ByteStreamHelper.encodeIntList(self, [10, 30, 80])  # Event Tickets Cost
        ByteStreamHelper.encodeIntList(self, [6, 20, 60])  # Event Tickets Amount
        ByteStreamHelper.encodeIntList(self, [20, 50, 140])  # Coin Packs Cost
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200])  # Coin Packs Amount

        self.writeVInt(2)  # ?
        
        self.writeVInt(200)  # Max Battle Tokens
        self.writeVInt(20)  # Battle Tokens Refresh Amount
        self.writeVInt(0)  # ?
        self.writeVInt(10)  # ?
        self.writeVInt(5)  # ?
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        self.writeVInt(0)  # ?
        self.writeVInt(0)  # ?
        self.writeBoolean(True) # Boxes Enabled In Shop
        
        self.writeVInt(0)  # ?
        self.writeVInt(1)  # IntValue Entry
        self.writeInt(1)
        self.writeInt(41000001) # Theme ID
        
        # Logic Conf Data End
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLong(*player.ID)  # Home ID

        self.writeVInt(0)  # Notification Factory
        
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

        self.writeVInt(len(brawlersUnlockID)+5)#heroesLength + 5)  # Items Count
        for hero in brawlersUnlockID:
            self.writeDataReference(23, hero)#hero["u"])  # Item ID
            self.writeVInt(1)  # Item Data

        self.writeDataReference(5, 1)  # Resource ID
        self.writeVInt(100)  # Keys Amount
        self.writeDataReference(5, 5)  # Resource ID
        self.writeVInt(0)  # Chips Amount
        self.writeDataReference(5, 6)  # Resource ID
        self.writeVInt(0)  # Elixir Amount
        self.writeDataReference(5, 7)  # Resource ID
        self.writeVInt(0)  # Upgrade Tokens Amount
        self.writeDataReference(5, 8)  # Resource ID
        self.writeVInt(100000)  # Coins Amount
        # Unlocked Brawlers and Resources Array End

        # Brawlers Trophies Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVInt(1250)  # Brawler Trophies
        # Brawlers Trophies Array End

        # Brawlers Highest Trophies Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVInt(1250)  # Brawler Highest Trophies
        # Brawlers Highest Trophies Array End

        # Highest Resources Amount Array
        self.writeVInt(0)  # Resources Count
        for x in range(0):
            self.writeDataReference(5, 0)  # Resource ID
            self.writeVInt(0)  # Resource Amount
        # Highest Resources Amount Array End

        # Brawlers Power Points Array
        self.writeVInt(0)  # Brawlers Count
        for x in range(0):
            self.writeDataReference(16, 0)  # Brawler ID
            self.writeVInt(0)  # Brawler Power Points Amount
        # Brawlers Power Points Array End

        # Brawlers Level Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for x in brawlers:
            self.writeDataReference(16, x)  # Brawler ID
            self.writeVInt(8)  # Brawler Power Level
        # Brawlers Level Array End

        # Brawlers Star Power Array
        self.writeVInt(len(starPowers) + len(gadgets))  # Items Count
        for x in starPowers + gadgets:
            self.writeDataReference(23, x)  # Item ID
            self.writeVInt(1)  # Item Data possibly state
        # Brawlers Star Power Array End

        # Brawlers Seem State Array
        self.writeVInt(len(brawlers))  # Brawlers Count
        for x in brawlers:
            self.writeDataReference(16, 0)  # Brawler ID
            self.writeVInt(0)  # Brawler Seem State
        # Brawlers Seem State Array End

        self.writeVInt(100000)  # Player Gems
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
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion