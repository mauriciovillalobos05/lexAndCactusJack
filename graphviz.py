from graphviz import Digraph

def generate_dfa():
    dot = Digraph(comment='CPU Instruction DFA')
    dot.attr(rankdir='LR', size='8,5')

    # States
    dot.node('START', 'START')
    dot.node('POLITE', 'POLITE')
    dot.node('TURN', 'TURN')
    dot.node('MOVE', 'MOVE')
    dot.node('DEGREE', 'DEGREE')
    dot.node('NUMBER', 'NUMBER')
    dot.node('FORWARD', 'FORWARD')
    dot.node('EXECUTE', 'EXECUTE', shape='doublecircle')
    dot.node('ERROR', 'SYNTAX ERROR', shape='box', style='filled', color='red')

    # Transitions
    dot.edge('START', 'POLITE', label='polite word')
    dot.edge('POLITE', 'TURN', label='turn')
    dot.edge('POLITE', 'MOVE', label='move')

    dot.edge('TURN', 'DEGREE', label='90/180/270')
    dot.edge('DEGREE', 'EXECUTE', label='degrees')

    dot.edge('MOVE', 'NUMBER', label='number')
    dot.edge('NUMBER', 'FORWARD', label='blocks')
    dot.edge('FORWARD', 'EXECUTE', label='forward')

    # Error transitions
    dot.edge('START', 'ERROR', label='not polite', style='dashed')
    dot.edge('POLITE', 'ERROR', label='unknown verb', style='dashed')
    dot.edge('DEGREE', 'ERROR', label='not "degrees"', style='dashed')
    dot.edge('FORWARD', 'ERROR', label='not "forward"', style='dashed')

    # Render to file (can also output PDF, SVG, etc.)
    dot.render('cpu_instruction_dfa', format='png', cleanup=False)
    print("DFA diagram generated as 'cpu_instruction_dfa.png'.")

generate_dfa()
