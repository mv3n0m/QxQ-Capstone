import cirq
from random import choices

encode_gates = { 0: cirq.I, 1: cirq.X }
basis_gates = { 'X': cirq.H, 'Y': cirq.Y, 'Z': cirq.I }

get_qubits = lambda n: cirq.NamedQubit.range(n, prefix='q')


def text_to_bits(text):
    bits = ''.join(format(ord(char), '08b') for char in text)
    return [int(bit) for bit in bits]

def bits_to_text(bits):
    text = ''.join(chr(int(''.join(map(str, bits[i:i+8])), 2)) for i in range(0, len(bits), 8))
    return text
