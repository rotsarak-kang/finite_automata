import numpy as np
import pandas as pd

class DesignFA:
    def __init__(self,state,symbol,start_state,final_state,transition):
        self.state = state
        self.symbol = symbol
        self.start_state = start_state
        self.final_state  = final_state
        self.transition = transition
    def defineEndState(self):
        endstate = self.final_state
        for i in endstate:
            if i in self.state:
                self.state[self.state.index(i)] = '*'+i
    def defineStartState(self):
        startstate = self.start_state
        for i in startstate:
            if i in self.state and i in self.final_state:
                self.state[self.state.index(i)] = "->*" + i
            elif i in self.state:
                self.state[self.state.index(i)] = "->"+i
    def convertFaToDataframe(self):
        self.defineStartState()
        self.defineEndState()
        data = []
        ind = 0
        for i in self.transition.values():
            data.append([])
            for j in i.values():
                for k in j:
                    data[ind].append(k)
            ind += 1
        df = pd.DataFrame(data,columns=self.symbol,index=self.state)
        return df