from Classes.Messaging import Messaging
from Classes.Packets.Server.Authentification.OutOfSyncMessage import OutOfSyncMessage
from Classes.Packets.PiranhaMessage import PiranhaMessage
from time import time

class MatchmakeRequestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
        self.target = []
        self.index = [0,1]
        self.requestType = 3
        self.ticketsInput = 0

    def encode(self):
        self.writeDataReference(*self.target)
        self.writeVInt(self.requestType)
        self.writeVInt(self.index[0])
        self.writeVInt(self.index[1])
        self.writeVInt(self.ticketsInput)

    def decode(self):
        """With my method to get this packet on offline battles you cannot get the brawler apparently"""
        self.target = self.readDataReference()
        self.requestType = self.readVInt()
        self.index[0] = self.readVInt()
        self.index[1] = self.readVInt()
        self.ticketsInput = self.readVInt()
        return self

    def execute(message, calling_instance, cryptoInit):
        if message.index[1] == 6:
            tickets = [1, 2, 3, 4, 5, 10, 15, 20]
            selectedTicket = tickets[message.ticketsInput]
            print("You paid " + str(selectedTicket) + " tickets!")
            if calling_instance.player.Tickets<selectedTicket:
                outOfSyncMessage = OutOfSyncMessage(b'')
                Messaging.sendMessage(outOfSyncMessage, calling_instance.client, cryptoInit)
            else:
                calling_instance.player.selectedTickets = selectedTicket
                calling_instance.player.ticketEventTime = time()
        elif message.index[1]== 9:
            calling_instance.player.isInPowerPlay = True
        calling_instance.player.isInRealGame = True

                

    def getMessageType(self):
        return 14103

    def getMessageVersion(self):
        return self.messageVersion
