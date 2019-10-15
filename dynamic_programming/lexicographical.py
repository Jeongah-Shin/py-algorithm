def split(word):
    return [ord(char) for char in word]

def dp_longest_inc_subseq(seq):
    L = [1] * len(seq)
    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1+ L[pre])
    print(seq)
    print(L)
    return max(L)

if __name__ == '__main__':
    # ann - 3개 요소 삭제
    input1 = 'banana'
    # abcd - 1개 요소 삭제
    input2 = 'abcda'
    # cccc - 4개 요소 삭제
    input3 = 'cbacdcbc'
    chars = split(input3)
    print(len(chars)-dp_longest_inc_subseq(chars))