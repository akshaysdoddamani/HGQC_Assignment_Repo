#importing riquired modules
import numpy as np
import random as rn

#intialising to ket notation
def intialise_qubit_to_ket(alpha,beta):
    ket_qubit = np.array([[alpha], [beta]])#creating a coloum vector
    return ket_qubit

#checking the function
print(intialise_qubit_to_ket(0+0.6j,0-0.8j))

#intialising_to_bra_notation
def intialise_qubit_to_bra(alpha,beta):
    ket_qubit = intialise_qubit_to_ket(alpha,beta)
    bra_qubit = ket_qubit.conjugate().transpose()
    return bra_qubit

#checking the function
print(intialise_qubit_to_bra(0+0.6j,0-0.8j))

#checking validity
def check_validity(alpha,beta):
    ket_qubit = intialise_qubit_to_ket(alpha,beta)
    bra_qubit = intialise_qubit_to_bra(alpha,beta)
    #matrix multiplication
    bra_ket = np.dot(bra_qubit,ket_qubit)
    if bra_ket[0] == 1:
        print('valid pair of alpha and beta')
    else:
        print('invalid pair of alpha and beta')

#checking the function
check_validity(0+0.6j,0-0.8j)
check_validity(0+0.4j,0-0.5j)

#constructing standard basis
def construct_standard_basis(n):#n is no. of qubit
    basis_vector_list = []
    for i in range(2**n):
        #using binary number notation
        basis = '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
        basis_vector_list.append(basis)
    return basis_vector_list

#checcking the function
print(construct_standard_basis(4))


#creating a function to convert array into list
def convt(array):#argument is column matrix
    if np.size(array,axis=0) == 1:
        nest_lst = array.tolist()
    elif np.size(array,axis=1) == 1:
        array_1 = array.transpose()
        nest_lst = array_1.tolist()
    return nest_lst[0]


#forming a combined state
def combine_state(qubit_state1,qubit_state2):#arguments are array with coloum vectors
    qubit_state1_list = convt(qubit_state1)
    qubit_state2_row = qubit_state2.transpose()
    qubit_combined_state = []
    for i in range(len(qubit_state1_list)):
        qubit_combined_state_1 = convt(qubit_state1_list[i]*qubit_state2_row)
        qubit_combined_state = qubit_combined_state+qubit_combined_state_1
    combined_state_coloum = np.array([np.asarray(qubit_combined_state)])
    combined_state1 = combined_state_coloum.transpose()
    return combined_state1

#checking the function
qubit_1 = np.array([[0],[1]])
qubit_2 = np.array([[1],[0]])
print(combine_state(qubit_1,qubit_2))


#measure a single qubit
def measure_single(qubit1,generalstate):#the arguments are array with pre-mutliplier as the elements
        measure_qubit_list = convt(np.dot(qubit1.transpose(),generalstate))
        measure_qubit = measure_qubit_list[0]
        return measure_qubit


#checking the function
qubit_1 = np.array([[0.6],[0.8]])
qubit_2 = np.array([[1/2**5],[1/2**5]])
print(measure_single(qubit_1,qubit_2))

#measure multiple qubit
def measure_multiple(qubits):#the arugment are array
    n = len(convt(qubits))
    random_state = rn.randint(2, n-1)
    if random_state == n-1:
        part_1 = convt(np.zeros([1, n-1], dtype = int))
        part_2 = [1]
        standard_state_list = part_1 + part_2
    else:
        part_1 = convt(np.zeros([1, random_state], dtype = int))
        part_2 = [1]
        part_3 = convt(np.zeros([1, n - random_state-1], dtype = int))
        standard_state_list = part_1 + part_2 + part_3
    standard_state = np.array([np.asarray(standard_state_list)])
    measure_qubit_list = convt(np.dot(qubits.transpose(),standard_state.transpose() ))
    measure_qubit = measure_qubit_list[0]
    return measure_qubit

#checking the function
qubit_1 = np.array([[0],[0],[1],[0]])
print(measure_multiple(qubit_1))
