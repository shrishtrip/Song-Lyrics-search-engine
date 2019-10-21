import pandas as pd

df_words = pd.read_csv('bag_of_words.txt',delim_whitespace=False,sep = ',',encoding="ISO-8859-1",header=None)
# df = pd.read_csv('mxm_779k_matches.txt', delim_whitespace=False, sep='<SEP>', header=None)

# df_words = df_words.transpose();
ls = df_words.astype(str).values.tolist()
ls = ls[0]                                      ##list of sorted words



# df_words = df_words.sort_values(by = 1 , axis=1)
# print(df_words)
