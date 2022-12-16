

def String_Search(string_in, char_to_find) :
    
    _index = string_in.index(char_to_find)
    _string_out = string_in[_index + 1 :]
    return _string_out.strip()