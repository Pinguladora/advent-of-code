from hashlib import md5

PREDICATE = "00000"
ALLOWED_POSITIONS = {"0", "1", "2", "3", "4", "5", "6", "7"}

# This can be solved in a more efficient way by using "parallelism" (multiprocessing bc of CPython GIL), splitting the search without collisions
# I stick with this for simplicity, so please don't take this as an efficient solution

def find_password_by_predicate(door_id: int, n: int) -> str:
    i=0
    password=[]
    while len(password)!=n:
        to_hash=f"{door_id}{i}".encode()
        hashed_hex=md5(to_hash).hexdigest()
        if hashed_hex.startswith(PREDICATE):
            password.append(hashed_hex[5])
        i+=1
    return "".join(password)


def find_password_by_predicate_and_positions(door_id: int, n: int) -> str:
    i=0
    password=["-"]*n
    while n!=0:
        to_hash=f"{door_id}{i}".encode()
        hashed_hex=md5(to_hash).hexdigest()
        if hashed_hex.startswith(PREDICATE):
            char_idx=hashed_hex[5]
            if char_idx in ALLOWED_POSITIONS:
                char_idx=int(char_idx)
                if password[char_idx] == "-":
                    password[char_idx]=hashed_hex[6]
                    n-=1
        i+=1
    return "".join(password)

def main() -> None:
    door_id = "wtnhxymk"

    # First challenge
    password=find_password_by_predicate(door_id, 8)
    print(f"First challenge: the password is {password}")

    # Second challenge
    password=find_password_by_predicate_and_positions(door_id, 8)
    print(f"Second challenge: the password is {password}")     

if __name__ == "__main__":   
    main()
