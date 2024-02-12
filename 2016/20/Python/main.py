def find_lowest_allowed_ip_sort_merge(blacklisted_ranges: list[list[int]]) -> int:
    # Sort ranges by range start boundary
    blacklisted_ranges.sort()
    current_range = blacklisted_ranges.pop(0)
    lowest_allowed = 0

    for start, end in blacklisted_ranges:
        range_end = current_range[1]
        if start <= range_end + 1:
            current_range[1] = max(range_end, end)
            continue
        # A gap was found
        lowest_allowed = range_end + 1
        break 
    return lowest_allowed

def count_allowed_ips_sort_merge(max_value: int, blacklisted_ranges: list[list[int]]) -> int:
    blacklisted_ranges.sort()
    current_range = blacklisted_ranges.pop(0)
    allowed = 0

    for start, end in blacklisted_ranges:
        range_end = current_range[1]
        if start <= range_end + 1:
            current_range[1] = max(range_end, end)
        else:
            # A gap was found, add all of its ips
            gap_size = start - range_end - 1
            allowed += gap_size
            current_range = [start, end]
    # Possible gap after the last range 
    last_gap = max_value-current_range[1] 
    return allowed + last_gap

def read_blacklist(filepath: str) -> list[list[int]]:
    with open(filepath, 'rt') as f:
        return [list(map(int, line.rstrip().split("-"))) for line in f]

if __name__ == "__main__":
    filepath = "input.txt"
    blacklist=read_blacklist(filepath)

    # First challenge
    lowest_ip=find_lowest_allowed_ip_sort_merge(blacklist)
    print(f"The lowest-valued IP which isn't blocked is {lowest_ip}")

    # Second challenge
    allowed_ips=count_allowed_ips_sort_merge(2**32-1, blacklist)
    print(f"The number of allowed IPs is {allowed_ips}")
