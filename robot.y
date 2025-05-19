%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);
%}

%union {
    int num;
}

%token POLITE TURN MOVE FORWARD BLOCKS
%token <num> NUMBER DEGREE
%type <num> command turn_cmd move_cmd

%%

command:
      POLITE turn_cmd    { printf("Valid turn command\n"); }
    | POLITE move_cmd    { printf("Valid move command\n"); }
    ;

turn_cmd:
    TURN DEGREE DEGREES   { printf("Turn: %d degrees\n", $2); }
    ;

move_cmd:
    MOVE NUMBER BLOCKS FORWARD { printf("Move: %d blocks forward\n", $2); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter a command:\n");
    yyparse();
    return 0;
}
