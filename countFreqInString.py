def countLetterFreq(s1):
    '''It will parse freq of any character in string'''
    counts={}
    for char in s1:
        if(char not in counts):
            counts[char]=0
        counts[char]=counts[char]+1
    return counts
def countWordFreq(str1):
    '''It will parse any freq of word in string .It is not case sensitive'''
    freq_words={}
    for char in str1.split():   
        if(char not in freq_words):
            freq_words[char]=0
        freq_words[char]=freq_words[char]+1
    return freq_words

with open("para.txt","a+") as f:
    f.write("Hello world my name is Akash Patel\n")
    f.write("Studying in St.John College of Engineering")
    f.seek(0)
    # print(f.read())
    dict=countLetterFreq(f.read())
    f.seek(0)
    dict2=countWordFreq(f.read())
    print(dict)
    print(dict2)