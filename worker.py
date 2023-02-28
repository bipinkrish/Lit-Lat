from fuzzywuzzy import fuzz
import json

with open("dictionary/kn.json", "r", encoding="utf-8") as f:
    words = json.load(f)

def get_closest_match(word, words_dict):
    best_match = None
    best_ratio = -1
    for key, value in words_dict.items():
        ratio = fuzz.ratio(word, key)
        if ratio > best_ratio:
            best_match = key
            best_ratio = ratio
        elif ratio == best_ratio and value > words_dict[best_match]:
            # if ratios are the same, choose the word with higher priority
            best_match = key
            best_ratio = ratio
    return best_match


# example usage
query = "ಬಗ"
closest_match = get_closest_match(query,words)
print(f"Closest match for '{query}' is '{closest_match}'")
