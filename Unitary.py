from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)

# to get the Unitary of a curcuit
from qiskit.quantum_info import Operator
U = Operator(qc)
U.draw('latex')