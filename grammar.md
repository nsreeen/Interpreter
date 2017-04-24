TERMINALS:

!ADD
!SUB
!MUL
->
integers [0-9]+
names ?[^ ]+
|
>



NON-TERMINALS:

PROGRAM := STATEMENT +

STATEMENT := EXPRESSION
             ASSIGNMENT

EXPRESSION := | EXPRESSION operator EXPRESSION >
     	      | INTEGER >
    	      | NAME >

ASSIGNMENT := | NAME <- EXPRESSION >




RULES:

- Expressions and assignments must be surrounded by | and >

