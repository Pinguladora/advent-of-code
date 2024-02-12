from collections import deque
from hashlib import md5

def find_64th_key(salt: str) -> (int, str):
    keys = []
    # Sliding window size
    hash_window = deque(maxlen=1001)
    real_length = hash_window.maxlen - 1
    i=0
    while len(keys) != 64:
        hash_window.append(md5_hash(salt + str(i)))
        key = process_sliding_window(hash_window)
        if key:
            # Index are checked within the slide window, [... real i ...] current i, so i - (sliding window size-1) due to popleft
            keys.append((i - real_length, key))
        i+=1
    return keys[-1]

def find_64th_key_with_streching(salt: str, n_streching: int) -> (int, str):
    keys = []
    # Sliding window size
    hash_window = deque(maxlen=1001)
    real_length = hash_window.maxlen - 1
    i=0
    while len(keys) != 64:
        hash_val = md5_hash(salt + str(i))
        # Key streching with recursion
        hash_val = [hash_val:= md5_hash(hash_val) for _ in range(n_streching)][-1] 
        hash_window.append(hash_val)

        key = process_sliding_window(hash_window)
        if key:
            # Index are checked within the slide window, [... real i ...] current i, so i - (sliding window size-1) due to popleft
            keys.append((i - real_length, key))
        i+=1
    return keys[-1]

def process_sliding_window(hash_window: deque[str]) -> str | None:
    if len(hash_window) == 1001:
        potential_key = hash_window.popleft()
        triplet_char = find_triplet(potential_key)

        if triplet_char:
            if find_quintuplet(hash_window, triplet_char):
                return potential_key
    return None

def md5_hash(string: str) -> str:
    return md5(string.encode()).hexdigest()

def find_triplet(hash: str) -> str | None:
    for i in range(len(hash) - 2):
        # Check 1 by 1 to address for overlapping
        if hash[i] == hash[i + 1] == hash[i + 2]:
            return hash[i]
    return None

def find_quintuplet(hash_window: deque[str], char: str):
    for hash_str in hash_window:
        if char * 5 in hash_str:
            return True
    return False

if __name__ == "__main__":
    salt = "ngcjuoqr"

    #  First challenge
    key, hash = find_64th_key(salt)
    print("First challenge: 64th key index is", key)

    # Second challenge
    key, hash = find_64th_key_with_streching(salt, 2016)
    print("Second challenge: 64th key index is", key)

