import pytest
from interpreter import interpret

class TestStatementInterpretation:
    def test_dictionary_returned(self):
        assert interpret("| 5 !ADD 7 >", {})[1] == {}

    def test_addition(self):
        assert interpret("| 5 !ADD 7 >", {})[0].statements[0].value == 12

    def test_subtraction(self):
        assert interpret("| 5 !SUB 7 >", {})[0].statements[0].value == -2

    def test_multiplication(self):
        assert interpret("| 2 !MUL 4 >", {})[0].statements[0].value == 8

    def test_multiple_expressions(self):
        assert interpret("| 3 !MUL | 5 !ADD 7 > > | 20 !ADD 10 >", {})[0].statements[0].value == 36
        assert interpret("| 3 !MUL | 5 !ADD 7 > > | 20 !ADD 10 >", {})[0].statements[1].value == 30

    def test_assignment(self):
        assert interpret("| ?x <- | 5 !ADD 7 > >", {})[0].statements[0].value.value == 12

    def test_assignment(self):
        assert interpret("| ?x <- | 5 !ADD 7 > >", {})[0].statements[0].value.value == 12

    def test_assignment_and_dictionary(self):
        assert interpret("| ?x <- | 5 !ADD 7 > >", {})[1]["?x"] == 12

    def test_assignment_and_dictionary(self):
        assert interpret("| ?x <- | 5 !ADD 7 > >", {})[1]["?x"] == 12

    def test_multiple_assignment_expression(self):
        assert interpret("| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >", {})[0].statements[0].value.value == 12
        assert interpret("| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >", {})[0].statements[1].value == 30

    def test_assignment_and_use(self):
        assert interpret("| ?x <- | 5 > > | ?x !ADD 5 >", {})[0].statements[1].value == 10
