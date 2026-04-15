import traceback
from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Messaging import Messaging
from Classes.Packets.Server.Home.LobbyInfoMessage import LobbyInfoMessage

class MessageManager:
    def receiveMessage(self, messageType, messagePayload, cryptoInit):
        message = LogicLaserMessageFactory.createMessageByType(messageType, messagePayload)
        if message is not None:
            try:
                if message.isServerToClient():
                    message.encode()
                else:
                    message.decode()
                    message.execute(self, cryptoInit)

            except Exception:
                print(traceback.format_exc())
        if messageType > 10100:
            lobbyInfoMessage = LobbyInfoMessage(b'')
            Messaging.sendMessage(lobbyInfoMessage, self.client, cryptoInit, self)