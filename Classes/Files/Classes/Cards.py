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
                    if row[6] == '4' and row[4].lower() != "true":
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
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
                    if row[6] == '5':
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
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
                            print(row)
                            if row[6].lower() == '4' and row[3] == name and row[4] != "true":
                                # print(row[0], line_count - 3)
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
                            if row[6].lower() == '0' and row[3] == name and row[4].lower() != "true":
                                # print(row[0], line_count - 3)
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
                    if row[6] == '0' and row[4].lower() != "true":
                        # print(line_count - 2, row[7], row[3], row[4], row[5])
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
                        if row[6] == '4':
                            return True
                        else:
                            return False
                    line_count += 1
        
