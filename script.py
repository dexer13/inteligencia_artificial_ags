import re


def print_hex(value):
    matches = re.findall(r'([#]([0-9]|[A-F]|[a-f]){6}|[#]([0-9]|[A-F]|[a-f]){3})(?!([0-9]|[A-Z]|[a-z]))', value)
    for match in matches:
        for m in match:
            if len(m) in [4, 7]:
                print(m)


is_selector = True
lines = int(input())

while lines > 0:
    input()
    input()
    lines -= 2
    line = input()
    lines -= 1
    while line != '}':
        fields = line.split(';')
        for field in fields:
            if field:
                print_hex(field.split(':')[1])
        line = input()
        lines -= 1


