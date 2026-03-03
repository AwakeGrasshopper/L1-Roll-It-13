def make_statement(statement, decoration):
    """adds emoji/ additional characters to the start and end of headings"""

    ends = decoration * 3
    print(f"{ends} {statement} {ends}")


# main routine
make_statement("I love python", "🐍")
make_statement("round results", "=")


