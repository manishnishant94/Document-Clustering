import nltk,string,numpy
from nltk.stem.snowball import SnowballStemmer
import string,numpy
sno = SnowballStemmer('english')
def rem(w):
    while (True):
        if(w.endswith('.')):
            w = w[:-1]
            continue
        if(w.endswith(':')):
            w = w[:-1]
            continue
        if(w.endswith((';','"','?' ))):
            w = w[:-1]
            continue
        if(w.endswith(',')):
            w = w[:-1]
            continue
        if(w.startswith(('0','1','2','3','4','5','6','7','8','9'))):
            w=w[1:]
            continue
        if(w.endswith(('0','1','2','3','4','5','6','7','8','9'))):
            w=w[:-1]
            continue
            
        break
    return sno.stem(w)

#start taking input
files = []
n = int(input("Enter no. of documents you have "))
for q in range(n):
    files.append('c'+ str(q) + '.txt')
print(files)
#create files for frequency of words

for q in range(len(files)):
    open('freq_'+files[q], 'w').close()
    
#create file to write word frequency
open('words.txt', 'w').close()

file_len = len(files)
stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

#Compute the frequency for each term.

for i in range(file_len):
    freq = {}
    text_doc = open(files[i],'r')
    text_string = text_doc.read().lower()
    #print (text_string)
    word_token = text_string.split()
    #print (word_token)
    for word in word_token:
	if(word in stopwords):
            continue
        word = rem(word)
        count = freq.get(word,0) #For key word, returns value or default if key not in dictionary
        #print (count)
        freq[word] = count +1
        print (freq[word])
    freq_list = freq.keys() #returns list of dictionary keys
    print (freq_list)

    open('words.txt', 'w').close()
    for words in freq_list:
        p=open('words.txt','a')
        p.write(str(words) +"\n")
        p.close()
    
        

    
    

