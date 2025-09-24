import pytest
from stuff.accum import Accumulator

# If you use a yield statement instead of a return statement in a fixture
# the fixture function becomes something known in Python as a generato
@pytest.fixture
def accum():
  yield Accumulator()
  print("DONE-ZO!")

# By default, the scope is set to "function", meaning that the fixture will run once for each function that needs it. 
# However, if you change the scope to "session", then the fixture runs only one time for the entire test suite.
@pytest.fixture
def accum2(scope="session"):
    return Accumulator()