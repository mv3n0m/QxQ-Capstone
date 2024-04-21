import cirq
from . import encode_gates, basis_gates, get_qubits


def encrypt_message(message_bits, num_bits, bases):
    qubits = get_qubits(num_bits)

    circuit = cirq.Circuit()
    for idx in range(num_bits):
        encode_value = message_bits[idx]
        encode_gate = encode_gates[encode_value]

        basis_value = bases[idx]
        basis_gate = basis_gates[basis_value]

        qubit = qubits[idx]
        circuit.append(encode_gate(qubit))
        circuit.append(basis_gate(qubit))

    return circuit
