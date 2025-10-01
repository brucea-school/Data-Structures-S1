

def num_vowels(data: str) -> int:
    vow = 0
    data = data.lower()
    for i in data:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vow += 1
    return vow


print(num_vowels("Hello world"))
