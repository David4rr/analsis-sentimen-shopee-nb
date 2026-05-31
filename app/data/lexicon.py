# Lexicon Dictionaries from Reference Project

POSITIVE_LEXICON = {
    # === Core positive sentiment ===
    "bagus": 4, "baik": 4, "senang": 4, "suka": 4, "puas": 5,
    "mantap": 5, "keren": 5, "hebat": 5, "sempurna": 5,
    "istimewa": 5, "unggul": 5, "fantastis": 5, "luar biasa": 5,
    "menakjubkan": 5, "memukau": 5, "terbaik": 5, "prima": 5,
    "memuaskan": 5, "menyenangkan": 4, "mengagumkan": 5,
    "oke": 1, "sesuai": 1, "cocok": 3, "pas": 1,
    "tepat": 1, "benar": 1, "betul": 1, "setuju": 2,
    "mendukung": 3, "apresiasi": 4, "rekomendasi": 4,
    "terima kasih": 3, "terimakasih": 3,
    # === Quality ===
    "berkualitas": 5, "original": 4, "asli": 4, "mewah": 4,
    "elegan": 4, "premium": 5, "tahan": 3, "awet": 4,
    "kuat": 3, "solid": 4, "kokoh": 4, "rapi": 3, "bersih": 3,
    "halus": 3, "lembut": 3, "tebal": 3, "detail": 3,
    "presisi": 4, "akurat": 4, "tajam": 3, "jernih": 3,
    "cemerlang": 4, "bermutu": 5, "unggul": 5,
    "tahan lama": 4, "anti luntur": 4, "anti air": 3,
    "terjamin": 4, "bersertifikat": 4,
    # === E-commerce / Delivery ===
    "cepat": 3, "kilat": 4, "ekspres": 4, "instan": 3,
    "murah": 4, "terjangkau": 4, "hemat": 3, "diskon": 3,
    "gratis": 4, "bonus": 3, "hadiah": 3, "spesial": 4,
    "worth": 4, "worthit": 4, "sebanding": 4,
    "ramah": 4, "sopan": 3, "profesional": 4, "responsif": 4,
    "tanggap": 4, "sigap": 4, "informatif": 3,
    "aman": 3, "nyaman": 4, "praktis": 3, "efisien": 4,
    "lengkap": 3, "komplit": 3,
    "utuh": 4, "terlindungi": 4, "terbungkus": 3, "selamat": 3,
    "tepat waktu": 4, "on time": 4,
    "diterima": 3, "tiba": 2,
    # === Emotional ===
    "bahagia": 5, "gembira": 4, "ceria": 4, "antusias": 4,
    "semangat": 4, "optimis": 4, "percaya": 3, "yakin": 3,
    "bangga": 4, "kagum": 4, "takjub": 5, "terkesan": 4,
    "terharu": 4, "sabar": 3, "tenang": 3,
    "syukur": 3, "beruntung": 4, "senang hati": 4,
    "bersyukur": 4, "terpukau": 5, "terpesona": 5,
    "girang": 4, "riang": 4, "sukacita": 5,
    # === Tech / Modern ===
    "canggih": 4, "modern": 3, "trendy": 3, "stylish": 4,
    "inovatif": 4, "kreatif": 4, "cerdas": 4, "pintar": 4,
    "otomatis": 3, "lancar": 3, "mudah": 3, "simpel": 3,
    "ringan": 3, "stabil": 3, "konsisten": 3, "kompatibel": 3,
    "ergonomis": 4, "intuitif": 3, "responsif": 4,
    # === Trust ===
    "terpercaya": 4, "handal": 4, "andal": 4, "jujur": 3,
    "tulus": 4, "loyal": 4, "setia": 4,
    "dipercaya": 4, "diandalkan": 4,
    # === Success ===
    "sukses": 4, "berhasil": 4, "tercapai": 4, "terwujud": 4,
    "tuntas": 3, "selesai": 2,
    # === Appearance ===
    "cantik": 4, "indah": 4, "menarik": 4, "tampan": 3,
    "imut": 3, "lucu": 3, "unik": 3, "menawan": 4,
    "memesona": 5, "anggun": 4, "gagah": 3, "ganteng": 3,
    "estetis": 4, "estetik": 4, "fotogenik": 3,
    # === Food / Taste ===
    "enak": 4, "lezat": 5, "nikmat": 5, "segar": 3,
    "gurih": 4, "manis": 3, "wangi": 4, "harum": 4,
    "sedap": 4, "lembut": 3, "renyah": 4,
    # === English (common in Shopee reviews) ===
    "love": 4, "like": 3, "good": 3, "great": 4,
    "nice": 3, "best": 5, "excellent": 5, "amazing": 5,
    "awesome": 5, "perfect": 5, "wonderful": 5,
    "happy": 4, "thank": 3, "thanks": 3,
    "fast": 3, "quick": 3, "smooth": 3,
    "beautiful": 4, "pretty": 3, "cool": 3, "super": 4,
    "fantastic": 5, "brilliant": 5, "outstanding": 5,
    "satisfied": 4, "impressed": 4, "recommend": 4,
    "trusted": 4, "reliable": 4, "genuine": 4,
    "worth it": 4, "value": 3, "affordable": 4,
    "comfortable": 4, "durable": 4, "original": 4,
    "elegant": 4, "premium": 5, "quality": 4,
    # === Slang Positive ===
    "sip": 3, "joss": 5, "jos": 4, "mantul": 5,
    "baguslah": 4, "kece": 4, "gokil": 4, "top": 4,
    "juara": 5, "nais": 3, "pol": 4,
    "favorit": 4, "pilihan": 3, "bintang": 4, "jempol": 4,
    "terkesima": 5, "mempesona": 5, "ciamik": 5, "kece badai": 5,
    "gg": 4, "uwu": 3, "auto beli": 4, "auto repeat": 4,
    "the best": 5, "top markotop": 5, "mantap jiwa": 5,
    "sukak": 4, "sukaa": 4, "sukakk": 4,
    "waw": 4, "wow": 4, "woww": 4,
    # === Phrase-level positive ===
    "sesuai pesanan": 4, "sesuai gambar": 4, "sesuai deskripsi": 4,
    "sesuai foto": 4, "sesuai ekspektasi": 5,
    "foto asli": 3, "cepat sampai": 4, "pengiriman cepat": 4,
    "penjual ramah": 4, "seller ramah": 4,
    "respon cepat": 4, "tanggapan cepat": 4, "fast respon": 4, "fast response": 4,
    "pengemasan rapi": 4, "packing rapi": 4, "packing aman": 4,
    "harga murah": 4, "harga terjangkau": 4, "harga bersahabat": 4,
    "free ongkir": 4, "gratis ongkir": 4,
    "kualitas bagus": 5, "kualitas baik": 5, "kualitas mantap": 5,
    "kualitas premium": 5, "kualitas oke": 4,
    "tidak mengecewakan": 4, "tidak kecewa": 4,
    "sangat puas": 5, "sangat bagus": 5,
    "sangat suka": 5, "sangat senang": 5, "sangat rekomendasi": 5,
    "beli lagi": 4, "order lagi": 4, "pesan lagi": 4,
    "repeat order": 4, "langganan": 4,
    "harga sesuai": 4, "harga sepadan": 4,
    "barang bagus": 5, "barang sesuai": 4, "barang ori": 5,
    "produk bagus": 5, "produk berkualitas": 5,
    "layak beli": 4, "wajib beli": 5,
    "tidak menyesal": 4, "tidak rugi": 4,
    "sangat membantu": 4, "sangat berguna": 4,
    "sudah terbukti": 4, "terbukti bagus": 5,
    "terima kasih seller": 4,
    "pengiriman aman": 4, "barang utuh": 4,
}

