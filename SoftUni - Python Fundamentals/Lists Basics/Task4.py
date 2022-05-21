n = int(input())
word = input()
my_list = []
filtered_list = []
for index in range(n):
    current_sentence = input()
    my_list.append(current_sentence)
print(my_list)
for sentence in my_list:
    if word in sentence:
        filtered_list.append(sentence)
print(filtered_list)