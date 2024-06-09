# Create a quantum circuit that generates an entangled pair of qubits.
from qiskit import QuantumCircuit

# Create a quantum circuit with two qubits
qc = QuantumCircuit(2, 2)

# Create an entangled pair
# first bellState
qc.h(0)
qc.cx(0, 1)
qc.draw('mpl')

# the intanglment Qsphere
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere
stateVector = Statevector(qc)
plot_state_qsphere(stateVector)