NEGATIVE_LEXICON = {
    # === Core negative sentiment ===
    "buruk": -4, "jelek": -4, "kecewa": -5, "benci": -5,
    "marah": -4, "kesal": -4, "bosan": -3, "sedih": -4,
    "takut": -3, "khawatir": -3, "cemas": -3, "gelisah": -3,
    "payah": -4, "parah": -5, "mengerikan": -4, "menyedihkan": -4,
    "menyebalkan": -4, "mengesalkan": -4, "menjengkelkan": -4,
    "memalukan": -4, "mengecewakan": -5, "merugikan": -5,
    "membosankan": -3, "menakutkan": -3, "menyakitkan": -4,
    "menderita": -4, "gagal": -4, "sia-sia": -4,
    "menyesal": -4, "kapok": -4, "jijik": -5,
    "muak": -4, "bete": -3, "sebel": -4, "dongkol": -4,
    "frustrasi": -4, "depresi": -5, "stress": -4, "stres": -4,
    "trauma": -5,
    # === Quality issues ===
    "rusak": -4, "hancur": -5, "cacat": -4, "palsu": -5,
    "imitasi": -4, "tiruan": -4, "murahan": -3, "ringkih": -3,
    "rapuh": -3, "tipis": -2, "luntur": -4, "pudar": -3,
    "pecah": -4, "patah": -4, "penyok": -3, "lecet": -3,
    "sobek": -3, "retak": -3, "kusut": -3,
    "kotor": -3, "jorok": -4, "bau": -3, "basi": -4,
    "expired": -4, "kadaluarsa": -4, "bekas": -3,
    "rongsok": -5, "rongsokan": -5, "bobrok": -5,
    "usang": -3, "lapuk": -3, "karatan": -4,
    "bengkok": -3, "miring": -2, "gepeng": -3,
    "mengelupas": -3, "terkelupas": -3, "rontok": -3,
    "berkarat": -4, "jamur": -3, "berjamur": -4,
    "melting": -3, "meleleh": -3, "berkeringat": -2,
    # === Phrase-level quality ===
    "gampang rusak": -4, "mudah rusak": -4, "cepat rusak": -4,
    "mudah patah": -4, "mudah pecah": -4, "mudah sobek": -4,
    "cepat luntur": -4, "cepat pudar": -4,
    # === E-commerce / Shopping ===
    "lambat": -3, "lama": -3, "lemot": -4,
    "mahal": -3, "kemahalan": -4, "boros": -3, "pemborosan": -4,
    "tipu": -5, "bohong": -5, "curang": -5, "penipuan": -5,
    "scam": -5, "fraud": -5, "hoax": -5,
    "sampah": -5, "busuk": -5, "zonk": -4,
    "aneh": -2, "janggal": -3, "mencurigakan": -4,
    "menipu": -5, "pembohong": -5, "penipu": -5,
    "merampok": -5, "memeras": -5, "manipulasi": -5,
    "rugikan": -5, "dirugikan": -5, "kerugian": -5,
    # === Delivery issues ===
    "telat": -3, "terlambat": -3, "hilang": -4,
    "nyasar": -3, "tertukar": -3, "tercampur": -3,
    # === Service issues ===
    "jutek": -4, "cuek": -3, "sombong": -4, "kasar": -4,
    "galak": -4, "angkuh": -4, "arogan": -4,
    "mengabaikan": -4, "diabaikan": -4, "dicuekin": -4,
    # === Product mismatch ===
    "beda": -3, "berbeda": -3, "meleset": -3,
    # === Tech issues ===
    "error": -4, "bug": -4, "crash": -5, "hang": -4,
    "lag": -3, "ngehang": -4, "ngadat": -4,
    "trouble": -4, "loading": -2, "stuck": -3,
    "force close": -5, "restart": -3,
    # === Packaging issues ===
    "remuk": -4, "bocor": -4,
    # === Difficulty ===
    "sulit": -3, "susah": -3, "rumit": -3, "ribet": -3,
    "membingungkan": -3, "kompleks": -2, "repot": -3,
    # === Standalone negative markers ===
    "kurang": -2, "tanpa": -2, "anti": -2,
    # === Complaints ===
    "komplain": -3, "protes": -3, "keluhan": -3, "aduan": -3,
    "laporan": -2, "tuntutan": -3,
    # === Waste ===
    "mubazir": -4, "percuma": -4, "sia-sia": -4,
    # === English (common) ===
    "bad": -3, "terrible": -5, "horrible": -5, "worst": -5,
    "poor": -4, "ugly": -4, "hate": -5, "disappointed": -5,
    "slow": -3, "broken": -4, "fake": -5,
    "awful": -5, "stupid": -4, "useless": -5, "waste": -4,
    "angry": -4, "annoyed": -4, "frustrated": -4,
    "defective": -4, "damaged": -4, "wrong": -3,
    "overpriced": -3, "trash": -5, "garbage": -5,
    "sucks": -5, "suck": -5, "crap": -5,
    "pathetic": -5, "disgusting": -5, "regret": -4,
    "refund": -3, "return": -2,
    "cheap quality": -4, "low quality": -4, "rip off": -5,
    # === Slang Negative ===
    "abal": -4, "receh": -3, "gaje": -2,
    "lemah": -3, "dodol": -3, "ampas": -5,
    "bego": -4, "tolol": -5, "bodoh": -4,
    "kampungan": -3, "norak": -3, "ngeselin": -4,
    "nyebelin": -4, "anjir": -3, "bangsat": -5,
    "tai": -5, "sampahh": -5,
    # === Contextual / Nuance ===
    "masalah": -3, "kendala": -3, "gangguan": -3, "hambatan": -3,
    "kekurangan": -3, "kelemahan": -3, "cacat": -4,
    "kelambatan": -3, "keterlambatan": -3,
    "kerusakan": -4, "kebocoran": -4,
    "ketidaksesuaian": -4, "ketidakpuasan": -5,
    # === Phrase-level negative ===
    "tidak sesuai": -4, "tidak sesuai gambar": -4, "tidak sesuai deskripsi": -4,
    "tidak sesuai foto": -4, "tidak sesuai ekspektasi": -4,
    "beda gambar": -4, "beda deskripsi": -4,
    "beda warna": -3, "beda ukuran": -3,
    "salah warna": -3, "salah ukuran": -3, "salah kirim": -4,
    "tidak ramah": -4, "tidak responsif": -4, "tidak profesional": -4,
    "lambat respon": -3, "lama sampai": -3,
    "tidak sampai": -5, "belum sampai": -3,
    "tidak aman": -3, "tanpa bubble wrap": -3,
    "tidak puas": -5, "sangat kecewa": -5,
    "tidak rekomendasi": -4, "tidak recommend": -4,
    "buang waktu": -4, "buang uang": -4,
    "kapok beli": -5, "menyesal beli": -5,
    "barang jelek": -5, "barang rusak": -5, "barang palsu": -5,
    "produk jelek": -5, "produk buruk": -5,
    "kualitas buruk": -5, "kualitas jelek": -5,
    "kualitas rendah": -4, "kualitas kurang": -3,
    "tidak layak": -4, "kurang layak": -3,
    "tidak berguna": -4, "tidak berfungsi": -5,
}

