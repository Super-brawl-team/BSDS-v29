import sqlite3
import json
from Classes.Instances.Classes.Player import Player
class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('Database/database.db',check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Players (
                token TEXT PRIMARY KEY,
                data TEXT
            )
        ''')
        self.connection.commit()
        
    def findTokenInTable(self, token):
        self.cursor.execute("SELECT 1 FROM Players WHERE token = ?", (token,))
        result = self.cursor.fetchone()
        return result is not None
    
    def createAccount(self, player: Player):
        self.assignLowId(player)
        jsonData = player.toJSON()
        self.cursor.execute(
            "INSERT INTO Players (token, data) VALUES (?, ?)",
            (player.Token, json.dumps(jsonData))
        )
        self.connection.commit()
        
    def loadInstance(self, token):
        player = Player()
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (token,))
        result = self.cursor.fetchone()
        if result:
            jsonData = json.loads(result[0])
            player.fromJSON(jsonData)
        return player

            
    def getAllPlayers(self):
        self.cursor.execute("SELECT data FROM Players")
        results = self.cursor.fetchall()
        instances = []
        for result in results:
            player = Player()
            jsonData = json.loads(result[0])
            player.fromJSON(jsonData)
            instances.append(player)
        return instances
    
    def loadMultipleInstance(self, tokens):
        players = ",".join(["?"] * len(tokens))
        query = f"SELECT data FROM Players WHERE token IN ({players})"
        self.cursor.execute(query, tokens)
        results = self.cursor.fetchall()
        instances = []
        for result in results:
            player = Player()
            jsonData = json.loads(result[0])
            player.fromJSON(jsonData)
            instances.append(player)
        return instances

    def getTokenByLowId(self, lowID):
        self.cursor.execute("SELECT token, data FROM Players")
        rows = self.cursor.fetchall()

        for token, data in rows:
            playerData = json.loads(data)
            if "ID" in playerData and isinstance(playerData["ID"], list):
                if playerData["ID"][1] == lowID:
                    return token

        return None


    def getSpecifiedValue(self, name, player):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (player.Token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            return playerData.get(name)

    def replaceValue(self, name, updated, player):
        self.cursor.execute(
            "UPDATE Players SET data = json_set(data, ?, json(?)) WHERE token = ?",
            (f"$.{name}", json.dumps(updated), player.Token)
        )
        self.connection.commit()

    def replaceOtherValue(self, value_name, new_value, token):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            playerData[value_name] = new_value
            self.cursor.execute("UPDATE Players SET data = ? WHERE token = ?", (json.dumps(playerData), token))
            self.connection.commit()

    def appendElementToArray(self, name, element, player):
        self.cursor.execute("SELECT data FROM Players WHERE token = ?", (player.Token,))
        result = self.cursor.fetchone()
        if result:
            playerData = json.loads(result[0])
            if name in playerData and isinstance(playerData[name], list):
                playerData[name].append(element)
            else:
                playerData[name] = [element]
            self.cursor.execute("UPDATE Players SET data = ? WHERE token = ?", (json.dumps(playerData), player.Token))
            self.connection.commit()
        
    def assignLowId(self, player):
        self.cursor.execute("SELECT COUNT(*) FROM Players")
        low_id = self.cursor.fetchone()[0] + 1
        player.ID = [0, low_id]
