class FAStringTesting:
    def __init__(self,string,state,symbols,start_state,final_state,transition):
        self.string = string
        self.state = state
        self.symbols = symbols
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
    def getAvailableTransition(self,state):
        transition = []
        for i in self.transition[state]:
            for j in self.transition[state][i]:
                 transition.append(i)
        return transition
    def stringTesting(self):
        state_process = self.start_state[0]
        for i in self.string:
            transition = self.getAvailableTransition(state_process)
            if i in transition:
                state_process = self.transition[state_process][i][0]
                # print(i,state_process)
        if state_process in self.final_state:
            return "String Accepted"
        else:
            return "String Not Accepted"


# a = FAStringTesting(
#     'bbababa',
#     ['q0','q1','q2','q3'],
#     ['a','b'],
#     ['q0'],
#     ['q2'],
#     {
#         'q0':{
#             'a':['q1'],
#             'b':['q0']
#         },
#         'q1': {
#             'a': ['q2'],
#             'b': ['q0']
#         },
#         'q2': {
#             'a': ['q2'],
#             'b': ['q3']
#         },
#         'q3': {
#             'a': ['q3'],
#             'b': ['q3']
#         }
#     }
# )
# print(a.stringTesting())