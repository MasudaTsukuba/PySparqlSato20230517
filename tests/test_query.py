from main import execute_query


def test_q1():
    result = execute_query('query/q1.json')
    assert len(result) == 815


def test_q2():
    result = execute_query('query/q2.json')
    assert len(result) == 2146


def test_q3a():
    result = execute_query('query/q3a.json')
    assert len(result) == 3732


def test_q3b():
    result = execute_query('query/q3b.json')
    assert len(result) == 3695


def test_q4():
    result = execute_query('query/q4.json')
    assert len(result) == 19526


def test_q5():
    result = execute_query('query/q5.json')
    assert len(result) == 43980


def test_q6():
    result = execute_query('query/q6.json')
    assert len(result) == 219


def test_q7():
    result = execute_query('query/q7.json')
    assert len(result) == 1


def test_q1pred():
    result = execute_query('query/q1pred.json')
    assert len(result) == 1
