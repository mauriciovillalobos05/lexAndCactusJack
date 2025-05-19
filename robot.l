%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[Pp]lease              { return POLITE; }
[Kk]indly              { return POLITE; }
[Cc]ould[ \t]+you      { return POLITE; }

[Tt]urn                { return TURN; }
[Mm]ove                { return MOVE; }

[1-9][0-9]*            { yylval.num = atoi(yytext); return NUMBER; }

[Bb]locks              { return BLOCKS; }
[Ff]orward             { return FORWARD; }

[Dd]egrees             { return DEGREES; }

[ \t\n]+               ;  // Ignore whitespace

.                      { printf("Invalid character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
