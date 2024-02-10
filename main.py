from collections import deque

class DFA:  
    
    def __init__(self, q, sigma, delta, initial_state, f):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.initial_state = initial_state
        self.f = f
        
        
    def accept(self, string):

        ans = False
        if string == "":
            ans = True
        else: 
            q = deque()    
            q.append([0,self.initial_state])
        
            while q and not ans:
                idx, state = q.popleft()
                
                if idx == len(string) and state in self.f:
                    ans = True
                
                elif idx < len(string):
                    if state in self.delta:
                        for transition in self.delta[state].items():
                            if string[idx] == transition[0]:
                                q.append([idx + 1, transition[1]])
                                        
        return ans    

q = {'q0', 'q1', 'q2'}
sigma = {'0', '1'}
delta = {'q0': {'0': 'q0', '1': 'q1'}, 'q1': {'0': 'q2', '1': 'q0'}, 'q2': {'0': 'q1', '1': 'q2'}}
i_state = 'q0'
f = {'q0'}

w = str(input("Enter a word of alphabet: "))
fa = DFA(q, sigma, delta, i_state, f).accept(w)


if __name__ == '__main__':
        
    if fa == True:
        print(f'The DFA accepts the string  "{w}"')
    else:
        print(f'The DFA rejects the string  "{w}"')
    
