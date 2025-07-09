import pytest

from app import Stack

@pytest.fixture
def stack():
    stack = Stack()
    yield stack

def test_empty_stack_size(stack):
    assert stack.size() == 0

def test_push(stack):
    stack.push(1)
    assert stack.size() == 1
    