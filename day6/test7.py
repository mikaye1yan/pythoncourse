scrambled_letters_1 = ['g', 'e', 'o']
positions_1 = [1, 0, 2]
scrambled_letters_2 = ['e', 't', 's', 't']
positions_2 = [3, 0, 2, 1]
scrambled_letters_3 = ['b', 'e', 't', 'i', 'd', 'a']
positions_3 = [1, 4, 5, 0, 3, 2]
word_dict_1 = {positions_1[i]: scrambled_letters_1[i] for i in range(len(scrambled_letters_1))}
word_dict_2 = {positions_2[i]: scrambled_letters_2[i] for i in range(len(scrambled_letters_2))}
word_dict_3 = {positions_3[i]: scrambled_letters_3[i] for i in range(len(scrambled_letters_3))}
unscrambled_word_1 = ''.join(word_dict_1[key] for key in sorted(word_dict_1.keys()))
unscrambled_word_2 = ''.join(word_dict_2[key] for key in sorted(word_dict_2.keys()))
unscrambled_word_3 = ''.join(word_dict_3[key] for key in sorted(word_dict_3.keys()))
print(unscrambled_word_1)  
print(unscrambled_word_2)  
print(unscrambled_word_3)  
