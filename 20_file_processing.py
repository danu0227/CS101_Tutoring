import random

random.seed()
# random inteager file generate
for i in range(1, 11):
    f = open("datas/random_%d.txt" % i, 'w')
    for j in range(2000):
        f.write("%d\n" % random.randint(0, 100))
    f.close()

## Task 1
# draw histogram from random_1.txt ~ random_10.txt file
# create file with stat_1.txt ~ stat_10.txt
# write mean, most frequent, least frequent of each random_%d.txt to each stat_%d.txt
for i in range(1, 11):
    f = open("datas/random_%d.txt" % i, 'r')
    output_f = open("datas/stat_%d.txt" % i, 'w')
    datas = f.readlines()
    count = [0] * 101
    sum = 0
    for j in range(len(datas)):
        sum += int(datas[j])
        count[int(datas[j])] += 1
    mean = sum / len(datas)
    output_f.write("mean: %f\n" % mean)
    max = 0
    max_i = 0
    min = 2000
    min_i = 0
    for j in range(len(count)):
        if count[j] > max:
            max_i = j
        if count[j] < min:
            min_i = j
    output_f.write(" most frequent: %d\n" % max_i)
    output_f.write("least frequent: %d\n" % min_i)
    for j in range(len(count)):
        output_f.write("%3d: " % j + "#" * count[j] + "\n")
    output_f.close()

## Task 2
# read Pride_and_Prejudice.txt file
# filter each line in the file so that it contains alphabet character and blank only.
# calculate frequent of each words.
# after calculating frequent of each words, sort the dictionary from most frequent to least frequent.
# write each items in dictionary to the file Pride_and_Prejudice_stat.txt in the sorted order.
f = open("datas/Pride_and_Prejudice.txt", encoding='utf8')
freq_dict = {}
for l in f.readlines():
    line = ""
    for c in l:
        if c.isalpha() or c == " ":
            line += c
    for i in line.split():
        if freq_dict.get(i, None) == None:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1

freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
output_f = open('datas/Pride_and_Prejudice_stat.txt', 'w', encoding='utf8')
output_f.write("%25s" % 'word' + "%25s\n" % 'count')
for k, v in freq_dict.items():
    output_f.write("%25s" % str(k) + "%25s\n" % str(v))
output_f.close()