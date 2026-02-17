class FiniteAutomatonSearch:
    def __init__(self) -> None:
        pass

    def build_transition_table(self, pattern: str, 
                                         alphabet: set[str]) -> list[dict[str, int]]:
        m = len(pattern)

        pi = [0] * m

        for i in range(1, m):
            j = pi[i - 1]

            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j - 1]

            if pattern[i] == pattern[j]:
                j += 1

            pi[i] = j

        transition_table: list[dict[str, int]] = [{} for _ in range(m + 1)]

        for state in range(m + 1):
            for char in alphabet:
                if state < m and char == pattern[state]:
                    transition_table[state][char] = state + 1

                elif state == 0:
                    transition_table[state][char] = 0

                else:
                    transition_table[state][char] = transition_table[
                        pi[state - 1]][char]

        return transition_table

    def search(self, text: str, pattern: str) -> list[int]:
        if not pattern:
            return []

        alphabet = set(text) | set(pattern)
        transition_table = self.build_transition_table(pattern, alphabet)

        m = len(pattern)
        current_state = 0
        positions: list[int] = []

        for i, char in enumerate(text):
            current_state = transition_table[current_state].get(char, 0)

            if current_state == m:
                positions.append(i - m + 1)

        return positions


def main():
    text = "ABABABACABAABABACABAB"
    pattern = "ABABAC"

    fas = FiniteAutomatonSearch()
    positions = fas.search(text, pattern)

    if positions:
        print(f"Текст = {text}")
        print(f"Паттерн = {pattern}")
        print(f"Найдено вхождений: {len(positions)}, на позициях: {positions}")

    else:
        print("\nВхождений не найдено")


if __name__ == "__main__":
    main()
