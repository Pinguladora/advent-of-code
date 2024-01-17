# Double quotes
print(len('""'))
print(len(""))
line=""
print(len(rf"'{line.encode()}'"))
print(len(line))

# Abc
print(len('"abc"'))
print(len("abc"))
line="abc"
print(len(rf"'{line.encode()}'"))
print(len(line))

# String with backslah
print(len(r'"aaa\"aaa"'))
print(len("aaa\"aaa"))
line="aaa\"aaa"
print(len(rf"'{line.encode()}'"))
print(len(line))

# Hex
line=b"\x27"
var=rf"'{line}'"
var=repr(r"\x27")
print(len(var))
print(len(line))
line=rf'\"{line}\"'
print(line)
print(line(len))