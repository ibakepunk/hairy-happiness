__author__ = 'ibakepunk'


def get_diff(expected, actual, key=None):
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
        diff += 'Expected keys at {key} not found: {keys}'.format(key=key, keys=str(d1_not_d2) + '\n') if d1_not_d2 \
            else ''
        diff += 'Not expected keys at {key} found: {keys}'.format(key=key, keys=str(d2_not_d1) + '\n') if d2_not_d1 \
            else ''
        for k in expected:
            if k in actual:
                diff += get_diff(expected[k], actual[k], key + '/' + k)
    elif isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            diff += '{key} expected length {exp_len}, got {act_len}\n'.format(key=key, exp_len=len(expected),
                                                                              act_len=len(actual))
            return diff
        for i, (v1, v2) in enumerate(zip(expected, actual)):
            diff += get_diff(v1, v2, key + '[' + str(i) + ']')
    else:
        if expected != actual:
            diff += '{key} must be {exp}, got {act}\n'.format(key=key, exp=str(expected), act=str(actual))
    return diff