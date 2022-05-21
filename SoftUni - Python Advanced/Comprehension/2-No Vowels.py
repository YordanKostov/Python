word = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
filtered = [x for x in word if x not in vowels]
print(f"{''.join(filtered)}")