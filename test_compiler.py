import compiler

class TestStatementOutput:
    def test_addition(self):
        assert compiler.compile("| 5 !ADD 7 >", {}) == [12, {}]

    def test_subtraction(self):
        assert compiler.compile("| 5 !SUB 7 >") == [-2]

    def test_multiplication(self):
        assert compiler.compile("| 2 !MUL 4 >") == [8]

    def test_nested_expression(self):
        assert compiler.compile("| | 2 !ADD | 3 !ADD 1 > > !SUB | 5 !ADD 7 > >") == [-6]

    def test_multiple_expressions(self):
        assert compiler.compile("| 3 !MUL | 5 !ADD 7 > > | 20 !ADD 10 >") == [36, 30]

    def test_assignment(self):
        assert compiler.compile("| ?x <- | 5 !ADD 7 > >") == [12]

    def test_multiple_assignment_expression(self):
        assert compiler.compile("| ?x <- | 5 !ADD 7 > > | 20 !ADD 10 >") == [12, 30]
