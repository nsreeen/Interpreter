terminals:

!ADD
!SUB
!MUL

->

integers [0-9]+
names ?[^ ]+
|
>



Rules:
- Expressions that can be surrounded by | and >


non terminals (should have own func in parser and most have own class):

PROGRAM := STMT +

STMT := EXPR
        ASSIGNMENT

EXPR := | EXPR operator EXPR >
        INTEGER
        NAME

ASSIGNMENT :=
        NAME <- EXPR
