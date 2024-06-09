from qiskit import QuantumCircuit

qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
qc.draw()

# State vector 
from qiskit.quantum_info import Statevector
stateVector = Statevector(qc)
stateVector.draw('latex')

