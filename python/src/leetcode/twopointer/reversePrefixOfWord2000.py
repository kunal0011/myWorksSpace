class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        tempWord = word
        i = word.find(ch)
        if(i == -1):
            return tempWord
        return word[0:i+1][::-1]+tempWord[i+1:]
    
class Solution1:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word
        left = 0
        right = index
        word = list(word)
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return ''.join(word)   
    

if __name__  == '__main__':
    s =Solution1()
    print(s.reversePrefix("abvd","d"))    