# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку

text = '''It is not necessary to hold a strong reference (i.e. increment the reference count) 
for every local variable that contains a pointer to an object. 
In theory, the object’s reference count goes up by one when the variable 
is made to point to it and it goes down by one when the variable goes out of scope. 
However, these two cancel each other out, so at the end the reference count 
hasn’t changed. The only real reason to use the reference count is to prevent 
the object from being deallocated as long as our variable is pointing to it. 
If we know that there is at least one other reference to the object that 
lives at least as long as our variable, there is no need to take a new strong 
reference (i.e. increment the reference count) temporarily. 
An important situation where this arises is in objects that are passed as arguments 
to C functions in an extension module that are called from Python; 
the call mechanism guarantees to hold a reference to every 
argument for the duration of the call
'''

words = text.split()
print(words)

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

top_words = sorted_words_count[:10]

print(top_words)
