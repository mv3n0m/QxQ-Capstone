import cirq
from . import basis_gates, get_qubits


def decrypt_message(encrypted_circuit, num_bits, private_key, bases):
    qubits = get_qubits(num_bits)

    circuit = cirq.Circuit()
    for idx in range(num_bits):
        basis_value = bases[idx]
        basis_gate = basis_gates[basis_value]

        qubit = qubits[idx]
        circuit.append(basis_gate(qubit))

    circuit.append(cirq.measure(qubits, key=private_key))

    bb84_circuit = encrypted_circuit + circuit

    sim = cirq.Simulator()
    results = sim.run(bb84_circuit)
    key = results.measurements[private_key][0]

    return key
