import os
import re


def opener():
    os.chdir("D:\Coding\Python\words")
    f = open("aaa.txt", encoding='unicode_escape').read().lower()

    word_power = int(input("Enter your level out of 5 >>>")) #asking for Rank between 1 to 5 

    rank = open('best rank.txt').read().split()[: word_power * 10000]
    my_rank = open('my rank word only.txt').read().split()[: word_power * 1000]
    verb = open('1000  verbs with  verb forms.txt', 'r').read().split()[:word_power * 1500]
    adjectives = open('adjectives.txt', 'r').read().split()
    main = open('main.txt', 'r').read().split("\n")[: word_power * 1000]
    PrefixSuffix = open("prefix-suffix.txt").read().split("\n\n")
    prefix = PrefixSuffix[0].split(" ")
    suffix = PrefixSuffix[1].split(" ")
    known_words = set(main + verb + adjectives + rank[:word_power * 1000] + my_rank)

    subtitle = [i for i in re.findall('[a-z\']+', f) if i in rank]
    important = [i for i in subtitle if i not in known_words]
    temp = set(important)
    length = len(temp)
    input(f"Total word for main process {len(temp)}\nwaiting for conformation....")
    return temp, known_words, length, important, prefix, suffix, subtitle, rank


def main(temp, known_words, length, prefix, suffix):
    not_removed, repeated = [], {}
    for j, i in enumerate(temp.copy()):
        if not j % 10:
            print(f"\r processing {j * 100 // length}{str('%')} complect.", end="")
        for j in prefix:
            for k in suffix:

                if (j + i + k) in known_words or (j + i[:-1] + k) in known_words or (j + i + i[-1] + k) in known_words:
                    temp.remove(i)
                    break

                elif (j + i + k) in not_removed or (j + i[:-1] + k) in not_removed or (
                        j + i + i[-1] + k) in not_removed:
                    temp.remove(i)
                    repeated[i] = j+i+k
                    break
                elif i[-1] == 'y':
                    if (j + i[:-1] + 'i' + k) in known_words:
                        temp.remove(i)
                        break

                a = i[len(j): -len(k)] if len(k) > 0 else i[len(j):]

                if i.startswith(j) and i.endswith(k) and len(a) == len(i) - len(j + k):
                    if a + 'e' in known_words:
                        temp.remove(i)
                        break

                    elif a + 'e' in not_removed:
                        temp.remove(i)
                        repeated[i] = a+'e'
                        break

                    for m in prefix:
                        for n in suffix:
                            if (m + a + n) in known_words or (m + a[:-1] + n) in known_words:
                                temp.remove(i)
                                break
                            elif (m + a + n) in not_removed or (m + a[:-1] + n) in not_removed:
                                temp.remove(i)
                                repeated[i] = m+a+n
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break

            else:
                continue
            break
        not_removed.append(i)
    return repeated


def last(important, subtitle, rank, temp, repeated):
    important = [i for i in important if i in temp]
    main_words = list(dict.fromkeys(important))
    Only_Repetition_dct = {i: important.count(i) for i in main_words if important.count(i) > 1}
    Only_Repetition_lst = sorted(Only_Repetition_dct, key=lambda x: Only_Repetition_dct[x])
    Only_non_Repetition_lst = [i for i in main_words if i not in Only_Repetition_lst]
    dct = {rank.index(i): i for i in Only_non_Repetition_lst}  # temp
    Only_non_Repetition_lst = [dct[i] for i in sorted(dct.keys())[::-1]]  # in rank order

    print(f'\n\n\n\n\nTotal words {len(subtitle)},  important vocabulary {len(important)}\n')  # Total words and main + Repetition length
    print(f"Repeated words\n{repeated}\n")  # repeated words but different
    print(f'Words frequency more then one {len(Only_Repetition_lst)}\n{Only_Repetition_lst}\n')  # Words with frequency more then one
    print('Total words only one Repetition (main words) ', len(main_words))  # main words length
    print(f'Only one frequency Words {len(Only_non_Repetition_lst)}\n{Only_non_Repetition_lst}')  # only one frequency words
