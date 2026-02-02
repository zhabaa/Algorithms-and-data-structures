def kmp_search(text: str, pattern: str) -> list[int]:
    if not pattern:
        return []
    
    def build_lps(pattern: str):
        m = len(pattern)
        lps = [0] * m

        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1

            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = build_lps(pattern)
    result: list[int] = []
    n, m = len(text), len(pattern)
    i = j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            
            if j == m:
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return result


def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    
    print("Текст:", text)
    print("Паттерн:", pattern)
    
    indices = kmp_search(text, pattern)
    
    if indices:
        print("Найдено на позициях:", indices)

    else:
        print("Не найдено")


if __name__ == "__main__":
    main()
