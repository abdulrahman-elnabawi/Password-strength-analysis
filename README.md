# Password Strength Analysis Tool

This project provides a Python-based tool to evaluate the strength of passwords. It checks passwords based on length, complexity, entropy, and whether the password is common. Additionally, it supports loading external password lists for more robust analysis.

---

## Features

1. **Length Check**: Ensures passwords meet a minimum length requirement.
2. **Complexity Analysis**: Evaluates the presence of uppercase letters, lowercase letters, digits, and special characters.
3. **Entropy Calculation**: Estimates password strength using mathematical entropy.
4. **Guessed List Check**: Compares passwords against a list of common or compromised passwords.
5. **Scoring System**: Provides a score and feedback on password strength (Weak, Medium, or Strong).
---

#### Example Usage:

{
  password = "p@S5w0rD!9#"
}


#### Example Output:

{
    "length": 11,
    "complexity": {
        "lowercase": true,
        "uppercase": true,
        "digits": true,
        "specials": true
    },
    "entropy": 71.27,
    "is_common": false,
    "score": 8,
    "strength": "Strong"
}



## Loading External Password Lists

**Download a password list** from a source (https://github.com/danielmiessler/SecLists) and add this code


 {

 
def load_common_passwords(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = file.read().splitlines()
        return passwords
    except FileNotFoundError:
        print("Error: File not found.")
        return []

COMMON_PASSWORDS = set(load_common_passwords("2020-200_most_used_passwords.txt"))


}
