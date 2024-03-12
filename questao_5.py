def inverter(string: str) -> str:
    inverted = []
    for l in string:
        inverted.insert(0, l)
    return ''.join(inverted)

print(inverter('ola'))
print(inverter('target sistemas'))
print(inverter('tenet'))
print(inverter('socorram me subi no onibus em marrocos'))