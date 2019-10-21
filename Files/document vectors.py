import pandas as pd
import math
import csv

file = open('mxm_dataset_test.txt','r')

idf_list = pd.read_csv('idf.csv',delim_whitespace=False,sep = ',',encoding="ISO-8859-1",header=None)
idf_list = idf_list.astype(float).values.tolist()
idf_list = idf_list[0]
print(idf_list)



train = {}
# idf_list = pd.read_csv('idf.csv',delim_whitespace=False,sep = ',',encoding="ISO-8859-1",header=None)

# idf_list  = []


def check(ls,j):
    for tup in ls:
        tup = str(tup)
        # print(type(tup),"\n")
        temp_ls = tup.split(':')
        if int(temp_ls[0]) == int(j):           ###  check for \n in the last entry
            # print("temp_ls[0]",temp_ls[0])
            # print("temp_ls[1]", temp_ls[1])
            # s_temp = temp_ls[1]
            # if s_temp[-1]=='n':
            #     s_temp = s_temp[:]
            return int(temp_ls[1])
    return int(-1)



def idf(j):
    # print("inside idf:",j)
    ans = int(0)
    final_ans = float(0)
    for each in train:
        # print("checking ",j,"is present ",each)
        temp_val = int(check(train[str(each)],j))
        if temp_val != int(-1):
            # print(each," found")
            ans = ans+1
            # print("ans ",ans)
        # else:
        #     print(each,"not found")
    # print("df:",ans)
    if ans == int(0):
        final_ans += 99999
    else:
        final_ans = float(math.log10(N/ans))
    return final_ans






def tf_idf(s,j):
    # score = float(0)
    temp_ls = train[s]
    check_value = int(check(temp_ls , j))
    if check_value != int(-1):
        tf = 1 + math.log10(check_value)
        # print("tf:",tf)
        idf_val = float(idf_list[j])
        # print("idf:",idf_val)

        score = float(tf * idf_val)
    else:
        score = float(0)

    return score





for each in file:       ##create a train ditionary
    record = each.split(',')
    # print(record)
    s = record[0]
    ls = record[2:]
    # print(ls)
    train[(s)] = ls
    # print(train)


N=int(len(train))
print("train made with size:",N)

      # caluclating idf values and writing in file
# for i in range(5000):
#     print("iteration:",i)
#     temp = idf(i+1)
#     print(temp)
#     idf_list.append(temp)
#
# w = csv.writer(open("idf.csv", "w"))        ## wrinting idf values
# w.writerow(idf_list)





# print(idf_list[0])




# doc_vect = {}       #declare dictionry of documnet vectors

# print((idf_list[1]))


#############################
cnt = int(0)
w = csv.writer(open("output.csv", "w",newline=''))


for each in train:      #calculate tf-idf score
    cnt = cnt + 1
    print(cnt)
    # if cnt>int(10):
    #     break
    print("************************\n")
    print("\n","vector making start ", each,":")
    ls_final = []
    # ls = []
    ls_final.append(each)
    for j in range(5000):
        # print("iteration no:",j," ")
        temp = float(tf_idf(each,j))
        # print(" ",temp," ")
        if temp == 0:
            ls_final.append(0)
        else:
            ls_final.append(temp)
    w.writerow(ls_final)
###################################





