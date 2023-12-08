from charivna_kulka import charivna_kulka
from charivna_kulka import answers
from charivna_kulka import probabilities


def test_charivna_kulka():
    result = charivna_kulka('Is this question random?')

    assert isinstance(result, str)

    assert result in answers

    new_result = charivna_kulka('')
    assert new_result == 'Invalid input'

def test_probabilities():
    count_of_tests = 1000
    success_count = 0
    for x in range(count_of_tests):
        result = charivna_kulka('Is this question random?')
        if result == answers[0]:
            success_count += 1
        
    observed_probability = success_count / count_of_tests
    expected_probability = probabilities[0]
    tolerance = 0.05
    print(f'observed: {observed_probability}, expected: {expected_probability}')
    assert abs(observed_probability - expected_probability) <= tolerance