from fuzzywuzzy import fuzz
import json

def get_file_contents(filename):
    with open(filename, "r", encoding="utf-8") as f: return json.load(f)

def get_closest_matched_word(word, words_dict):
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

def get_closest_match_for_sentence(src_text, from_file):
    file_contents = get_file_contents(from_file)
    text = ""
    for word in src_text.split(): text += get_closest_matched_word(word, file_contents) + " "
    return text
