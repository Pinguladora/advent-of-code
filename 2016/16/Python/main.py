def calc_checksum(state: str) -> str:
    # res=[]
    # for i in range(0, len(state),2):
    #     pair=state[i:i+2]
    #     if len(set(pair)) == 1:
    #         res.append("1")
    #         continue
    #     res.append("0")

    # One-liner
    res=["1" if len(set(state[i:i+2])) == 1 else "0" for i in range(0, len(state), 2)]
    return "".join(res)

def custom_dragon_curve(state: str) -> str:
    # This works because string is an inmutable data type on Python
    a=state
    b=a
    b=a[::-1]
    b="".join("1" if bit == "0" else "0" for bit in b)
    return "0".join([a,b])

def main(initial_state: str, disk_size: int) -> str:
    # Calculate state
    data=custom_dragon_curve(initial_state)
    while len(data) < disk_size:
        data=custom_dragon_curve(data)

    # Calculate checksum
    checksum=calc_checksum(data[:disk_size])
    while len(checksum) % 2 == 0:
        checksum = calc_checksum(checksum)
    return checksum

if __name__ == "__main__":
    initial_state = "01111010110010011"

    #  First challenge
    disk_size = 272
    checksum=main(initial_state, disk_size)
    print(f"First challenge: the correct checksum is {checksum}")

    #  Second challenge
    disk_size = 35651584
    checksum=main(initial_state, disk_size)
    print(f"Second challenge: the correct checksum is {checksum}")
