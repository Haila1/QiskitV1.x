from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
from qiskit.providers.basic_provider import BasicSimulator 
qc = QuantumCircuit(3)

# connect the QFT oracle to the curcit 
qc.append(QFT(3), [0,1,2])
qc.measure_all()
qc.draw()

# get the backend to qc 
from qiskit import transpile

transpiled_qc = transpile(qc, backend=BasicSimulator())

job = BasicSimulator().run(transpiled_qc)
result = job.result()
count = result.get_counts()

print(count)
