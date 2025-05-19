%{
#include "y.tab.h"
%}

%%
[pP]lease              { return POLITE; }
[kK]indly              { return POLITE; }
[Cc]ould[ \t]+you      { return POLITE; }

[tT]urn                { return TURN; }
[mM]ove                { return MOVE; }

[1-9][0-9]*            { yylval.num = atoi(yytext); return NUMBER; }

90|180|270             { yylval.num = atoi(yytext); return DEGREE; }

[bB]locks              { return BLOCKS; }
[fF]orward             { return FORWARD; }

[dD]egrees             { return DEGREES; }

[ \t\n]+               ;  // Ignore whitespace

.                      { printf("Invalid character: %s\n", yytext); }
%%
