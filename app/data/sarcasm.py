from __future__ import annotations
from data.lexicon import (
    POSITIVE_LEXICON, NEGATIVE_LEXICON, 
    calculate_polarity_score, classify_by_polarity
)

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

def detect_sarcasm(original_text: str, cleaned_text: str, nb_prediction: str) -> dict:
    original_lower = original_text.lower()
    cleaned_lower = cleaned_text.lower()
    
    words_orig = set(original_lower.split())
    words_cleaned = set(cleaned_lower.split())
    
    # We can check triggers against both
    words_all = words_orig | words_cleaned
    
    found_pos = SARCASM_POS_TRIGGERS & words_all
    found_neg = SARCASM_NEG_TRIGGERS & words_all
    found_conn = SARCASM_CONNECTORS & words_all
    
    is_sarcasm = False
    reason = ""
    
    # Signal 1 & 2: Rule-based explicit contradictions
    if found_pos and found_neg and found_conn:
        is_sarcasm = True
        reason = f"Pola sarkasme: {', '.join(found_pos)} + [{', '.join(found_conn)}] + {', '.join(found_neg)}"
    elif found_pos and found_neg:
        is_sarcasm = True
        reason = f"Kontradiksi: kata positif ({', '.join(found_pos)}) & negatif ({', '.join(found_neg)})"
        
    # Signal 3: Lexicon vs Naive Bayes disagreement
    if not is_sarcasm:
        lex_score = calculate_polarity_score(cleaned_lower)
        lex_sentiment = classify_by_polarity(lex_score)
        
        # We only override if Lexicon disagrees with NB prediction
        if lex_sentiment.lower() != nb_prediction.lower() and lex_sentiment != "netral":
            # Check for any pos/neg words from the huge Lexicon dictionaries in cleaned text
            has_any_pos = any(w in POSITIVE_LEXICON for w in words_cleaned)
            has_any_neg = any(w in NEGATIVE_LEXICON for w in words_cleaned)
            
            if has_any_pos and has_any_neg:
                is_sarcasm = True
                pos_words = [w for w in words_cleaned if w in POSITIVE_LEXICON]
                neg_words = [w for w in words_cleaned if w in NEGATIVE_LEXICON]
                reason = f"Model tidak sepakat (Lexicon={lex_sentiment.capitalize()}, NB={nb_prediction.capitalize()}) karena terdeteksi kata kontradiktif: positif ({', '.join(pos_words)}) & negatif ({', '.join(neg_words)})."
                
    return {
        "is_sarcasm": is_sarcasm,
        "reason": reason
    }
