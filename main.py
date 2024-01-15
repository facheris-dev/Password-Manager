import argparse
import db
import manager

def init_cli_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(       
        prog='PassMan',
        usage='%(prog)s [OPTION] [FILE]...',
        description="Manages your personal keys.",
        epilog='Check out the github for more information.'
    )

    # Add the user argument, used to verify the current user.
    parser.add_argument(
        '-u',
        '--user',
        required=True
    )
    
    # Add the host command
    parser.add_argument(
        '--host',
        required=True
    )
      
    return parser

# Retrieves a stored user key on the local machine.
def get_user_key() -> str:
    key = ''

    try:
        with open('.key', mode='r', encoding='utf-8') as key_file:
            key = key_file.read()
    except  FileNotFoundError as err:
        print('Unable to locate the .key file, please generate your key and save it in the current directory.')
        exit()

    return key
    
if __name__ == '__main__':
    # Initialize the parser for our command line args
    parser = init_cli_args()

    # Get the args
    args = parser.parse_args()
   
    # Get the user
    user = args.user

    # Get the host
    host = args.host
 
    # Get the users key, if the key doesn't exist prompt the user to 
    # generate a key file.
    key = get_user_key()
    
    # Create the database, and pass the control to the manager.
    database = db.Database()

    manager = manager.Manager(database, key, user) 

    # TEST
    print(manager.get_password(host))

    # Close the database
    database.close()        
