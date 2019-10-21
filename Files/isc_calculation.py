import math
import csv
from porter2stemmer import Porter2Stemmer

idf=[]
with open("idf.csv","r") as idffile:
    idfreader=csv.reader(idffile)
    for each in idfreader:
        idf.append(each)
idf=idf[0]
idf_list=[float(q) for q in idf]

words = open("words.txt","r")   #opening words file
a=words.read().split(',')
dict={}
for k in range(1,5001):
    dict[a[k-1]]=k           #creating dictionary of word-index pairs
query=input().lower()    #getting query from user and converting to lowercase
#normalisation and tokenisation of query
query = query.replace("'m ", " am ")
query = query.replace("'re ", " are ")
query = query.replace("'ve ", " have ")
query = query.replace("'d ", " would ")
query = query.replace("'ll ", " will ")
query = query.replace(" he's ", " he is ")
query = query.replace(" she's ", " she is ")
query = query.replace(" it's ", " it is ")
query = query.replace(" ain't ", " is not ")
query = query.replace("n't ", " not ")
query = query.replace("'s ", " ")
punctuation = (',', "'", '"', ",", ';', ':', '.', '?', '!', '(', ')','{', '}', '/', '\\', '_', '|', '-', '@', '#', '*')
for p in punctuation:
    query = query.replace(p, '')
query=query.split()
#stemming of tokens
stemmer=Porter2Stemmer()
query=[stemmer.stem(q) for q in query]
q_vector=[]
for k in range(5000):
    q_vector.append(int(0))      #initialising query's tf-idf vector (q_vector)
n=len(query)
for k in range(n):
    if query[k] in dict:
        q_vector[dict[query[k]]-1]+=1    #frequency of word of appropriate index is incremented in q_vector (with the help of dict created above) if the query token is equal to the respective word of the dictionary
for k in range(5000):
    if q_vector[k]==0:
        q_vector[k]=float(0)
    else:
        q_vector[k]=1+math.log10(q_vector[k])    #tf of q_vector terms
        q_vector[k]=float(q_vector[k]*float(idf_list[k]))    #tf*idf of q_vector terms

docs=[]

with open("output.csv","r") as csvfile:
    csvreader=csv.reader(csvfile)
    for each in csvreader:
        docs.append(each)    #tf-idf vectors of tracks copied to docs
N=len(docs)
isc_score=[]
q_root=math.sqrt(sum(q_vector))
for each in docs:
    temp=float(0)
    track=[]
    for k in range(1,5001):
        track.append(float(each[k]))
    for k in range(5000):
        temp+=math.sqrt(q_vector[k]*track[k])
    temp/=q_root
    temp/=math.sqrt(sum(track)) #for each track in docs, ISC similarity is calculated with q_vector and is stored in temp
    temp_list=[]
    temp_list.append(temp)
    temp_list.append(each[0])
    isc_score.append(temp_list) #isc_score contains list of ISC_Similarity_Score_Of_Track_With_Query-Track_ID pairs

isc_score.sort()
isc_score=isc_score[::-1]  #ISC Scores are now in descending order along with their respective track IDs
f=open("music.txt","r")   #opening track details file
tracks={}
for each in f:
    r=each.split('<SEP>')
    tracks[r[0]]=r[1:]   #dictionary of Track_ID:Track_Details is created
k,ct=0,0
while ct<10:  #printing the top ten results based on ISC Similarity Scorew
    if isc_score[k][1] in tracks:   #checking whether the track is present in track details dataset. If yes, print the track details. Else, move to the next best result
        print("Top Result Number "+str(ct+1)+":")
        print("Track Name: "+tracks[isc_score[k][1]][1])
        print("Track Artist: "+tracks[isc_score[k][1]][0]+"\n")
        ct+=1
    k+=1