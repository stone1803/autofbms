import codecs
import random
with codecs.open("test.txt", "r",encoding='utf8') as f:
    list2 = []
    for item in f:
        number = 0
        while number < 5:
            list2.append(item + str(number))
            number += 1
    print(random.choice(list2))