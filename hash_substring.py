# python3

def read_input():
    mode = input()
    if mode == "I":
        return (input().rstrip(), input().rstrip())
    elif mode == "F":
        with open(input()) as file:
            return (file.readline().rstrip(), file.readline().rstrip())
    return ('','')
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    indices = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and text[i:i + pattern_len] == pattern:
            indices.append(i)
        if i < text_len - pattern_len:
            text_hash = hash(text[i + 1:i + pattern_len + 1])
    return indices


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