INTENSIFIER_WORDS = {
    "sangat": 1.5, "amat": 1.5, "sekali": 1.5,
    "banget": 1.5, "terlalu": 1.3, "paling": 1.5,
    "super": 1.5, "luar biasa": 1.8,
    "benar-benar": 1.5, "sungguh": 1.5, "betul-betul": 1.5,
    "bener-bener": 1.5,
    "pol": 1.5, "abis": 1.3, "habis": 1.3,
    "extremely": 1.8, "very": 1.5, "really": 1.5,
    "so": 1.3, "totally": 1.5, "absolutely": 1.8,
    "completely": 1.5, "truly": 1.5, "highly": 1.5,
}

DIMINISHER_WORDS = {
    "agak": 0.5, "sedikit": 0.5,
    "cukup": 0.7, "lumayan": 0.7, "hampir": 0.7,
    "mungkin": 0.5, "sepertinya": 0.5, "kayaknya": 0.5,
    "rada": 0.5, "setengah": 0.5,
    "slightly": 0.5, "somewhat": 0.5, "fairly": 0.7,
    "quite": 0.7, "rather": 0.7,
    "a bit": 0.5, "a little": 0.5,
}

NEGATION_WORDS = {
    "tidak", "bukan", "belum", "jangan", "tanpa", "tak",
    "tiada", "enggan", "non", "anti",
    "never", "not", "no", "dont", "isnt", "wasnt",
    "neither", "none", "cannot",
}

