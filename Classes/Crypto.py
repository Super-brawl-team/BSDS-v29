from os import urandom
from hashlib import blake2b
from _tweetnacl import (crypto_box_beforenm, crypto_scalarmult_base, crypto_box_NONCEBYTES, crypto_secretbox, crypto_secretbox_open)

class Nonce:
    def __init__(self, nonce=None, clientKey=None, serverKey=None):
        if not clientKey:
            if nonce:
                self._nonce = nonce
            else:
                self._nonce = urandom(crypto_box_NONCEBYTES)
        else:
            b2 = blake2b(digest_size=24)
            if nonce:
                b2.update(bytes(nonce))
            b2.update(bytes(clientKey))
            b2.update(serverKey)
            self._nonce = b2.digest()
    
    def __bytes__(self):
        return self._nonce
    def __len__(self):
        return len(self._nonce)
    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(crypto_box_NONCEBYTES, 'little')

    
class Crypto:
    def __init__(self):
        self.authenticated = False
        self.client_secret_key = bytes.fromhex("BB14D6FD2B7C9823EAEDB4338CB7237F61E422D23C4977F74ADA052702C0C62D")
        self.server_public_key = bytes.fromhex("0C60170E51746626A27683BF1619467A3C8BBCF9785C4899358EF71A3384CD74") # crypto_scalarmult_base of server private key
        self.client_public_key = None
        self.session_key = None
        self.shared_encryption_key = bytes(urandom(32))
        self.decryptNonce = None
        self.encryptNonce = Nonce(urandom(24))
        self.nonce = None
        self.s = None
    
    def decryptClient(self, packet_id, payload):
        if packet_id == 10100:
            return payload
        elif packet_id == 10101:
            self.authenticated = True
            self.client_public_key = bytes(payload[:32])
            if payload[:32] != self.client_public_key:
                raise self.CryptographyError(f"Client public key does not match! client public key: {self.client_public_key}, message (10101) key: {payload[:32]}")
            self.nonce = Nonce(clientKey=self.client_public_key, serverKey=self.server_public_key)
            self.s = crypto_box_beforenm(self.server_public_key, self.client_secret_key)
            payload = bytes(payload[32:])
            decrypted = crypto_secretbox_open(payload, bytes(self.nonce), self.s)
            if decrypted[:24] != self.session_key:
                raise self.CryptographyError("LoginMessage SessionKey does not match with server key!")
            self.decryptNonce = Nonce(decrypted[24:48])
            return decrypted[48:]
        elif self.decryptNonce is None:
            return payload
        else:
            if not self.authenticated: raise self.CryptographyError("Client Session has not passed authentication yet!")
            self.decryptNonce.increment()
            decrypted = crypto_secretbox_open(payload, bytes(self.decryptNonce), self.shared_encryption_key)
            return decrypted

    def encryptServer(self, packet_id, payload):
        if packet_id == 20100:
            return payload
        elif packet_id == 20103 and self.authenticated == False:
            return payload
        else:
            if packet_id == 20104 or packet_id == 20103:
                nonce = Nonce(self.decryptNonce, clientKey=self.client_public_key, serverKey=self.server_public_key)
                payload = bytes(self.encryptNonce) + self.shared_encryption_key + payload
                encrypted = crypto_secretbox(payload, bytes(nonce), self.s)
                return encrypted
            else:
                self.encryptNonce.increment()
                encrypted = crypto_secretbox(payload, bytes(self.encryptNonce), self.shared_encryption_key)
                return encrypted
            
    def setSessionKey(self, sessionKey):
        self.session_key = sessionKey