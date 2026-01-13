BANNED_WORDS = [
    "weapon", "explosive", "drugs", "violence",
    "sexual", "hate", "scam", "fraud"
]

def is_safe(text: str) -> bool:
    text = text.lower()
    return not any(word in text for word in BANNED_WORDS)
