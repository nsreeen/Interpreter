TERMINALS:

!ADD
!SUB
!MUL
->
integers [0-9]+
names ?[^ ]+
|
>




RULES:

- Expressions must be surrounded by | and >




NON-TERMINALS:

PROGRAM := STATEMENT +

STATEMENT := EXPRESSION
             ASSIGNMENT

EXPRESSION := | EXPRESSION operator EXPRESSION >
     	      | INTEGER >
    	      | NAME >

ASSIGNMENT := | NAME <- EXPRESSION >
