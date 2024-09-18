class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.steps = 0
    
    def step(self):
        tape_symbol = self.tape[self.head_position]
        key = (self.current_state, tape_symbol)
        if key in self.transition_function:
            next_state, symbol_to_write, head_move = self.transition_function[key]
            self.tape[self.head_position] = symbol_to_write
            self.head_position += 1 if head_move == 'R' else -1
            self.current_state = next_state
            self.steps += 1
            return True
        else:
            return False
    
    def run(self):
        while self.current_state not in self.final_states:
            if not self.step():
                break
        return self.tape, self.steps

transition_function = {
    ('q0', '0'): ('q1', '1', 'R'),
    ('q1', '0'): ('q2', '1', 'R'),
    ('q2', '0'): ('q3', '1', 'R'),
    ('q3', '0'): ('q4', '1', 'R'),
    ('q4', ' '): ('halt', ' ', 'R')
}

initial_tape = '0000     '

tm = TuringMachine(initial_tape, 'q0', {'halt'}, transition_function)

final_tape, steps = tm.run()

print('Final tape:', ''.join(final_tape))
print('Total steps:', steps)
