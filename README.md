COMMAND ANALYZER FOR ROBOT
==========================

DESCRIPTION OF THE PROBLEM
--------------------------
This project implements a lexical and syntactic analyzer capable of understanding 
natural language commands directed to a robot. The system processes structured 
instructions like:

- "Robot please move 2 blocks ahead."
- "Robot please move 3 blocks ahead and then turn 90 degrees, then move 2 blocks."

And correctly rejects malformed instructions such as:

- "Robot moves 2 blocks"
- "Move 2 blocks right now"
- "Robot 2 blocks moves"

This is developed under the Project-Based Learning (PBL) approach, applying 
compiler construction techniques and natural language rules.

------------------------------------------------------------

LEXICAL ANALYZER
----------------
Implemented using Flex (lexer.l), the lexical analyzer identifies the following tokens:

- NOUN: "Robot", "robot"
- KIND WORDS: "please", "kindly", "would you please"
- CONJUNCTIONS: ", and then", ", then"
- VERBS:
  - INS_ROTATE_VERB: "rotate", "turn"
  - INS_MOVE_VERB: "move"
- UNITS:
  - ARG_DEGREES_UNIT: "degrees", "deg"
  - ARG_BLOCKS_UNIT: "blocks", "block"
- NUMERIC LITERALS:
  - INT_L: Integer values
- COMMENTS: Lines starting with `//` are ignored
- ERROR HANDLING: Unexpected characters are reported with line number

------------------------------------------------------------

SYNTAX ANALYZER
---------------
Implemented using Bison (parser.y), the CFG (Context-Free Grammar) defines valid 
instruction sequences for the robot.

GRAMMAR RULES:
--------------
program           -> statement_list
statement_list    -> statement | statement_list statement
statement         -> NOUN POLITE_WORDS instruction_list '.'
instruction_list  -> instruction | instruction_list INS_CONJUNCTION instruction
instruction       -> rotate_instruction | move_instruction
rotate_instruction-> INS_ROTATE_VERB value ARG_DEGREES_UNIT
move_instruction  -> INS_MOVE_VERB value ARG_BLOCKS_UNIT
value             -> INT_L | REAL_L

SEMANTIC CONSTRAINTS:
---------------------
- Valid rotation degrees: 90, 180, 270
- Movement must be between 1 and 10 blocks

------------------------------------------------------------

VISUALIZER
----------
The included `cpu.py` simulates robot execution on a 10x10 grid:
- Tracks position and direction (N, E, S, W)
- Visualizes movements and rotations
- Detects and blocks out-of-bound moves
- Receives parsed instructions as input

------------------------------------------------------------

VALID INPUT EXAMPLES
--------------------
✓ Robot please move 2 blocks.
✓ Robot kindly rotate 90 degrees.
✓ Robot would you please move 3 blocks, then turn 180 degrees, and then move 1 block.

NOTE You should have instructions with '.' at the end of each of them.

To change the instructions you want to try, change the file instructions.txt and run make run afterwards.

INVALID INPUT EXAMPLES
----------------------
✗ Robot moves 2 blocks            → missing polite form
✗ Move 2 blocks right now         → missing subject
✗ Robot 2 blocks moves            → invalid word order
✗ Robot please rotate 45 degrees → invalid rotation value
✗ Robot please move 15 blocks    → out-of-range block count

------------------------------------------------------------

USAGE INSTRUCTIONS
------------------
1. Install packages: pip install -r requirements.txt

The following commands should be executed inside parser folder

1. Compile:
   make

2. Run parser:
   make run

3. Optional: remove generated files
   make clean

------------------------------------------------------------

FILES INCLUDED
--------------
- lexer.l         → Flex lexer definition
- parser.y        → Bison parser definition
- cpu.py          → Python robot grid simulator
- graphviz.py     → Python machine state diagram
- README.md       → This documentation

------------------------------------------------------------

FUTURE WORK
-----------
- Add support for new commands: "go back", "repeat", "pause"
- Add GUI for robot visualization
- Add error recovery in grammar

------------------------------------------------------------
