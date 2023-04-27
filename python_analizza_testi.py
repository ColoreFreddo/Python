class TextAnalyzer:
    def __init__(self, file_path):
        self.words_count = {}
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    self.words_count[word] = self.words_count.get(word, 0) + 1

    def most_frequent_word(self):
        return max(self.words_count, key=self.words_count.get)

analyzer = TextAnalyzer('test.txt')
most_frequent = analyzer.most_frequent_word()
print("La parola con frequenza maggiore:", most_frequent)