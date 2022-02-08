# works properly
def strip_punctuation(word):
    for i in punctuation_chars:
        word=word.replace(i,"")
    return word

def get_pos(str):
    count=0
    strg=strip_punctuation(str.lower())
    strli=strg.split()
    for word in strli:
        if word in positive_words:
            count=count+1
    return count

def get_neg(str):
    count=0
    strg=strip_punctuation(str.lower())
    strli=strg.split()
    for word in strli:
        if word in negative_words:
            count=count+1
    return count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

with open("resulting_data.csv","w") as result:
    with open("project_twitter_data.csv") as twt_data:
        lines=twt_data.readlines()
        result.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
        for line in lines[1:]:
            data=line.split(",")
            pos_twt=get_pos(data[0])
            neg_twt=get_neg(data[0])
            retweets=data[1]
            replies=data[2].strip()
            print(retweets,replies,pos_twt,neg_twt)
            result.write("{},{},{},{},{}".format(retweets,replies,pos_twt,neg_twt,pos_twt-neg_twt))
            result.write("\n")