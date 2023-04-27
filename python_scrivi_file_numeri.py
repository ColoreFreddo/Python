class WordAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        
    def read_file(self):
        words = []
        with open(self.file_name, 'r') as f:
            for line in f:
                for word in line.strip().split():
                    words.append(word)
        return words
    
    def longest_words(self, n=1):
        words = self.read_file()
        sorted_words = sorted(words, key=len, reverse=True)
        return sorted_words[:n]
    
file_name = 'test.txt'
analyzer = WordAnalyzer(file_name)
longest_word = analyzer.longest_words()
print(longest_word)