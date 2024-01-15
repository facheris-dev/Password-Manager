import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('example.db')
        self.cur = self.connection.cursor()
    
    def close(self):
        self.connection.close()

    def create_user(self, user, key):
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO USERS VALUES
                        (?, ?)
                """, [(user, key)])
        except sqlite3.OperationalError as err:
            print('Their was an error creating the user, the table does not exist.')
   
    # Set a user password in the table
    def set_password(self, host, password, key):
        try:
            with self.connection:
                self.connection.execute("""
                    INSERT INTO PASSWORDS VALUES
                        (?, ?, ?)
                """, (password, key, host,))
        except sqlite3.IntegrityError as err:
            print('Unable to insert this host/key pair, it already exists. Try updating the password instead.')
    
    # Obtain a single user password entry from the password table
    def get_password(self, host, key):
        password = ''

        try:
            with self.connection:
                password = self.connection.execute('SELECT password FROM PASSWORDS where host = ? and key = ?', [host, key]).fetchone()
        except sqlite3.OperationalError as err:
            print('Unable to retrieve password, operational error.')

        return password

    

    