NEUTRAL_THRESHOLD = 1.0

def calculate_polarity_score(text: str) -> float:
    """Calculate polarity score using enhanced lexicon analysis."""
    if not isinstance(text, str) or len(text.strip()) == 0:
        return 0.0

    words = text.lower().split()
    n = len(words)
    total_score = 0.0
    i = 0
    negation_active = False
    negation_countdown = 0
    modifier = 1.0

    while i < n:
        word = words[i]

        if word in NEGATION_WORDS:
            negation_active = True
            negation_countdown = 3
            i += 1
            continue

        if word in INTENSIFIER_WORDS:
            modifier = INTENSIFIER_WORDS[word]
            i += 1
            continue

        if word in DIMINISHER_WORDS:
            modifier = DIMINISHER_WORDS[word]
            i += 1
            continue

        score = 0.0
        matched_len = 1

        # Try trigram
        if i + 2 < n:
            trigram = f"{words[i]} {words[i+1]} {words[i+2]}"
            if trigram in POSITIVE_LEXICON:
                score = POSITIVE_LEXICON[trigram]
                matched_len = 3
            elif trigram in NEGATIVE_LEXICON:
                score = NEGATIVE_LEXICON[trigram]
                matched_len = 3

        # Try bigram
        if score == 0 and i + 1 < n:
            bigram = f"{words[i]} {words[i+1]}"
            if bigram in POSITIVE_LEXICON:
                score = POSITIVE_LEXICON[bigram]
                matched_len = 2
            elif bigram in NEGATIVE_LEXICON:
                score = NEGATIVE_LEXICON[bigram]
                matched_len = 2

        # Try unigram
        if score == 0:
            if word in POSITIVE_LEXICON:
                score = POSITIVE_LEXICON[word]
            elif word in NEGATIVE_LEXICON:
                score = NEGATIVE_LEXICON[word]

        if score != 0:
            score = score * modifier
            modifier = 1.0
            if negation_active:
                score = -score
                negation_active = False
                negation_countdown = 0
            total_score += score
        else:
            if negation_active:
                negation_countdown -= 1
                if negation_countdown <= 0:
                    negation_active = False
            modifier = 1.0

        i += matched_len

    return total_score

def classify_by_polarity(score: float) -> str:
    """Classify sentiment with threshold-based neutral zone."""
    if score > NEUTRAL_THRESHOLD:
        return "positif"
    elif score < -NEUTRAL_THRESHOLD:
        return "negatif"
    else:
        return "netral"
