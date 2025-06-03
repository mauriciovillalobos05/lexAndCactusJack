COMMAND ANALYZER FOR ROBOT
==========================

DESCRIPTION OF THE PROBLEM
--------------------------
This project implements a lexical and syntactic analyzer capable of understanding 
natural language commands directed to a robot. The system processes structured 
instructions like:

- "Robot please move 2 blocks ahead"
- "Robot please move 3 blocks ahead and then turn 90 degrees, then move 2 blocks"

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
- VERBS:
  - INS_ROTATE_VERB: "rotate", "turn"
  - INS_MOVE_VERB: "move"
- UNITS:
  - ARG_DEGREES_UNIT: "degrees", "deg"
  - ARG_BLOCKS_UNIT: "blocks", "block"
- INSTRUCTION CONJUNCTIONS: ", and then", ", then"
- NUMERIC LITERALS:
  - INT_L: Integer values
  - REAL_L: Decimal values
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
The included `visualizer.py` simulates robot execution on a 10x10 grid:
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
1. Compile:
   flex lexer.l
   bison -d parser.y
   gcc lex.yy.c parser.tab.c -o robot_parser

2. Run parser:
   ./robot_parser

3. Optional: Run visualizer
   ./robot_parser | python3 visualizer.py

------------------------------------------------------------

FILES INCLUDED
--------------
- lexer.l         → Flex lexer definition
- parser.y        → Bison parser definition
- visualizer.py   → Python robot grid simulator
- parser.tab.c/h  → Bison-generated files
- lex.yy.c        → Flex-generated file
- README.md       → This documentation

------------------------------------------------------------

FUTURE WORK
-----------
- Add support for new commands: "go back", "repeat", "pause"
- Add GUI for robot visualization
- Add error recovery in grammar

------------------------------------------------------------
