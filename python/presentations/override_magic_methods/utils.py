from copy import deepcopy


def add_dictionaries(content1, content2):
    new_content = deepcopy(content1)
    for val in content2.values():
        if val not in new_content.values():
            new_content[len(new_content) + 1] = val
    return new_content


def sub_dictionaries(content1, content2):
    new_content = deepcopy(content1)
    for key, val in content2.iteritems():
        if val in new_content.values():
            del new_content[key]
    return new_content


def format_phone(value):
    trans_map = {
        ord('-'): None,
        ord('('): None,
        ord(')'): None,
        ord(' '): None,
    }
    value = value.translate(trans_map)
    if len(value) > 3:
        value = value[:3] + '-' + value[3:]
        if len(value) > 7:
            value = value[:7] + '-' + value[7:]
    return value
