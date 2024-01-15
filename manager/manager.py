import hashlib
import encryption

class Manager:
    def __init__(self, database, key, user):
        self.database = database
        self.key = key
        self.uid = hashlib.sha256(user.encode('utf-8')).hexdigest()

    def get_password(self, host):
        cipher_text = self.database.get_password(host, self.uid)   
        plain_text = encryption.AES_CBC(self.key).decrypt(cipher_text[0])
        password = plain_text.decode('utf-8')        
        return password 

    def set_password(self, host, password):
        enc_password = password.encode('utf-8')
        cipher_text = encryption.AES_CBC(self.key).encrypt(enc_password)
        self.database.set_password(host, cipher_text, self.uid)

    def update_password(self, host, old_password, new_password):
        pass        
