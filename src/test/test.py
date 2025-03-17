def match_keys(expected, result):
    """
        Matches the keys of two dictionary objects recursively.

        Returns:
            Bool: True on match, False on different dictionary structure
    """
    
    if isinstance(expected, dict) and isinstance(result, dict):
        return (set(expected.keys()) == set(result.keys())) and (all(match_keys(expected[key], result[key]) for key in expected))
    
    if isinstance(expected, list):
        if not expected:
            return True
        if not isinstance(result, list):
            return False    
        return (all(match_keys(expected[0], item) for item in result))

    if result is None:
        return True
    
    if isinstance(expected, (int, float)) and isinstance(result, (int, float)):
        return True
    
    return isinstance(result, type(expected))