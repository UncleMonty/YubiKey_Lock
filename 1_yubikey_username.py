import os
import time

def main():
    try:
        # Use the getpass module to get the username
        username = os.getlogin()
        print(f"Detected Username: {username}")
        #return username
    
    except OSError:
        print("Unable to retrieve the username.")
        return None
    time.sleep(30) 

if __name__ == "__main__":
    main()
