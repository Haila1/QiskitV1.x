# append oracle to curcuit 
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT 
qc = QuantumCircuit(3)

# connect the QFT oracle to the curcit 
qc.append(QFT(3), [0,1,2])
qc.measure_all()
qc.draw()


