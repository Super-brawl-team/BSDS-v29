from Classes.Messaging import Messaging
from Classes.Packets.Server.Authentification.LoginFailedMessage import LoginFailedMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.ClientsManager import ClientsManager
from Classes.Packets.Server.Authentification.LoginOkMessage import LoginOkMessage
from Classes.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Classes.Packets.Server.Home.MyAllianceMessage import MyAllianceMessage
from Classes.Packets.Server.Home.AllianceWarMessage import AllianceWarMessage
from Classes.Utility import Utility
from time import *

class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.accountID = []
        self.passToken = ""
        self.clientMajor = 0
        self.clientMinor = 0
        self.clientBuild = 0

    def encode(self):
        pass

    def decode(self):
        self.accountID = self.readLong()
        self.passToken = self.readString()
        self.clientMajor = self.readInt()
        self.clientMinor = self.readInt()
        self.clientBuild = self.readInt()
        self.readString() #ResourceSha
        self.readString() # Device
        self.readString()
        self.readString()
        self.readString()
        self.readDataReference() #PreferredLanguage
        self.readString() #PreferredDeviceLanguage
        self.readString() #OSVersion
        self.readString()
        self.readBoolean() #isAndroid
        self.readStringReference() #IMEI 
        self.readStringReference() # AndroidID
        self.readStringReference()
        self.readBoolean() #isAdvertisingEnabled
        self.readString() # AppleIFV
        self.readInt() #RandomKey
        self.readVInt() #Appstore ID
        self.readStringReference() #ClientVersion
        self.readStringReference() #TencentOpenId
        self.readStringReference() #TencentToken
        self.readStringReference()
        self.readStringReference()
        self.readVInt() #TencentPlatform
        self.readStringReference() #DeviceVerifierResponse
        self.readStringReference() #AppLicensingSignature
        self.readStringReference() #DeviceVerifierResponse2
        self.readCompressedString() #SupercellIdToken
        self.readBoolean() #UpdateMaintenanceMode
        return self

    def execute(message, calling_instance, cryptoInit):
        if message.clientMajor != 26:
            loginFailedMessage = LoginFailedMessage(b'')
            loginFailedMessage.setErrorID(16)
            loginFailedMessage.setUpdateURL("https://google.cat")
            loginFailedMessage.setReason("Unsupported client version")
            Messaging.sendMessage(loginFailedMessage,calling_instance.client, cryptoInit)
            return
        print(f"[LoginMessage] Player {message.accountID} is trying to log in with token {message.passToken}")
        if message.accountID[1] == 0 or message.passToken == "":
            #calling_instance.db.getPlayerId(calling_instance.player)
            calling_instance.player.Token = Utility.generateToken()
        elif not calling_instance.db.findTokenInTable(message.passToken):
            calling_instance.player.Token = message.passToken
            calling_instance.player.ID = message.accountID
        else:
            calling_instance.player = calling_instance.db.loadInstance(message.passToken)
        calling_instance.player.ClientVersion = f'{str(message.clientMajor)}.{str(message.clientBuild)}.{str(message.clientMinor)}'
        #lastConnectionDay = daylight TODO convert to day to restart the stuff
        ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client)
        loginOkMessage = LoginOkMessage(b'')
        Messaging.sendMessage(loginOkMessage, calling_instance.client, cryptoInit, calling_instance)
        ownHomeDataMessage = OwnHomeDataMessage(b'')
        Messaging.sendMessage(ownHomeDataMessage, calling_instance.client, cryptoInit, calling_instance)
        myAllianceMessage = MyAllianceMessage(b'')
        Messaging.sendMessage(myAllianceMessage, calling_instance.client, cryptoInit, calling_instance)
        allianceWarMessage = AllianceWarMessage(b'')
        Messaging.sendMessage(allianceWarMessage, calling_instance.client, cryptoInit, calling_instance)

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion