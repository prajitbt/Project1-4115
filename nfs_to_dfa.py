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
keys_list = list(list(nfa.keys())[0])
paths = list(nfa[keys_list[0]].keys()) 


def find_first_row_dfa():
    dfa[keys_list[0]] = {}                      #creating a nested dictionary in dfa 
    for i in range(Total_transitions):
        var = "".join(nfa[keys_list[0]][paths[i]])   #Representing all elements in single string
        dfa[keys_list[0]][paths[i]] = var            #assigning the state in DFA table
        if var not in keys_list:                      
            new_states.append(var)                  
            keys_list.append(var)                       
        


def find_other_rows():
    while len(new_states) != 0:                     
        dfa[new_states[0]] = {}                     
        for _ in range(len(new_states[0])):
            for i in range(len(paths)):
                temp = []                                
                for j in range(len(new_states[0])):
                    temp += nfa[new_states[0][j]][paths[i]]  #taking the union of the states
                single_str = ""
                single_str = single_str.join(temp)                         
                if single_str not in keys_list:                   
                    new_states.append(single_str)            
                    keys_list.append(single_str)                  
                dfa[new_states[0]][paths[i]] = single_str   
        
        new_states.remove(new_states[0])    
def print_dfa():
    print("\nDFA :- \n")    
    print(dfa)                                           #Print the DFA
    print("\nPrinting DFA table :- ")
    dfa_table = pd.DataFrame(dfa)
    print(dfa_table.transpose())



    dfa_final_states = []

def find_dfa_final_state():
    dfa_states = list(dfa.keys())
    for x in dfa_states:
        for i in x:
            if i in nfa_final_state:
                dfa_final_states.append(x)
                break


def main():
    print_nfa()
    find_first_row_dfa()
    find_other_rows()
    print_dfa()
    find_dfa_final_state()

    print("\nFinal states of the DFA: ",dfa_final_states) 


if __name__ == '__main__':
    main()
