%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);

%}

%union {
    int ival;
    float rval;
}

%token NOUN POLITE_WORDS INS_CONJUNCTION
%token INS_ROTATE_VERB INS_MOVE_VERB
%token ARG_DEGREES_UNIT ARG_BLOCKS_UNIT
%token <ival> INT_L
%token <rval> REAL_L

%type <ival> statement_list statement instruction_list instruction rotate_instruction move_instruction value

%%

program:
    statement_list
    ;

statement_list:
      /* Empty */
    | statement_list statement
    ;

statement:
    NOUN POLITE_WORDS instruction_list '.'    { printf("Instruction completed.\n"); }
    ;

instruction_list:
      instruction
    | instruction_list INS_CONJUNCTION instruction
    ;

instruction:
      rotate_instruction
    | move_instruction
    ;

rotate_instruction:
    INS_ROTATE_VERB value ARG_DEGREES_UNIT
    {
        if ($2 == 90 || $2 == 180 || $2 == 270)
            printf("Rotate: %d degrees\n", $2);
        else
            yyerror("Only 90, 180, and 270 degrees are allowed.");
    }
    ;

move_instruction:
    INS_MOVE_VERB value ARG_BLOCKS_UNIT
    {
        if ($2 >= 1 && $2 <= 10)
            printf("Move: %d blocks forward\n", $2);
        else
            yyerror("Move must be between 1 and 10 blocks.");
    }
    ;

value:
    INT_L { $$ = $1; }
    | REAL_L { $$ = (int)$1; } // You can round or validate differently if needed
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Parse error: %s\n", s);
}

int main(void) {
    printf("Enter instructions (end each with '.'): \n");
    return yyparse();
}