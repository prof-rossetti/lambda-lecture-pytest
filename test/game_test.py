

# This is a test file!
# For Pytest to recognize this file as containing "tests",
# ... the file name must end with "_test.py" or start with "test_"
# ... (see: https://docs.pytest.org/en/latest/goodpractices.html#test-discovery).

from app.game import determine_winner

# This is test. It's just a normal function.
# For Pytest to recognize this function as a "test", the function name must begin with "test_".
# Ideally we invoke the logic we are testing (e.g. the determine_winner() function) from within the test
# ... and then make one or more "assertions" about what the expected result should be.
def test_determine_winner():
    #assert determine_winner("rock", "rock") == None
    assert determine_winner("rock", "paper") == "paper"
    #assert determine_winner("rock", "scissors") == "rock"
    #
    #assert determine_winner("paper", "rock") == "paper"
    #assert determine_winner("paper", "paper") == None
    #assert determine_winner("paper", "scissors") == "scissors"
    #
    #assert determine_winner("scissors", "rock") == "rock"
    #assert determine_winner("scissors", "paper") == "scissors"
    #assert determine_winner("scissors", "scissors") == None
