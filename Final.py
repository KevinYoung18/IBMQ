import numpy as np
import qiskit as q
import math

print("Rock beat scissors, scissors beats paper, paper beats gun and gun beats rock ")
print("Any other combination results in a tie.")
print("However, antman entangles with the computer and returns an output for you that will not result in a tie")

backend = q.Aer.get_backend('qasm_simulator')

binary = {'00' : 'rock', '01' : 'scissors', '10' : 'paper', '11' : 'gun'}

qr = q.QuantumRegister(4)
cr = q.ClassicalRegister(4)
qc = q.QuantumCircuit(qr, cr)

str =""
while True:
    str = input("Enter rock, paper, scissors, gun or antman: ")
    if str == "rock":
        print("You", end=' ')
        qc.h(qr[0])
        qc.h(qr[1])
        break
    elif str == "paper":
        print("You", end=' ')
        qc.h(qr[0])
        qc.h(qr[1])
        qc.x(qr[2])
        break
    elif str == "scissors":
        print("You", end=' ')
        qc.h(qr[0])
        qc.h(qr[1])
        qc.x(qr[3])
        break
    elif str == "gun":
        print("You", end=' ')
        qc.h(qr[0])
        qc.h(qr[1])
        qc.x(qr[2])
        qc.x(qr[3])
        break
    elif str == "antman":
        print("Antman", end=' ')
        qc.h(qr[0])
        qc.h(qr[1])
        qc.cx(qr[0], qr[2])
        qc.cx(qr[1], qr[3])
        qc.x(qr[2])
        qc.x(qr[3])
        break
    else:
        print("Invalid input.")



qc.measure(qr, cr)
job = q.execute(qc, backend, shots =1)

results = job.result().get_counts()
result = ''
for r in results:
    result = r
if result == '0000' or  result == '1111' or  result == '0101' or  result == '1010' or result ==  '0010' or  result ==  '1000' or result ==  '1101' or result ==  '0111':
    you, comp = result[:math.floor(len(result)/2)], result[math.floor(len(result)/2):]
    print('chose', binary[you] , 'and the computer chose', binary[comp])
    print("Tie")
if result == '0001' or  result == '0110' or result ==  '1011' or result == '1100':
    you, comp = result[:math.floor(len(result)/2)], result[math.floor(len(result)/2):]
    print('chose', binary[you] , 'and the computer chose', binary[comp])
    print("You win!")
if result == '0100' or  result == '1001' or  result == '1110' or  result == '0011':
   you, comp = result[:math.floor(len(result)/2)], result[math.floor(len(result)/2):]
   print('chose', binary[you] , 'and the computer chose', binary[comp])
   print("You lose!")