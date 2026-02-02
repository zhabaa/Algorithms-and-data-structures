def boyer_moore_search(text: str, pattern: str) -> list[int]:
    def build_bad_char_table(pattern: str) -> dict[str, int]:
        table: dict[str, int] = {}
        m = len(pattern)

        for i in range(m - 1):
            table[pattern[i]] = m - 1 - i

        return table
    
    def build_good_suffix_table(pattern: str) -> list[int]:
        m = len(pattern)
        table = [m] * m
        last_prefix = m
        
        for i in range(m - 1, -1, -1):
            if is_prefix(pattern, i + 1):
                last_prefix = i + 1

            table[m - 1 - i] = last_prefix - i + m - 1
        
        for i in range(m - 1):
            slen = suffix_length(pattern, i)

            if pattern[i - slen] != pattern[m - 1 - slen]:
                table[slen] = m - 1 - i + slen
        
        return table
    
    def is_prefix(pattern: str, p: int):
        m = len(pattern)
        j = 0

        for i in range(p, m):
            if pattern[i] != pattern[j]:
                return False

            j += 1
    
        return True
    
    def suffix_length(pattern: str, p: int):
        m = len(pattern)
        length = 0
        i = p
        j = m - 1

        while i >= 0 and pattern[i] == pattern[j]:
            length += 1
            i -= 1
            j -= 1

        return length
    
    if not pattern:
        return []
    
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    bad_char = build_bad_char_table(pattern)
    good_suffix = build_good_suffix_table(pattern)
    
    result: list[int] = []
    i = m - 1
    
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        
        if j < 0:
            result.append(i + 1)
            i += m + 1 if m > 1 else 1

        else:
            char_shift = bad_char.get(text[i], m)
            suffix_shift = good_suffix[m - 1 - j]
            i += max(char_shift, suffix_shift)
    
    return result


def main():
    text = "ABAAABCDBBABCDDEBCABC"
    pattern = "ABC"
    
    print("Текст:", text)
    print("Паттерн:", pattern)
    
    indices = boyer_moore_search(text, pattern)
    
    if indices:
        print("Найдено на позициях:", indices)

    else:
        print("Не найдено")


if __name__ == "__main__":
    main()
