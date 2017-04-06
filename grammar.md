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


non terminals:

PROGRAM := STMT +

STMT := EXPR
        ASSIGNMENT

EXPR := | EXPR operator EXPR >
        INTEGER
        NAME

ASSIGNMENT :=
        NAME <- EXPR



