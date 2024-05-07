def rabin_karp(text, pattern):
    prime = 101
    prime_power = pow(prime, len(pattern))

    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * prime + ord(pattern[i])) % prime_power
        text_hash = (text_hash * prime + ord(text[i])) % prime_power

    indices = []

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if text[i:i+len(pattern)] == pattern:
                indices.append(i)

        if i < len(text) - len(pattern):
            text_hash = (text_hash - ord(text[i]) * pow(prime, len(pattern) - 1)) % prime_power
            text_hash = (text_hash * prime + ord(text[i + len(pattern)])) % prime_power
            text_hash = (text_hash + prime_power) % prime_power

    return indices

def main():
    text = "AABAACAADAABAABA"
    pattern = "AABA"
    indices = rabin_karp(text, pattern)
    if indices:
        for index in indices:
            print(f"Pattern found at index: {index}")
    else:
        print("Pattern not found in the text.")

if __name__=='__main__':
    main()