import pandas as pd

#Defining variables for NFA which accepts set of strings over 0, 1 which ends with 1

nfa = {}                                 
Total_states = 2
Total_transitions = 2
nfa = {'A': { '0': ['A'], '1': ['A', 'B']}, 'B': {'0': [], '1': []}}
nfa_final_state = ['B']

def print_nfa():
    print("\nNFA :- \n")
    print(nfa)                                    #Printing NFA
    print("\nNFA table : ")
    nfa_table_visualize = pd.DataFrame(nfa)
    print(nfa_table_visualize.transpose())
    print("\nNFA Final State : ", nfa_final_state)



                 
    
new_states = []                       
dfa = {} 
