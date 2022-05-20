from Services.DesignFA import DesignFA
class NfaToDfa:
    def __init__(self,state,symbols,start_state,final_state,transition):
        self.state = state
        self.symbols = symbols
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
    def addNewNameTransition(self):
        state = self.state
        new_state = state[-1]
        while new_state in state:
            new_state = state[-1]+'1'
            tmp = 0
            tmp_s =''
            for i in new_state:
                if i.isnumeric():
                    tmp+=int(i)
                else: tmp_s+=i
            new_state = tmp_s+str(tmp)
        return new_state
    def countNumberOfTransition(self):
        for i in self.transition.values():
            for j in i.values():
                if len(j) > 1:
                    return True
        return False
    def checkEpsilonTransition(self):
        epsilon_state = []
        for i in self.transition:
            if 'E' in self.symbols:
                if len(self.transition[i]['E']) > 0:
                    epsilon_state.append(i)
        return epsilon_state
    def checkTransition(self,symbol,state):
        epsilon_state = self.checkEpsilonTransition()
        checktypetransition = self.countNumberOfTransition()
        tmp_state = []
        for i in state:
            if checktypetransition == False and i not in self.state:
                tmp_state.append(i)
            else:
                transition = self.transition[i][symbol]
                if len(transition) == 0 and checktypetransition == False:
                    transition.append(self.addNewNameTransition())
                for j in transition:
                    if j in epsilon_state:
                        for k in self.transition[j]['E']:
                            if k or k!='':
                                transition.append(k)
                transition.sort()
                if len(transition) > 0:
                    for j in transition:
                        if j not in tmp_state:
                            tmp_state.append(j)
        return tmp_state

    def generateNewTransition(self):
        epsilon_state = self.checkEpsilonTransition()
        state = self.state.copy()
        final_state = self.final_state.copy()
        symbols = self.symbols.copy()
        if 'E' in symbols:
            symbols.remove('E')
        start_state = self.start_state.copy()
        totest_state = []
        totest_state.append(self.start_state.copy())
        if start_state[0] in epsilon_state:
            for i in self.transition[start_state[0]]['E']:
                start_state[0] = start_state[0] + i
                totest_state[0].append(i)
        transition = self.transition.copy()

        new_final_state = []
        new_start_state = start_state.copy()


        new_transition = {}
        total_newstate = []
        total_newstate.append(start_state[0])

        for i in totest_state:
            now_state = ''.join(str(item) for item in i)
            new_transition[now_state] = {}
            for j in symbols:
                s = self.checkTransition(j,i)
                s_string = ''.join(str(item) for item in s)
                if s not in totest_state:
                    totest_state.append(s)
                    total_newstate.append(s_string)
                #generate final state
                if self.generateFinalState(s) == True:
                    if s_string not in new_final_state:
                        new_final_state.append(s_string)
                new_transition[now_state][j] = [''.join(str(item) for item in s)]

        return total_newstate,new_transition,symbols,new_start_state,new_final_state

    def generateFinalState(self,state):
        final_state = self.final_state.copy()
        for i in final_state:
            if i in state:
                return True
        return False
    def generateStartState(self,state):
        start_state = self.start_state.copy()
        for i in start_state:
            if i in state:
                return True
        return False
    def generateDataFrame(self,fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition): #return to user as transition table
        fa = DesignFA(fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition)
        dfa = fa.convertFaToDataframe()
        return dfa
    def exec(self):
        new_state,new_transition,new_symbols,new_start_state,new_final_state = self.generateNewTransition()
        print(new_state)
        print(new_symbols)
        print(new_start_state)
        print(new_final_state)
        df = self.generateDataFrame(new_state,new_symbols,new_start_state,new_final_state,new_transition)
        print(df)

FA = NfaToDfa(
    ['q0','q1','q2','q3'],
    ['a','b','E'],
    ['q0'],
    ['q3'],
    {
        'q0':{
            'a':['q0'],
            'b':['q0','q1'],
            'E':['q3']
        },
        'q1': {
            'a': ['q2'],
            'b': ['q2'],
            'E': ['q2']
        },
        'q2': {
            'a': ['q3'],
            'b': ['q3'],
            'E': []
        },
        'q3': {
            'a': [],
            'b': [],
            'E': []
        }
    }
)
# FA = NfaToDfa(
#     ['q0','q1','q2'],
#     ['a','b'],
#     ['q0'],
#     ['q2'],
#     {
#         'q0':{
#             'a':[],
#             'b':['q1']
#         },
#         'q1': {
#             'a': [],
#             'b': ['q2']
#         },
#         'q2': {
#             'a': [],
#             'b': ['q2']
#         }
#     }
# )
# FA.addNewNameTransition()
FA.exec()
# l = ['a']
# for i in l:
#     print(i)
#     if len(l) < 5:
#         l.append('a')