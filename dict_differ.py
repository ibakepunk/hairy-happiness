__author__ = 'ibakepunk'
__email__ = 'ibakepunk@gmail.com'

LIST_TYPES = (list, tuple)


def get_diff(expected, actual, key: str = '') -> str:
    """
    Recursively gets xpath of elements that differ.
    :param expected: Expected dict
    :param actual: Actual dict
    :type expected: dict
    :type actual: dict
    :return: Diff string
    :rtype: str
    """
    diff = ''
    key = key or '/'

    if isinstance(expected, dict) and isinstance(actual, dict):
        d1_not_d2 = [k for k in expected if k not in actual]
        d2_not_d1 = [k for k in actual if k not in expected]

        if d1_not_d2:
            diff += 'Expected keys at {key} not found: {keys}'.format(
                key=key, keys=str(d1_not_d2) + '\n')
        if d2_not_d1:
            diff += 'Not expected keys at {key} found: {keys}'.format(
                key=key, keys=str(d2_not_d1) + '\n')

        for k in expected:
            if k in actual:
                diff += get_diff(expected[k], actual[k], key + '/' + k)

    elif isinstance(expected, LIST_TYPES) and isinstance(actual, LIST_TYPES):
        if len(expected) != len(actual):
            diff += '{key} expected length {exp_len}, got {act_len}\n'.format(
                key=key, exp_len=len(expected), act_len=len(actual))
            return diff
        for i, (expected_value, actual_value) \
                in enumerate(zip(expected, actual)):
            diff += get_diff(expected_value, actual_value,
                             key + '[' + str(i) + ']')
    else:
        if expected != actual:
            diff += '{key} must be {exp}, got {act}\n'.format(
                key=key, exp=str(expected), act=str(actual))
    return diff
