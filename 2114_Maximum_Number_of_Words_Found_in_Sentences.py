class Solution(object):
    def mostWordsFound(self, sentences):
        return max(len(sentence.split()) for sentence in sentences)
    
    #sentence.split() splits a string into a list of words by using spaces as the default delimiter.
    #len() counts the number of words in each sentence.
    #max() finds the maximum count among all sentences.