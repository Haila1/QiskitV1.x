from qiskit import QuantumCircuit

qc = QuantumCircuit(2,2)
qc.h(0)
qc.measure(0,0)


from qiskit.providers.basic_provider import BasicSimulator 


# to store the results for each excution 
job = BasicSimulator().run(qc, shots=5, memory= True)

# stor the result
result = job.result()

# get the memory
result_memory = result.get_memory()
print(result_memory)