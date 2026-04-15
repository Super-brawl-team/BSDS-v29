import csv


class Cards:
    def getOwner(cardID):
        BrawlerOwner = ""
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == cardID:
                        BrawlerOwner = row[3]
                        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
                        char_reader = csv.reader(char_file, delimiter=',')
                        while open('Classes/Files/assets/csv_logic/characters.csv'):
                            char_line_count = 0
                            for char_row in char_reader:
                                if char_line_count == 0 or char_line_count == 1:
                                    char_line_count += 1
                                else:
                                    if char_row[0] == BrawlerOwner:
                                        return char_line_count - 2
                                    char_line_count += 1
                    line_count += 1
    def getStarpowersID():
        CardSkillsID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5] == '4' and row[4].lower() != "true":
                        CardSkillsID.append(line_count - 2)
                    line_count += 1

            return CardSkillsID
        
    def getGadgetsID():
        CardGadgetsID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5] == '5':
                        CardGadgetsID.append(line_count - 2)
                    line_count += 1

            return CardGadgetsID

    def getBrawlerStarpowers(brawlerID):
        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = []

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Classes/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            if row[5].lower() == '4' and row[3] == name and row[4] != "true":
                                id.append(line_count - 2)
                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    return id
                
    def getBrawlerGadgets(brawlerID):
        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = []

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Classes/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            if row[5].lower() == '5' and row[3] == name:
                                id.append(line_count - 2)
                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    return id

    def getBrawlerUnlockID(brawlerID):
        char_file = open('Classes/Files/assets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0
        id = 0

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawlerID + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('Classes/Files/assets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0
                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            if row[5].lower() == '0' and row[3] == name and row[4].lower() != "true":
                                id = line_count - 2
                            line_count += 1

                    char_file.close()
                    cards_file.close()
                    return id


    def getBrawlersUnlockID():
        CardUnlockID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5] == '0'  and row[4].lower() != "true":
                        CardUnlockID.append(line_count - 2)
                    line_count += 1

            return CardUnlockID
        
    def getBrawlersUnlockIDWithRarity(rarityID):
        rarity = Cards.getRarityByID(rarityID)
        CardUnlockID = []
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[5] == '0'  and row[4].lower() != "true" and row[12] == rarity:
                        CardUnlockID.append(line_count - 2)
                    line_count += 1

            return CardUnlockID
        
    def isStarPower(cardID):
        with open('Classes/Files/assets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count - 2 == cardID:
                        if row[5] == '4':
                            return True
                        else:
                            return False
                    line_count += 1
                    
    def getRarityByID(rarity) :
        if rarity == 0:
            return "common"
        if rarity == 1:
            return"rare"
        if rarity ==  2:
            return "super_rare"
        if rarity ==  3:
            return "epic"
        if rarity ==  4:
            return "mega_epic"
        if rarity ==  5:
            return "legendary"
        else: 
            return "common"