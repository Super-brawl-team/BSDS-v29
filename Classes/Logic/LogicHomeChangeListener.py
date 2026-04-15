from random import randint, choice, choices,sample
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Cards import Cards
from Classes.Entries.GachaDrop import GachaDrop

class LogicHomeChangeListener:
    def gacha(player, db, boxType):
        gachaDrops = []
        player.OwnedBrawlers = {int(k): v for k, v in player.OwnedBrawlers.items()}
        allCharacters = Characters.getBrawlersID()
        owned = []
        for x,y in player.OwnedBrawlers.items():
            owned.append(x)
            allCharacters.remove(x)
        hasBrawler = randint(0,5)==2 and len(allCharacters)>0
        hasBonus = randint(0,5) == 2
        hasStarPower = False
        maxed=[]
        for i, x in player.OwnedBrawlers.items():
            gadgets=x["Gadgets"]
            allGadgets=Cards.getBrawlerGadgets(i)
            unlockableGadgets = []
            for gadget in allGadgets:
                if gadget not in gadgets:
                    unlockableGadgets.append(gadget)
            starPowers=x["StarPowers"]
            allStarPowers=Cards.getBrawlerStarpowers(i)
            unlockableStarPowers = []
            for starPower in allStarPowers:
                if starPower not in starPowers:
                    unlockableStarPowers.append(starPower)
            if (x["PowerLevel"]>=9 and len(unlockableStarPowers) >0) or (x["PowerLevel"]>=7 and len(unlockableGadgets) >0):
                maxed.append(i)
        if len(maxed)>0:
            hasStarPower = randint(0,5)==2
            if boxType == 10 and hasStarPower:
                hasBrawler = False
        if hasBrawler:
            brawlerDrops = []
            brawlersAmount = choices(list(range(5)),[0.45, 0.35, 0.15, 0.1, 0.05], k=1)[0]+1 if boxType == 11 else 1
            for x in range(brawlersAmount):
                selectedRarity = choices(list(range(5)),[0.45, 0.35, 0.15, 0.1, 0.05], k=1)[0]+1
                ownedCardIDs = []
                for x in player.OwnedBrawlers.values():
                    ownedCardIDs.append(x["CardID"])
                allCardsWithRarity = Cards.getBrawlersUnlockIDWithRarity(selectedRarity)
                for x in ownedCardIDs:
                    if x in allCardsWithRarity:
                        allCardsWithRarity.remove(x)
                if len(allCardsWithRarity)<=0:
                    continue
                cardID = choice(allCardsWithRarity)
                characterID = Cards.getOwner(cardID)
                newBrawler = {'CardID': cardID, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2, 'Gadgets': [], 'StarPowers': []}
                player.OwnedBrawlers[characterID] = newBrawler
                brawler = GachaDrop()
                brawler.setAmount(1)
                brawler.setType(1)
                brawler.setCharacterDataReference([16, characterID])
                brawlerDrops.append(brawler)
            db.replaceValue("OwnedBrawlers", player.OwnedBrawlers, player)
            if len(brawlerDrops)<=0 and boxType==10:
                hasBrawler=False
        if boxType == 11:
            coinsAmount = randint(100,250)
        elif boxType == 12:
            coinsAmount = randint(25,105)
        else:
            coinsAmount = randint(14,70)
        if boxType == 10 and hasBrawler:
            hasBonus=False
        if not (boxType==10 and (hasBrawler or hasStarPower)):
            coins = GachaDrop()
            coins.setAmount(coinsAmount)
            coins.setType(7)
            gachaDrops.append(coins)
            player.Coins+=coinsAmount
            db.replaceValue("Coins", player.Coins, player)
            
        nonMaxed = []
        for i, x in player.OwnedBrawlers.items():
            if x["PowerLevel"]<8 and x["PowerPoints"] <1410:
                nonMaxed.append(i) 
        powerPointsDropCount = 0
        if boxType == 10:
            if not (hasBrawler or hasStarPower):
                powerPointsDropCount=2
        elif boxType == 11:
            powerPointsDropCount=5
        else:
            if hasBrawler or hasStarPower:
                powerPointsDropCount=2
            else:
                powerPointsDropCount=3
        if len(nonMaxed)<=0:
            powerPointsDropCount=0
        elif len(nonMaxed)<powerPointsDropCount:
            powerPointsDropCount=len(nonMaxed)
        targets = sample(nonMaxed, k=powerPointsDropCount)
        ppDrops=[]
        for targetID in targets:
            target = player.OwnedBrawlers[targetID]
            if boxType == 11:
                ppAmount = randint(5,50)
            elif boxType == 12:
                ppAmount = randint(5,30)
            else:
                ppAmount = randint(5,25)
            if target["PowerPoints"]+ppAmount>1410:
                ppAmount=1410-target["PowerPoints"]
            ppDrop = GachaDrop()
            ppDrop.setAmount(ppAmount)
            ppDrop.setType(6)
            ppDrop.setCharacterDataReference([16, targetID])
            ppDrops.append(ppDrop)
            target["PowerPoints"]+=ppAmount
            player.OwnedBrawlers[targetID] = target
            db.replaceValue("OwnedBrawlers", player.OwnedBrawlers, player)
        ppDrops.sort(key=lambda drop: drop.getAmount(), reverse=False)
        gachaDrops+=ppDrops
        if hasBrawler:
            brawlersAmount = choices(list(range(5)),[0.45, 0.35, 0.15, 0.1, 0.05], k=1)[0]+1 if boxType == 11 else 1
            for x in range(brawlersAmount):
                selectedRarity = choices(list(range(5)),[0.45, 0.35, 0.15, 0.1, 0.05], k=1)[0]+1
                ownedCardIDs = []
                for x in player.OwnedBrawlers.values():
                    ownedCardIDs.append(x["CardID"])
                allCardsWithRarity = Cards.getBrawlersUnlockIDWithRarity(selectedRarity)
                for x in ownedCardIDs:
                    if x in allCardsWithRarity:
                        allCardsWithRarity.remove(x)
                if len(allCardsWithRarity)<=0:
                    continue
                cardID = choice(allCardsWithRarity)
                characterID = Cards.getOwner(cardID)
                newBrawler = {'CardID': cardID, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2, 'Gadgets': [], 'StarPowers': []}
                player.OwnedBrawlers[characterID] = newBrawler
                reward = GachaDrop()
                reward.setAmount(1)
                reward.setType(1)
                reward.setCharacterDataReference([16, characterID])
                gachaDrops.append(reward)
            db.replaceValue("OwnedBrawlers", player.OwnedBrawlers, player)
        if hasStarPower:
            starPower = randint(0,1)
            targetID = choice(maxed)
            target = player.OwnedBrawlers[targetID]
            reward = GachaDrop()
            allGadgets=Cards.getBrawlerGadgets(targetID)
            allStarPowers=Cards.getBrawlerStarpowers(targetID)
            if (starPower==0 and target["PowerLevel"]>=7 and len(allGadgets)>0) or len(allStarPowers)<=0:
                gadgets=target["Gadgets"]
                unlockableGadgets = []
                for gadget in allGadgets:
                    if gadget not in gadgets:
                        unlockableGadgets.append(gadget)
                selectedGadget = choice(unlockableGadgets)
                target["Gadgets"].append(selectedGadget)
                reward.setExtraDataRefence([23,selectedGadget])
                reward.setAmount(1)
                reward.setType(4)
                gachaDrops.append(reward)
                db.replaceValue("OwnedBrawlers", player.OwnedBrawlers, player)
            elif len(allStarPowers)>0:
                starPowers=target["StarPowers"]
                allStarPowers=Cards.getBrawlerStarpowers(targetID)
                unlockableStarPowers = []
                for starPower in allStarPowers:
                    if starPower not in starPowers:
                        unlockableStarPowers.append(starPower)
                selectedStarPower = choice(unlockableStarPowers)
                target["StarPowers"].append(selectedStarPower)
                reward.setExtraDataRefence([23,selectedStarPower])
                reward.setAmount(1)
                reward.setType(4)
                gachaDrops.append(reward)
                db.replaceValue("OwnedBrawlers", player.OwnedBrawlers, player)
        if hasBrawler:
            gachaDrops+=brawlerDrops
        if hasBonus:
            bonus = GachaDrop()
            selectedBonus = choice([2,3,8])
            if selectedBonus==2:
                amount=200
                player.TokensDoubler+=amount
                db.replaceValue("TokensDoubler", player.TokensDoubler, player)
            elif selectedBonus==3:
                amount = choice([1,2,3,5])
                player.Tickets+=amount
                db.replaceValue("Tickets", player.Tickets, player)
            else:
                amount = choice([3, 5, 6, 8, 12])
                player.Gems+=amount
                db.replaceValue("Gems", player.Gems, player)
            bonus.setAmount(amount)
            bonus.setType(selectedBonus)
            gachaDrops.append(bonus)
        return gachaDrops