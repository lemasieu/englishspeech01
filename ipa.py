import json
import nltk
import epitran
from nltk.corpus import cmudict

# Tải CMUdict nếu chưa có
nltk.download('cmudict')
cmu = cmudict.dict()

# Chuyển đổi ARPAbet sang IPA
arpabet_to_ipa = {
    "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
    "B": "b", "CH": "ʧ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɝ", "EY": "eɪ",
    "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i", "JH": "ʤ", "K": "k",
    "L": "l", "M": "m", "N": "n", "NG": "ŋ", "OW": "oʊ", "OY": "ɔɪ", "P": "p",
    "R": "ɹ", "S": "s", "SH": "ʃ", "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u",
    "V": "v", "W": "w", "Y": "j", "Z": "z", "ZH": "ʒ"
}

def convert_to_ipa(word, pronunciation):
    return "".join(arpabet_to_ipa.get(p.strip("012"), p) for p in pronunciation)

# Tạo từ điển IPA
ipa_dict = {}
for word, pron_list in cmu.items():
    ipa_dict[word.lower()] = { 
        "us": convert_to_ipa(word, pron_list[0]), 
        "uk": convert_to_ipa(word, pron_list[0]) 
    }

# Xuất ra JSON
with open("ipa_dictionary.json", "w", encoding="utf-8") as f:
    json.dump(ipa_dict, f, indent=4, ensure_ascii=False)

print("✅ File ipa_dictionary.json đã được tạo!")
