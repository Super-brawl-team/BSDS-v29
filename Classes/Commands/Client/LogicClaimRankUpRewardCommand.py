from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Classes.Files.Classes.Milestones import Milestones
from Classes.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Logic.LogicHomeChangeListener import LogicHomeChangeListener
from Classes.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Classes.Entries.DeliveryUnit import DeliveryUnit
from Classes.Entries.GachaDrop import GachaDrop
from Classes.Files.Classes.Skins import Skins
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Cards import Cards

class LogicClaimRankUpRewardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)
        self.target = []
        self.milestoneID = 0
        self.season = 0

    def encode(self):
        LogicCommand.encode(self)
        self.writeVInt(self.milestoneID)
        self.writeDataReference(self.target)
        self.writeVInt(self.season)
        return self.messagePayload

    def decode(self, calling_instance):
        LogicCommand.decode(calling_instance)
        self.milestoneID = calling_instance.readVInt()
        self.target = calling_instance.readDataReference()
        self.season =calling_instance.readVInt()
        return self

    def execute(self, calling_instance, cryptoInit):
        print(calling_instance.player)
        calling_instance.player.OwnedBrawlers = {int(k): v for k, v in calling_instance.player.OwnedBrawlers.items()}
        availableServerCommandMessage = AvailableServerCommandMessage(b'')
        logicGiveDeliveryItemsCommand = LogicGiveDeliveryItemsCommand(b'')
        if self.milestoneID == 6:
            milestonesWithType = Milestones.getAllMilestonesWithType(self.milestoneID)
            selectedMilestone = milestonesWithType[calling_instance.player.TrophyRoadTier-1]
            calling_instance.player.TrophyRoadTier+=1
            calling_instance.db.replaceValue("TrophyRoadTier", calling_instance.player.TrophyRoadTier, calling_instance.player)
            logicGiveDeliveryItemsCommand.setMilestoneTrack(calling_instance.player.TrophyRoadTier)
        elif self.milestoneID == 9:
            milestonesWithType = Milestones.getAllMilestonesWithType(self.milestoneID, self.season)
            selectedMilestone = milestonesWithType[calling_instance.player.BrawlPassDatas[str(self.season)]["PaidPassTier"]-1]
            calling_instance.player.BrawlPassDatas[str(self.season)]["PaidPassTier"]+=1
            calling_instance.db.replaceValue("BrawlPassDatas", calling_instance.player.BrawlPassDatas, calling_instance.player)
            logicGiveDeliveryItemsCommand.setMilestoneTrack(calling_instance.player.BrawlPassDatas[str(self.season)]["PaidPassTier"])   
            logicGiveDeliveryItemsCommand.setSeason(self.season)
        elif self.milestoneID == 10:
            milestonesWithType = Milestones.getAllMilestonesWithType(self.milestoneID, self.season)
            selectedMilestone = milestonesWithType[calling_instance.player.BrawlPassDatas[str(self.season)]["FreePassTier"]-1]
            calling_instance.player.BrawlPassDatas[str(self.season)]["FreePassTier"]+=1
            calling_instance.db.replaceValue("BrawlPassDatas", calling_instance.player.BrawlPassDatas, calling_instance.player)
            logicGiveDeliveryItemsCommand.setMilestoneTrack(calling_instance.player.BrawlPassDatas[str(self.season)]["FreePassTier"])
            logicGiveDeliveryItemsCommand.setSeason(self.season)
        gachaDrops = []
        deliveryUnit = DeliveryUnit()
        gachaDrop = GachaDrop()
        gachaDrop.setAmount(selectedMilestone.getPrimaryLvlUpRewardCount())
        if selectedMilestone.getPrimaryLvlUpRewardType() == 1:
            gachaDrop.setType(7)
            calling_instance.player.Coins+=selectedMilestone.getPrimaryLvlUpRewardCount()
            calling_instance.db.replaceValue("Coins", calling_instance.player.Coins, calling_instance.player)
            gachaDrops.append(gachaDrop)   
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 3:
            gachaDrop.setType(1)
            gachaDrop.setCharacterDataReference([16,Characters.getBrawlerByName(selectedMilestone.getPrimaryLvlUpRewardHero())])
            gachaDrops.append(gachaDrop) 
            newBrawler = {'CardID': Cards.getBrawlerUnlockID(Characters.getBrawlerByName(selectedMilestone.getPrimaryLvlUpRewardHero())), 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2, 'Gadgets': [], 'StarPowers': []}
            calling_instance.player.OwnedBrawlers[Characters.getBrawlerByName(selectedMilestone.getPrimaryLvlUpRewardHero())] = newBrawler
            calling_instance.db.replaceValue("OwnedBrawlers", calling_instance.player.OwnedBrawlers, calling_instance.player)
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 4:
            gachaDrop.setType(9)
            gachaDrop.setCharacterDataReference([16,Skins.getBrawlerBySkin(Skins.getSkinByName(selectedMilestone.getPrimaryLvlUpRewardSkin()))])
            gachaDrop.setSkinDataReference([29, Skins.getSkinByName(selectedMilestone.getPrimaryLvlUpRewardSkin())])
            gachaDrops.append(gachaDrop)   
            calling_instance.player.OwnedBrawlers[Skins.getBrawlerBySkin(Skins.getSkinByName(selectedMilestone.getPrimaryLvlUpRewardSkin()))]["Skins"].append(Skins.getSkinByName(selectedMilestone.getPrimaryLvlUpRewardSkin()))
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 6:
            deliveryUnit.setType(10)
            gachaDrops = LogicHomeChangeListener.gacha(calling_instance.player, calling_instance.db, 10)
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 9:
            gachaDrop.setType(2)
            calling_instance.player.TokensDoubler+=selectedMilestone.getPrimaryLvlUpRewardCount()
            calling_instance.db.replaceValue("TokensDoubler", calling_instance.player.TokensDoubler, calling_instance.player)
            gachaDrops.append(gachaDrop)   
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 7:
            gachaDrop.setType(3)
            calling_instance.player.Tickets+=selectedMilestone.getPrimaryLvlUpRewardCount()
            calling_instance.db.replaceValue("Tickets", calling_instance.player.Tickets, calling_instance.player)
            gachaDrops.append(gachaDrop)   
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 10:
            deliveryUnit.setType(11)
            gachaDrops = LogicHomeChangeListener.gacha(calling_instance.player, calling_instance.db, 11)
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 12:
            gachaDrop.setType(6)
            gachaDrop.setCharacterDataReference(self.target)
            gachaDrops.append(gachaDrop)   
            calling_instance.player.OwnedBrawlers[self.target[1]]["PowerPoints"]+=selectedMilestone.getPrimaryLvlUpRewardCount()
            calling_instance.db.replaceValue("OwnedBrawlers", calling_instance.player.OwnedBrawlers, calling_instance.player)
        elif selectedMilestone.getPrimaryLvlUpRewardType() == 14:
            deliveryUnit.setType(12)
            gachaDrops = LogicHomeChangeListener.gacha(calling_instance.player, calling_instance.db, 12)
        deliveryUnit.setGachaDrops(gachaDrops)
        logicGiveDeliveryItemsCommand.setDeliveryUnits([deliveryUnit])
        logicGiveDeliveryItemsCommand.setMilestoneType(self.milestoneID)
        availableServerCommandMessage.setCommand(logicGiveDeliveryItemsCommand)
        Messaging.sendMessage(availableServerCommandMessage, calling_instance.client, cryptoInit, calling_instance)
        

    def getCommandType(self):
        return 517