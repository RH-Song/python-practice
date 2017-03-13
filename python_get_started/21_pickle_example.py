import pickle

dict_a = {'da':111,'key':222}

# write a pickle file
file = open('pickle_text.pickle','wb')
pickle.dump(dict_a,file)
file.close()

# read a pickle file
# if you use with, you needn't to close the file
# with open('pickle_text.pickle','rb') as file:
file = open('pickle_text.pickle','rb')
dict_b = pickle.load(file)
file.close()
print 'dict_a is ',dict_a
print 'dict_b is ',dict_b
