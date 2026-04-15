import traceback
from Classes.Packets.PiranhaMessage import PiranhaMessage

class Messaging:
    def writeHeader(message, payloadLen):
        message.messageBuffer += message.getMessageType().to_bytes(2, 'big', signed=True)
        message.messageBuffer += payloadLen.to_bytes(3, 'big', signed=True)
        message.messageBuffer += message.messageVersion.to_bytes(2, 'big', signed=True)

    def readHeader(headerBytes):
        headerData = []
        headerData.append(int.from_bytes(headerBytes[:2], 'big', signed=True))
        headerData.append(int.from_bytes(headerBytes[2:5], 'big', signed=True))
        return headerData

    def sendMessage(message: PiranhaMessage, clientConnection, cryptoInit,  calling_instance=None):
        if calling_instance is not None:
            message.encode(calling_instance)
        else:
            message.encode()
        Messaging.writeHeader(message, len(message.messagePayload))
        message.messageBuffer += message.messagePayload
        try:
            clientConnection.send(message.messageBuffer)
        except Exception:
            print(traceback.format_exc())