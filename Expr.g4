grammar Expr;


// ==================== REGLAS SINTÁCTICAS  ====================

program: (instruction | NEWLINE)* EOF;

instruction: simple_stmt;


simple_stmt: small_stmt (';' small_stmt)* ';'? NEWLINE;

small_stmt: expr_stmt| import_stmt| pass_stmt| return_stmt| break_stmt| continue_stmt| global_stmt| nonlocal_stmt| assert_stmt;

expr_stmt: list_exp (augassign testlist | OP_ASSIGN testlist)?;

augassign: OP_PLUSEQ| OP_MINUSEQ| OP_STAREQ| OP_FLOORDIVEQ| OP_DIVEQ| OP_PERCENTEQ| OP_POWEQ| OP_RSHIFTEQ| OP_LSHIFTEQ| OP_BITANDEQ| OP_BITXOREQ| OP_BITOREQ| OP_WALRUS   ;

list_exp: (test | star_expr) (',' (test | star_expr))* ','?;

star_expr: '*' test;

test: or_test ('if' or_test 'else' test)? | lambda_expr;

or_test: and_test ('or' and_test)*;

and_test: not_test ('and' not_test)*;

not_test: 'not' not_test| comparison;

comparison: expr (operators expr)*;
operators: '<'| '>'| '=='| '>='| '<='| '!='| '<>'| 'in'| 'not' 'in'| 'is'| 'is' 'not';

expr: xor_expr ('|' xor_expr)*;

xor_expr: and_expr ('^' and_expr)*;

and_expr: shift_expr ('&' shift_expr)*;

shift_expr: arith_expr (('<<'|'>>') arith_expr)*;

arith_expr: term (('+'|'-') term)*;

term: factor (('*'|'/'|'%'|'//'|'@') factor)*;

factor: ('+'|'-'|'~') factor;

argument: test (comp_for)?| test '=' test| '**' test| '*' test;

comp_for: 'for' list_exp 'in' or_test (comp_iter)?;

comp_iter: comp_for| comp_if;

comp_if: 'if' or_test (comp_iter)?;

lambda_expr: 'lambda';

vfpdef: IDENTIFIER;

yield_expr: 'yield' (yield_arg)?;

yield_arg: 'from' test| testlist;

testlist: test (',' test)* ','?;

with_item: test ('as' expr)?;


// -------------------- Importaciones --------------------
import_stmt: 'import' dotted_as_names| 'from' dotted_name 'import' ('*' | import_as_names);

dotted_name: IDENTIFIER ('.' IDENTIFIER)*;

dotted_as_names: dotted_as_name (',' dotted_as_name)*;

dotted_as_name: dotted_name ('as' IDENTIFIER)?;

import_as_names: import_as_name (',' import_as_name)*;

import_as_name: IDENTIFIER ('as' IDENTIFIER)?;

pass_stmt: 'pass';

return_stmt: 'return' (testlist)?;

break_stmt: 'break';

global_stmt: 'global' IDENTIFIER (',' IDENTIFIER)*;

continue_stmt: 'continue';

nonlocal_stmt: 'nonlocal' IDENTIFIER (',' IDENTIFIER)*;

assert_stmt: 'assert' test (',' test)?;


// ==================== REGLAS LÉXICAS  ====================

// ---------- Palabras reservadas ----------
IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
WHILE   : 'while';
FOR     : 'for';
IN      : 'in';
DEF     : 'def';
CLASS   : 'class';
RETURN  : 'return';
BREAK   : 'break';
CONTINUE: 'continue';
IMPORT  : 'import';
FROM    : 'from';
AS      : 'as';
PASS    : 'pass';
TRY     : 'try';
EXCEPT  : 'except';
FINALLY : 'finally';
WITH    : 'with';
GLOBAL  : 'global';
NONLOCAL: 'nonlocal';
ASSERT  : 'assert';
DEL     : 'del';
RAISE   : 'raise';
YIELD   : 'yield';
LAMBDA  : 'lambda';
NONE    : 'None';
TRUE    : 'True';
FALSE   : 'False';
AND     : 'and';
OR      : 'or';
NOT     : 'not';
IS      : 'is';
ELIPSIS : '...';
ASYNC   : 'async';
AWAIT   : 'await';

// ---------- Operadores y delimitadores ----------
OP_MAS        : '+';
OP_MINUS       : '-';
OP_STAR        : '*';
OP_DIV         : '/';
OP_PERCENT     : '%';
OP_FLOORDIV    : '//';
OP_POW         : '**';
OP_LSHIFT      : '<<';
OP_RSHIFT      : '>>';
OP_BITAND      : '&';
OP_BITOR       : '|';
OP_BITXOR      : '^';
OP_TILDE       : '~';
OP_LT          : '<';
OP_GT          : '>';
OP_LE          : '<=';
OP_GE          : '>=';
OP_EQ          : '==';
OP_NE          : '!=';
OP_NE2         : '<>';
OP_ASSIGN      : '=';
OP_PLUSEQ      : '+=';
OP_MINUSEQ     : '-=';
OP_STAREQ      : '*=';
OP_DIVEQ       : '/=';
OP_PERCENTEQ   : '%=';
OP_FLOORDIVEQ  : '//=';
OP_POWEQ       : '**=';
OP_LSHIFTEQ    : '<<=';
OP_RSHIFTEQ    : '>>=';
OP_BITANDEQ    : '&=';
OP_BITOREQ     : '|=';
OP_BITXOREQ    : '^=';
OP_WALRUS      : ':=';         
OP_DOUBLE_DOT  : ':';
OP_DOT_COMMA   : ';';
OP_COMMA       : ',';
OP_DOT         : '.';
OP_LPAREN      : '(';
OP_RPAREN      : ')';
OP_LBRACK      : '[';
OP_RBRACK      : ']';
OP_LBRACE      : '{';
OP_RBRACE      : '}';
OP_ARROW       : '->';
OP_DECORATOR   : '@';         
IDENTIFIER: ([a-zA-Z] | '_') ([a-zA-Z] | [0-9] | '_')*;
NUMBER: INTEGER| FLOAT;
fragment INTEGER: DECIMAL_INTEGER| OCT_INTEGER| HEX_INTEGER| BIN_INTEGER;
fragment DECIMAL_INTEGER: [1-9] [0-9]* | '0'+;
fragment OCT_INTEGER: '0' [oO] OCT_DIGIT+;
fragment OCT_DIGIT: [0-7];
fragment HEX_INTEGER: '0' [xX] HEX_DIGIT+;
fragment HEX_DIGIT: [0-9a-fA-F];
fragment BIN_INTEGER: '0' [bB] BIN_DIGIT+;
fragment BIN_DIGIT: [01];
fragment FLOAT: POINT_FLOAT| EXPONENT_FLOAT;
fragment POINT_FLOAT: INT_PART? FRACTION| INT_PART '.' FRACTION;
fragment EXPONENT_FLOAT: (INT_PART | POINT_FLOAT) EXPONENT;
fragment INT_PART: [0-9]+;
fragment FRACTION: '.' [0-9]+;
fragment EXPONENT: [eE] [+-]? [0-9]+;
WS: [ \t\n\r]+ -> skip;
NEWLINE: ('\r'? '\n' | '\r') [ \t]*;

