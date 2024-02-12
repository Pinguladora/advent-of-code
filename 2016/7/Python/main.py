import re

PATTERN = re.compile(r'([^[\]]+)(?:\[([^\[\]]+)\])?')

def contains_abba(string: str) -> bool:
    is_abba = False
    for i in range(len(string) - 3):
        #  Need to address overlapping, so they need to be checked 1 by 1
        if string[i] != string[i+1] and string[i] == string[i+3] and string[i+1] == string[i+2]:
            is_abba = True
            break
    return is_abba


def supports_tls(supernets: list[str], hypernets: list[str]) -> int:
    #  Guard clause for hypernet 
    if any([contains_abba(hypernet) for hypernet in hypernets]):
        return 0
    
    return 1 if any(contains_abba(supernet) for supernet in supernets) else 0

def supports_ssl(supernets: list[str], hypernets: list[str]) -> int:
    abas = set()
    for supernet in supernets:
        for i in range(len(supernet) - 2):
            if supernet[i] != supernet[i+1] and supernet[i] == supernet[i+2]:
                abas.add(supernet[i:i+3])
    
    for hypernet in hypernets:
        for i in range(len(hypernet) - 2):
            if hypernet[i] != hypernet[i+1] and hypernet[i] == hypernet[i+2]:
                bab = hypernet[i+1] + hypernet[i] + hypernet[i+1]
                if bab in abas:
                    return 1
    return 0

def parse_line(line: str) -> (list[str], list[str]):
    line=line.rstrip()
    matches=re.findall(PATTERN, line)
    return [match[0] for match in matches], [match[1] for match in matches if match[1]]

def main(filepath: str) -> (int, int):
    ips_with_tls, ips_with_ssl= 0, 0
    with open(filepath, 'r') as f:
        for line in f:
            supernets, hypernets = parse_line(line)

            ips_with_tls+=supports_tls(supernets, hypernets)
            ips_with_ssl+=supports_ssl(supernets, hypernets)
    return ips_with_tls, ips_with_ssl

if __name__ == '__main__':
    filepath = "input.txt"

    ips_with_tls, ips_with_ssl = main(filepath)

    # First challenge
    print(f"{ips_with_tls} supports TLS")

    # Second challenge
    print(f"{ips_with_ssl} supports SSL")