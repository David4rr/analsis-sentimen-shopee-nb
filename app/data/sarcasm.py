from __future__ import annotations

SARCASM_POS_TRIGGERS = {
    'bagus', 'hebat', 'mantap', 'keren', 'luar biasa', 'top',
    'sempurna', 'terbaik', 'sip', 'joss', 'nice', 'good', 'great',
    'amazing', 'perfect', 'wow', 'wah', 'suka', 'puas', 'rekomendasi',
}

SARCASM_NEG_TRIGGERS = {
    'rusak', 'hancur', 'palsu', 'jelek', 'buruk', 'zonk', 'bohong',
    'tipu', 'kecewa', 'sampah', 'busuk', 'parah', 'payah', 'ancur',
    'cacat', 'pecah', 'sobek', 'luntur', 'menyesal', 'kapok',
    'gagal', 'error', 'scam', 'fake', 'broken', 'terrible',
}

SARCASM_CONNECTORS = {
    'sampai', 'tapi', 'tetapi', 'cuma', 'sayangnya', 'eh', 'ternyata',
    'padahal', 'malah', 'justru', 'dong', 'ya', 'sih', 'kok',
}

def detect_sarcasm(text: str) -> dict:
    words = set(text.lower().split())
    
    found_pos = SARCASM_POS_TRIGGERS & words
    found_neg = SARCASM_NEG_TRIGGERS & words
    found_conn = SARCASM_CONNECTORS & words
    
    is_sarcasm = False
    reason = ""
    
    if found_pos and found_neg and found_conn:
        is_sarcasm = True
        reason = f"Pola sarkasme: {', '.join(found_pos)} + [{', '.join(found_conn)}] + {', '.join(found_neg)}"
    elif found_pos and found_neg:
        is_sarcasm = True
        reason = f"Kontradiksi: kata positif ({', '.join(found_pos)}) & negatif ({', '.join(found_neg)})"
        
    return {
        "is_sarcasm": is_sarcasm,
        "reason": reason
    }
