import math
import re

#list that can be guessed easily
COMMON_PASSWORDS = ["123456", "password", "123456789", "qwerty", "abc123", "letmein"]

def calculate_entropy(password):
    
    char_types = 0
    if any(c.islower() for c in password): char_types += 26  
    if any(c.isupper() for c in password): char_types += 26  
    if any(c.isdigit() for c in password): char_types += 10 
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password): char_types += 32  
    if char_types == 0: return 0
    return len(password) * math.log2(char_types)
 
def analyze_password(password):

    length = len(password)
    complexity = {
        "lowercase": bool(re.search(r'[a-z]', password)),
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "digits": bool(re.search(r'\d', password)),
        "specials": bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]', password)),
    }

    entropy = calculate_entropy(password)
    is_common = password.lower() in COMMON_PASSWORDS

    score = 0
    if length >= 12: score += 2
    elif length >= 8: score += 1

    score += sum(complexity.values())

    if entropy > 50: score += 2  
    elif entropy > 30: score += 1

    if is_common: score = 0  

    
    if score >= 7:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        "length": length,
        "complexity": complexity,
        "entropy": entropy,
        "is_common": is_common,
        "score": score,
        "strength": strength
    }

password =input("Enter your password: ")
analysis = analyze_password(password)
print("Password Analysis:", analysis)
