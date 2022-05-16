class DefineFAType:
    def __init__(self,state,symbol,start_state,final_state,transition):
        self.state = state
        self.symbol = symbol
        self.start_state = start_state
        self.final_state = final_state
        self.transition = transition
    def getAllTransition(self):
        all_transition = []
        for i in self.transition.values():
            for j in i.values():
                all_transition.append(j)
        return all_transition
    def define(self):
        all_transition = self.getAllTransition()
        for i in all_transition:
            if len(i) > 1:
                return "NFA"
        return "DFA"