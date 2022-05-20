from Services.DesignFA import DesignFA
class MinimizeDfa:
    def __init__(self,state,symbols,start_state,final_state,transition):
        self.state = state
        self.symbols = symbols
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
        self.new_state = []
        self.new_state_state = []
        self.new_final_state = []
        self.new_transition = []

    def generateDataFrame(self,fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition): #return to user as transition table
        fa = DesignFA(fa_state,fa_symbols,fa_start_state,fa_final_state,fa_transition)
        dfa = fa.convertFaToDataframe()
        return dfa


    def iter1(self,state): #Mark state with final
        final_state = self.final_state.copy()
        marked_state = []

        #get marked state
        for i in final_state:
            for j in state:
                tmp_state = []
                if i != j:
                    tmp_state.append(j)
                    tmp_state.append(i)
                    tmp_state.sort()
                    marked_state.append(tmp_state)

        unmarked_state = []
        #get unmark state
        for i in state[1:]:
            for j in state[:-1]:
                tmp_state = []
                if i!=j:
                    tmp_state.append(i)
                    tmp_state.append(j)
                    tmp_state.sort()
                    if tmp_state not in marked_state:
                        if tmp_state not in unmarked_state:
                            unmarked_state.append(tmp_state)
        unmarked_state.sort()

        return marked_state, unmarked_state

    def iter2(self,marked_f_state,unmarked_state): #Check equal to iter1 state
        unmarked_iter2_state = []

        #test state if match in marked_f_state
        for i in unmarked_state:
            total_tmp_state = []
            marked_check = False
            for j in self.symbols:
                tmp_state = []
                tmp_state.append(self.transition[i[0]][j][0])
                tmp_state.append(self.transition[i[1]][j][0])
                tmp_state.sort()
                total_tmp_state.append(tmp_state)
            for j in total_tmp_state:
                if j in marked_f_state:
                    marked_check = True
            if marked_check == True:
                marked_f_state.append(i)
            else:
                if i not in unmarked_iter2_state:
                    unmarked_iter2_state.append(i)

        return unmarked_iter2_state

    def step1(self): #Check transition from start state
        marked_state = []
        marked_state.append(self.start_state[0])
        transition = self.transition.copy()
        state = self.state.copy()

        #check directed transition from start state
        for i in self.symbols:
            if len(transition[self.start_state[0]][i]) > 0:
                marked_state.append(transition[self.start_state[0]][i][0])
        marked_state.sort()

        totest_state = marked_state[1:].copy()

        #remove marked state from total state
        for i in marked_state:
            state.remove(i)

        #check indirected transition state from start_state
        for i in state:
            for j in totest_state:
                check_break = False
                for k in self.symbols:
                    if transition[j][k][0] == i:
                        marked_state.append(i)
                        totest_state.append(i)
                        check_break = True
                        break
                if check_break == True:
                    break
        marked_state.sort()
        return marked_state

    def step2(self,state): #Mark the state
        #marked the state with final state
        marked_f_state,unmarked_state = self.iter1(state)
        unmarked_iter2_state = self.iter2(marked_f_state,unmarked_state)
        return unmarked_iter2_state

    def step3(self,state_to_step2,unmarked_iter2_state): #Merge equal state
        equal_state = []
        state = []
        for i in unmarked_iter2_state:
            for j in i:
                if j not in equal_state:
                    equal_state.append(j)
        equal_state.sort()
        mergestate = ''
        for i in equal_state:
            mergestate += i

        #generate else state of equal state
        for i in state_to_step2:
            if i not in equal_state:
                state.append(i)
        state.sort()
        unequal_state = state

        return unequal_state,equal_state,mergestate

    def step4(self,unequal_state,equal_state,mergestate): #generate final transition
        transition = {}

        #generate transition for unequal state
        for i in unequal_state:
            transition[i] = {}
            for j in self.symbols:
                tmp_state = []
                if self.transition[i][j][0] in equal_state:
                    transition[i][j] = [mergestate]
                else:
                    transition[i][j] = [self.transition[i][j][0]]

        #generate transition for merge state
        transition[mergestate] = {}
        for i in self.symbols:
            if self.transition[equal_state[0]][i][0] in equal_state:
                transition[mergestate][i] = [mergestate]
            else:
                transition[mergestate][i] = [self.transition[equal_state[0]][i][0]]

        unequal_state.append(mergestate)
        final_total_state = unequal_state.copy()

        #generate final end state
        final_end_state = []
        final_end_state.append(self.final_state[0])

        #generate final start state
        final_start_state = []
        if self.start_state[0] in final_total_state:
            final_start_state.append(self.start_state[0])
        else:
            final_start_state.append(mergestate)

        return transition,final_total_state,final_end_state,final_start_state

    def exce(self):
        state_to_step2 = self.step1()
        unmarked_iter2_state = self.step2(state_to_step2)
        unequal_state, equal_state,mergestate = self.step3(state_to_step2,unmarked_iter2_state)
        final_transition,final_total_state,final_end_state,final_start_state = self.step4(unequal_state,equal_state,mergestate)
        print(final_total_state)
        print(final_start_state)
        print(final_end_state)
        print(final_transition)
        dfa = self.generateDataFrame(final_total_state, self.symbols, final_start_state, final_end_state,final_transition)
        return dfa


# fa = MinimizeDfa(
#     ['q0','q1','q2','q3','q4'],
#     ['0','1'],
#     ['q0'],
#     ['q4'],
#     {
#         'q0':{
#             '0':['q1'],
#             '1':['q3']
#         },
#         'q1': {
#             '0': ['q2'],
#             '1': ['q4']
#         },
#         'q2': {
#             '0': ['q1'],
#             '1': ['q4']
#         },
#         'q3': {
#             '0': ['q2'],
#             '1': ['q4']
#         },
#         'q4': {
#             '0': ['q4'],
#             '1': ['q4']
#         }
#     }
# )
# print(fa.exce())