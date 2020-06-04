words = [w.strip() for w in open("wordlist_10000.txt").readlines()]
for length in range(1, 8):
    alphabets_dict = {}
    for w in words:
        if len(w) < length:
            continue
        for i in range(len(w) - length+1):
            if alphabets_dict.get(w[i:i + length]) is None:
                alphabets_dict[w[i:i + length]] = 1
            else:
                alphabets_dict[w[i:i + length]] += 1
    lmax = max([n for w, n in alphabets_dict.items()])
    print(sorted(list(alphabets_dict.items()), key=lambda x: x[1], reverse=True)[0])

