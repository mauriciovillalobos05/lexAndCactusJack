import graphviz

def improved_cpu_dfa():
    dot = graphviz.Digraph("Improved_CPU_DFA")
    
    # Estados
    dot.node("IDLE", "Idle / Waiting")
    dot.node("ROTATE", "Rotating")
    dot.node("MOVE", "Moving")
    dot.node("DONE", "Instruction Completed")
    dot.node("ERROR", "Error")

    # Transiciones válidas
    dot.edge("IDLE", "ROTATE", label="Rotate: 90|180|270")
    dot.edge("ROTATE", "IDLE", label="Complete Rotation")

    dot.edge("IDLE", "MOVE", label="Move: n (in bounds)")
    dot.edge("MOVE", "IDLE", label="Complete Move")

    dot.edge("IDLE", "DONE", label="Instruction completed")

    # Manejo de errores
    dot.edge("IDLE", "ERROR", label="Rotate: invalid angle")
    dot.edge("IDLE", "ERROR", label="Move: out of bounds")
    dot.edge("MOVE", "ERROR", label="Move: out of bounds")
    dot.edge("IDLE", "ERROR", label="Unknown instruction")

    return dot

dfa = improved_cpu_dfa()
dfa.render("improved_cpu_dfa", format="png", view=True)
