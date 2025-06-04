%{
#include "parser.tab.h"
#include <stdlib.h>
#include <string.h>
%}

%%
"Robot"|"robot"                   { return NOUN; }
"please"|"kindly"|"would you please" { return POLITE_WORDS; }
", and then"|", then"            { return INS_CONJUNCTION; }

"rotate"|"turn"                         { return INS_ROTATE_VERB; }
"move"                           { return INS_MOVE_VERB; }

"deg"|"degrees"                  { return ARG_DEGREES_UNIT; }
"block"s?                        { return ARG_BLOCKS_UNIT; }

[0-9]+                           { yylval.ival = atoi(yytext); return INT_L; }
[0-9]+"."[0-9]*|[0-9]*"."[0-9]+  { yylval.rval = strtof(yytext, NULL); return REAL_L; }

[ \t\r]+                         ;
\n                               { yylineno++; }
\.                               { return '.'; }

\/\/[^\n]*                       ;  // comment
.                                { fprintf(stderr, "Unexpected character: %s\n", yytext); return '.'; }
%%

int yywrap() { return 1; }