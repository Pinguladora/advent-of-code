from collections import Counter
from string import ascii_lowercase

ALPHABET_SIZE=len(ascii_lowercase)

def parse_line(line: str) -> (str, int, str):
    line = line.split("-")
    # Parse line
    encrypted_name=line[:-1]
    encrypted_name="".join(encrypted_name)
    sector_id, checksum = line[-1].split("[")
    checksum=checksum[:-1]
    return encrypted_name, int(sector_id), checksum

def is_real_room(encrypted_name: str, checksum: str) -> bool:
    char_count=Counter(encrypted_name)
    char_count=sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    # Check against the checksum
    return True if all(map(lambda x: x[0] in checksum, char_count[:5])) else False

def main(filepath: str, room_name: str) -> (int, int):
    sum_ids=0
    secret_room_id=-1
    msg_found=False

    with open(filepath, 'rt') as f:
        for line in f:
            encrypted_name, sector_id, checksum = parse_line(line)
            if is_real_room(encrypted_name, checksum):
                sum_ids+=sector_id
                if not msg_found:
                    dec_msg=decrypt_shift_cipher(encrypted_name, sector_id)
                    secret_room_id = sector_id if (dec_msg == room_name) else secret_room_id
    return sum_ids, secret_room_id
        
def decrypt_shift_cipher(msg: str, sector_id: int) -> str:
    res=[]
    for char in msg:
        char_pos=ascii_lowercase.index(char)
        real_char=ascii_lowercase[(char_pos+sector_id) % ALPHABET_SIZE]
        res.append(real_char)
    return "".join(res)

if __name__ == "__main__":
    filepath = "input.txt"
    # I had to print all of the deciphered messages in order to know what to search for
    secret_room = "northpoleobjectstorage"

    sum_ids, secret_room_id=main(filepath, secret_room)

    # First challenge
    print(f"The sum of the sector IDs of the real rooms is {sum_ids}")

    # Second challenge
    print(f"The sector ID of the room where North Pole objects are stored is {secret_room_id}")
