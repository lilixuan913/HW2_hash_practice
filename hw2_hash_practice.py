# -*- coding: utf-8 -*-
"""HW2_hash_practice

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1krAph0MLOMVIIXloQ_k2LJfU61vkKfzZ
"""

from google.colab import files
uploaded = files.upload()

import matplotlib.pyplot as plt
input_filename = 'hw2_data.txt'
output_filename = 'result.png'
#讀取
word_count = {}
with open(input_filename,'r') as f:
    for line in f:
        word = line.strip()
        if word:
            word_count[word] = word_count.get(word, 0) + 1
#統計、處理
unique_count = len(word_count)
sorted_word_count = sorted(word_count.items(), key=(lambda item:-item[1]))
print("1.相異個數=",unique_count)
print("2.次數統計")
for word,count in sorted_word_count:
    print(word,'=',count)
#繪圖
words,counts = [item[0] for item in sorted_word_count],[item[1] for item in sorted_word_count]
plt.figure()
plt.bar(words, counts)
plt.xlabel("word")
plt.ylabel("count")
plt.title("word count")
plt.savefig(output_filename)