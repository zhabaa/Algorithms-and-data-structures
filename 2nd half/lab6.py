def rabin_karp_search(text: str, pattern: str, prime: int=101) -> list[int]:
    def hash_string(s: str, length: int) -> int:
        h = 0
        
        for i in range(length):
            h = (h * 256 + ord(s[i])) % prime
        
        return h
    
    def recalc_hash(old_hash: int, old_char: str, new_char: str, h_mult: int) -> int:
        new_hash = (old_hash - ord(old_char) * h_mult) % prime
        new_hash = (new_hash * 256 + ord(new_char)) % prime
        return new_hash
    
    if not pattern or len(pattern) > len(text):
        return []
    
    n, m = len(text), len(pattern)

    pattern_hash = hash_string(pattern, m)
    text_hash = hash_string(text, m)
    
    h_mult = 1

    for _ in range(m - 1):
        h_mult = (h_mult * 256) % prime
    
    result: list[int] = []
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                result.append(i)
        
        if i < n - m:
            text_hash = recalc_hash(text_hash, text[i], text[i+m], h_mult)

    return result


def main():
    text = "GEEK FOR GEEKS"
    pattern = "GEEK"
    
    print("Текст:", text)
    print("Паттерн:", pattern)
    
    indices = rabin_karp_search(text, pattern)
    
    if indices:
        print("Найдено на позициях:", indices)

    else:
        print("Не найдено")


if __name__ == "__main__":
    main()
