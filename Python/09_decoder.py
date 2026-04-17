def decode(message):
    key = "YOURKEY"  #<-- Your key
    result = []
    key_idx = 0
    for ch in message:
        if ch == ' ':
            result.append(' ')
        else:
            shift = ord(key[key_idx % len(key)]) - ord('A') + 1
            decoded = ord(ch) - ord('A') + 1 - shift
            if decoded <= 0:
                decoded += 26
            result.append(chr(decoded + ord('A') - 1))
            key_idx += 1
    return ''.join(result)
