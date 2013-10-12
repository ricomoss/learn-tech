from copy import deepcopy


def add_dictionaries(content1, content2):
        new_content = deepcopy(content1)
        for val in content2.itervalues():
            if val not in new_content.itervalues():
                new_content[len(new_content) + 1] = val
        return new_content
