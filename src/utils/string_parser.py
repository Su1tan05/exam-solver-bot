import typing as t

# parse string to list of float 24.0;4;0.82;0.82;6.5
def parse_string_to_list(string: str) -> t.List[float]:
    return [float(item) for item in string.split(';')]