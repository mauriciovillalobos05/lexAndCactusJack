import graphviz

def cpu_logic_dfa():
    dot = graphviz.Digraph("CPU_DFA")
    
    # States
    dot.node("S0", "Start / Idle")
    dot.node("S1", "Rotating")
    dot.node("S2", "Moving")
    dot.node("E", "Error / Out of Bounds")

    # Transitions
    dot.edge("S0", "S1", label="ROTATE(90|180|270)")
    dot.edge("S1", "S0", label="Complete Rotation")
    dot.edge("S0", "S2", label="MOVE(n) within bounds")
    dot.edge("S2", "S0", label="Complete Move")
    
    # Errors
    dot.edge("S0", "E", label="Invalid ROTATE angle")
    dot.edge("S0", "E", label="MOVE out of bounds")

    return dot

dfa = cpu_logic_dfa()
dfa.render("cpu_dfa", format="png", view=True)