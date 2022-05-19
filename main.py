import numpy as np
import pandas as pd
from Services.DefineFAType import DefineFAType
from Services.FAStringTesting import FAStringTesting
from Services.NfaToDfa import NfaToDfa
from Services.MinimizeDfa import MinimizeDfa
from Services.DesignFA import DesignFA

def divider():
    print(*["-" for i in range(20)])

print("Welcome to FA Operation:")

fa_state = []
fa_symbols = []
fa_start_state = []
fa_final_state = []
fa_transition={}


divider()

print("Please Input your FA:")
input_name = [" 1. Input all states (e.g: q0,q1,q2,q3) : ",
              " 2. Input all symbols (e.g: 0,1) : ",
              " 3. Input a start states (e.g: q0) : ",
              " 4. Input the final states (e.g: q1,q2) : "
            ]
tmp = []

for i in input_name: tmp.append(input(i).split(','))

fa_state, fa_symbols, fa_start_state, fa_final_state = tmp

divider()

print("Please Input your FA transition:")
print("Note: \n 1. If null transition please click enter"
      + "\n 2. If more than a transition state please input e.g: q0,q1")
for i in fa_state:
    fa_transition[i] = {}
    for j in fa_symbols:
        each_tran = input("Input transition of "+i+" state by "+"symbol "+j+" : ")
        fa_transition[i][j] = each_tran.split(',')

print(fa_transition)


divider()

print("----------Your FA----------")
print("States:", fa_state)
print("Symbols:", fa_symbols)
print("Start state:", str(*fa_start_state))
print("Final state:", fa_final_state)
print("FA table transition:")
FA_table_transition = DesignFA(
    fa_state,
    fa_symbols,
    fa_start_state,
    fa_final_state,
    fa_transition
)
print(FA_table_transition.convertFaToDataframe())

divider()

while True:
    print("Functionality:")
    func_name = [" 1.Define FA Type","2.FA String Testing","3.Convert from NFA to DFA","4.Minimize DFA", "Q.Exit"]
    print(*[name+"\n" for name in func_name])

    divider()

    choosed_function = input("Please choose a functionality by input the functionality number : ")
    if choosed_function == '1':
        FA = DefineFAType(fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition)
        print("Your FA type is : " , FA.define())
        divider()
    elif choosed_function == '2':
        string = input("Input your testing string e.g : abba : ")
        FA = FAStringTesting(string,fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition)
        print(FA.stringTesting())
        divider()
    elif choosed_function == '3':
        FA = NfaToDfa()
        divider()
    elif choosed_function == '4':
        FA = MinimizeDfa(fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition)
        print(FA.exce())
        divider()
    elif choosed_function.lower() == 'q':
        print("You're exiting the program.......")
        break
    else:
        print("Please input the right number")
