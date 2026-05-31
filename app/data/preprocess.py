import re
import string

MORE_STOPWORDS = [
    "yg",
    "dg",
    "rt",
    "dgn",
    "ny",
    "d",
    "amp",
    "biar",
    "bikin",
    "bilang",
    "krn",
    "nya",
    "nih",
    "sih",
    "si",
    "tau",
    "tuh",
    "utk",
    "ya",
    "jd",
    "sdh",
    "aja",
    "n",
    "nyg",
    "hehe",
    "pen",
    "u",
    "nan",
    "loh",
    "dan",
    "atau",
    "di",
    "ke",
    "dari",
    "yang",
    "ini",
    "itu",
    "saya",
    "kamu",
    "dia",
    "mereka",
    "kita",
    "ada",
    "adalah",
    "kepada",
    "oleh",
    "pada",
    "min",
    "admin",
    "mimin",
    "kak",
    "kk",
    "gan",
    "sis",
    "bro",
    "bg",
    "mba",
    "mas",
    "cs",
    "dear",
    "dong",
    "lah",
    "deh",
    "yah",
    "bpk",
    "ibu",
]

NEGATION_WORDS = {
    "tidak",
    "tak",
    "bukan",
    "jangan",
    "kurang",
    "belum",
    "gak",
    "ga",
    "nggak",
    "enggak",
    "ngga",
    "kagak",
    "ndak",
    "gk",
    "tdk",
}

CONTRAST_WORDS = {
    "tapi",
    "namun",
    "cuman",
    "cuma",
    "sayang",
    "hanya",
    "meski",
    "walau",
    "padahal",
}

SLANG_MAP = {
    "bgt": "banget",
    "bngt": "banget",
    "bgtt": "banget",
    "gk": "gak",
    "ga": "gak",
    "ngga": "nggak",
    "ngak": "nggak",
    "kagak": "gak",
    "ndak": "tidak",
    "tdk": "tidak",
    "udh": "sudah",
    "sdh": "sudah",
    "dr": "dari",
    "krn": "karena",
    "karna": "karena",
    "yg": "yang",
    "utk": "untuk",
    "dgn": "dengan",
    "tp": "tapi",
    "tpi": "tapi",
    "pdhl": "padahal",
    "klo": "kalau",
    "kalo": "kalau",
    "skrg": "sekarang",
    "kmrn": "kemarin",
    "lg": "lagi",
    "msh": "masih",
    "td": "tadi",
    "bs": "bisa",
    "bsa": "bisa",
    "gmn": "gimana",
    "pd": "pada",
    "kpd": "kepada",
    "pake": "pakai",
    "pke": "pakai",
    "dpt": "dapat",
    "dapet": "dapat",
    "brg": "barang",
    "brng": "barang",
    "ongk": "ongkir",
    "ongkirnya": "ongkir",
    "apk": "aplikasi",
    "aplikasinya": "aplikasi",
    "app": "aplikasi",
    "eror": "error",
    "lemot": "lambat",
    "recomended": "recommended",
    "rekomen": "rekomendasi",
    "trimakasih": "terima kasih",
    "mksh": "makasih",
    "tks": "thanks",
    "ngotak": "masuk akal",
    "amanah": "jujur",
    "laa": "lah",
    "nyaa": "nya",
    "atw": "atau",
}


try:
    from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

    _base_sw = set(StopWordRemoverFactory().get_stop_words())
except (ModuleNotFoundError, ImportError):
    _base_sw = set(
        "yang untuk dengan dan atau ini itu di ke dari pada adalah "
        "saya kamu dia mereka kita ada".split()
    )

_final_stopwords = (_base_sw - NEGATION_WORDS - CONTRAST_WORDS).union(set(MORE_STOPWORDS))
_final_stopwords = _final_stopwords - NEGATION_WORDS - CONTRAST_WORDS
_negation_skip_words = _final_stopwords.union(
    {"sangat", "banget", "sekali", "amat", "agak", "cukup", "terlalu", "lebih", "paling"}
) - CONTRAST_WORDS


def _normalize_slang_token(token: str) -> str:
    return SLANG_MAP.get(token, token)


def _normalize_tokens(tokens: list[str]) -> list[str]:
    normalized = []
    for tok in tokens:
        normalized.extend(_normalize_slang_token(tok).split())
    return normalized


def _apply_negation_scope(tokens: list[str]) -> list[str]:
    result: list[str] = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok in NEGATION_WORDS:
            j = i + 1
            while j < len(tokens) and tokens[j] in _negation_skip_words:
                j += 1
            if j < len(tokens):
                result.append(f"tidak_{tokens[j]}")
                i = j + 1
                continue
        result.append(tok)
        i += 1
    return result


def preprocess_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+|https\S+|@[\w]+|#[\w]+", " ", text)
    text = re.sub(r"\d+", " ", text)
    punct = string.punctuation.replace("_", "")
    text = text.translate(str.maketrans(punct, " " * len(punct)))
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)
    text = re.sub(r"\s+", " ", text).strip()

    words = _normalize_tokens(text.split())
    words = _apply_negation_scope(words)
    words = [
        w for w in words if w not in _final_stopwords and w not in NEGATION_WORDS and len(w) > 1
    ]
    cleaned = " ".join(words).strip()
    return cleaned if cleaned else "kosong"
