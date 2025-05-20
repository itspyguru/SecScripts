import telnetlib3

def telnet_bruteforce(host, port, username, password):
    """
    Attempt to brute force Telnet login using the provided credentials.
    
    :param host: The target host IP address or hostname.
    :param port: The Telnet port (default is 23).
    :param username: The Telnet username to attempt.
    :param password: The Telnet password to attempt.
    :return: True if login is successful, False otherwise.
    """
    try:
        # Create a Telnet connection
        telnet = telnetlib3.Telnet(host, port)
        
        # Attempt to login
        telnet.login(username, password)
        
        # Check if login was successful
        if telnet.is_authenticated():
            print(f"Telnet session opened with {username}:{password}")
            return True
        else:
            print(f"Login failed with {username}:{password}")
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        telnet.close()