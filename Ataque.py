from collections import defaultdict
import math
import string




english_frequency = {
    "A": 0.08167, "B": 0.01492, "C": 0.02782, "D": 0.04253, "E": 0.12702,
    "F": 0.02228, "G": 0.02015, "H": 0.06094, "I": 0.06966, "J": 0.00153,
    "K": 0.00772, "L": 0.04025, "M": 0.02406, "N": 0.06749, "O": 0.07507,
    "P": 0.01929, "Q": 0.00095, "R": 0.05987, "S": 0.06327, "T": 0.09056,
    "U": 0.02758, "V": 0.00978, "W": 0.02360, "X": 0.00150, "Y": 0.01974,
    "Z": 0.00074,
}
portuguese_frequency = {
    "A": 0.1463, "B": 0.0104, "C": 0.0388, "D": 0.0499, "E": 0.1257,
    "F": 0.0102, "G": 0.0130, "H": 0.0078, "I": 0.0618, "J": 0.0039,
    "K": 0.0002, "L": 0.0278, "M": 0.0474, "N": 0.0505, "O": 0.1073,
    "P": 0.0252, "Q": 0.0120, "R": 0.0653, "S": 0.0781, "T": 0.0434,
    "U": 0.0463, "V": 0.0167, "W": 0.0001, "X": 0.0021, "Y": 0.0001,
    "Z": 0.0047
}


def decypher(encrypted_symbol, test_key):
    return (encrypted_symbol - test_key[0]) % 256

def factors_up_to(n: int, max_factor: int) -> list[int]:
    if n < 2 or max_factor < 2:
        return []
    
    factors = []
    # Only need to loop up to min(sqrt(n), max_factor)
    upper = min(int(n ** 0.5), max_factor)
    for i in range(2, upper + 1):
        if n % i == 0:
            factors.append(i)
            complement = n // i
            # Add the complementary factor if within limit and not duplicate
            if complement != i and complement <= max_factor:
                factors.append(complement)
    
    # If n itself is <= max_factor, include it
    if n <= max_factor:
        factors.append(n)
    
    return sorted(factors)

def letters_frequency(encrypted: bytearray, seq_len: int = 3, max_key_size: int = 20):
    positions: defaultdict[bytes, list[int]] = defaultdict(list)
    for i in range(len(encrypted) - seq_len - 1):
        combination = bytes(encrypted[i:i+seq_len])
        positions[combination].append(i)

    factors_frequency: dict[int, int] = {}
    for locs in positions.values():
        if len(locs) > 1:
            for j in range(len(locs)-1):
                spacing = locs[j+1] - locs[j]
                factors = factors_up_to(spacing, max_key_size)
                for factor in factors:
                    if factor not in factors_frequency:
                        factors_frequency[factor] = 1
                    else:
                        factors_frequency[factor] += 1

    return factors_frequency

def frequency(encrypted: bytearray, key_size: int, key_index: int, test_key: str):
    current_frequency: dict[int, int] = {}
    test_key = bytearray(test_key, "ascii")
    total = 0

    for i in range(key_index, len(encrypted), key_size):
        encrypted_symbol = encrypted[i]
        test_decrypted_symbol = decypher(encrypted_symbol, test_key)
        if test_decrypted_symbol not in current_frequency:
            current_frequency[test_decrypted_symbol] = 1
        else:
            current_frequency[test_decrypted_symbol] += 1

        total += 1

    result: dict[str, float] = {key: value / total for key, value in current_frequency.items()}
    return result

def chi_square_statistic(observed: dict[int, float], expected: dict[str, float]) -> float:
    chi2 = 0.0
    for category, E in expected.items():
        O = observed.get(ord(category.lower()), 0.0)
        if E > 0:
            chi2 += (O - E) ** 2 / E
            
    return chi2

def best_key_for_index(encrypted: bytearray, key_size: int, key_index: int, language: str = "en"):
    best_key = None
    best_score = math.inf

    if language == "en":
        freq = english_frequency
    else:
        freq = portuguese_frequency
    
    for test_key in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        score = chi_square_statistic(
            frequency(encrypted, key_size, key_index, test_key), freq
        )
        if score < best_score:
            best_key = test_key
            best_score = score

    return best_key

def attack_cypher(encrypted: bytearray, key_size: int, language: str = "en"):
    result = []
    if key_size:
        for i in range(key_size):
            result.append(best_key_for_index(encrypted, key_size, i, language))

    return "".join(result)

def best_size(encrypted: bytearray, candidates: list[int]) -> int:
    best_candidate = None
    best_score = math.inf

    for key_size in candidates:
        total_chi = 0.0
        for i in range(key_size):
            # find the best shift at this position
            min_chi = math.inf
            for test_key in string.ascii_letters:
                obs = frequency(encrypted, key_size, i, test_key)
                chi = chi_square_statistic(obs, english_frequency)
                if chi < min_chi:
                    min_chi = chi
            total_chi += min_chi

        avg_chi = total_chi / key_size
        if avg_chi < best_score:
            best_score = avg_chi
            best_candidate = key_size

    return best_candidate

def select_candidates(encrypted: bytearray, seq_len: int = 3, max_key_size: int = 20):
    text = encrypted
    freqs = letters_frequency(text, seq_len, max_key_size)
    items = sorted(freqs.items(), key=lambda kv: kv[1], reverse=True)
    if len(items) < 2:
        return [items[0][0]] if items else []

    # compute consecutive drops
    drops = [items[i][1] - items[i+1][1] for i in range(len(items)-1)]
    maximum_difference = drops.index(max(drops))

    return [size for size, _ in items[: maximum_difference+1]]

def attack(encrypted: bytearray, language="en"):
    candidates = select_candidates(encrypted)
    size = best_size(encrypted, candidates)
    return attack_cypher(encrypted, size, language=language)




from Ataque import *
if __name__ == "__main__":

    entrada = input("Qual arquivo deseja atacar? \n") 
    lingua = input("Em qual lingua está o arquivo?(pt/en) \n").lower()
    
    with open(entrada, "rb") as f:
        data = f.read()
        data = bytearray(data)
    
    key = attack(data, lingua)
    print(f"A chave encontrada é {key}")
    