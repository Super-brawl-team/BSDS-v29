import sqlite3
import json
from Classes.Instances.Classes.Alliance import Alliance
class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect('Database/alliances.db',check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Alliances (
                ID INTEGER PRIMARY KEY,
                data TEXT
            )
        ''')
        self.connection.commit()
        
    def findIDInTable(self, ID):
        self.cursor.execute("SELECT 1 FROM Alliances WHERE ID = ?", (ID,))
        result = self.cursor.fetchone()
        return result is not None
    
    def createAccount(self, alliance: Alliance):
        self.assignLowId(alliance)
        jsonData = alliance.toJSON()
        self.cursor.execute(
            "INSERT INTO Alliances (ID, data) VALUES (?, ?)",
            (alliance.ID[1], json.dumps(jsonData))
        )
        self.connection.commit()
        
    def loadInstance(self, ID):
        alliance = Alliance()
        self.cursor.execute("SELECT data FROM Alliances WHERE ID = ?", (ID,))
        result = self.cursor.fetchone()
        if result:
            jsonData = json.loads(result[0])
            alliance.fromJSON(jsonData)
        return alliance

            
    def getAllAlliances(self):
        self.cursor.execute("SELECT data FROM Alliances")
        results = self.cursor.fetchall()
        instances = []
        for result in results:
            alliance = Alliance()
            jsonData = json.loads(result[0])
            alliance.fromJSON(jsonData)
            instances.append(alliance)
        return instances
    
    def loadMultipleInstance(self, IDs):
        alliances = ",".join(["?"] * len(IDs))
        query = f"SELECT data FROM Players WHERE ID IN ({alliances})"
        self.cursor.execute(query, IDs)
        results = self.cursor.fetchall()
        instances = []
        for result in results:
            alliance = Alliance()
            jsonData = json.loads(result[0])
            alliance.fromJSON(jsonData)
            instances.append(alliance)
        return instances


    def getSpecifiedValue(self, name, alliance):
        self.cursor.execute("SELECT data FROM Alliances WHERE ID = ?", (alliance.ID[1],))
        result = self.cursor.fetchone()
        if result:
            allianceData = json.loads(result[0])
            return allianceData.get(name)

    def replaceValue(self, name, updated, alliance):
        self.cursor.execute(
            "UPDATE Alliances SET data = json_set(data, ?, json(?)) WHERE ID = ?",
            (f"$.{name}", json.dumps(updated), alliance.ID[1])
        )
        self.connection.commit()

    def replaceOtherValue(self, value_name, new_value, ID):
        self.cursor.execute("SELECT data FROM Alliances WHERE ID = ?", (ID,))
        result = self.cursor.fetchone()
        if result:
            allianceData = json.loads(result[0])
            allianceData[value_name] = new_value
            self.cursor.execute("UPDATE Alliances SET data = ? WHERE ID = ?", (json.dumps(allianceData), ID))
            self.connection.commit()

    def appendElementToArray(self, name, element, alliance):
        self.cursor.execute("SELECT data FROM Alliances WHERE ID = ?", (alliance.ID[1],))
        result = self.cursor.fetchone()
        if result:
            allianceData = json.loads(result[0])
            if name in allianceData and isinstance(allianceData[name], list):
                allianceData[name].append(element)
            else:
                allianceData[name] = [element]
            self.cursor.execute("UPDATE Alliances SET data = ? WHERE ID = ?", (json.dumps(allianceData), alliance.ID[1]))
            self.connection.commit()
        
    def assignLowId(self, alliance):
        self.cursor.execute("SELECT COUNT(*) FROM Alliances")
        low_id = self.cursor.fetchone()[0] + 1
        alliance.ID = [0, low_id]
