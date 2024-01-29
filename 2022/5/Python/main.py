def find_marker(message: str, n: int) -> int:
    msg_size = len(message)
    for i in range(0, msg_size):
        if len(set(message[i:i+n])) == n:
            return i+n


def read_file(filepath: str) -> str:
    with open(filepath, 'rt') as f:
        return f.read()
    
if __name__ == "__main__":
    filepath = "input.txt"
    message=read_file(filepath)

    # First challenge
    sol=find_marker(message, 4)
    print(f"{sol} characters needs to be processed before the first start-of-packet marker is detected")

    # Second challenge
    sol=find_marker(message, 14)
    print(f"{sol} characters needs to be processed before the first start-of-message is detected")