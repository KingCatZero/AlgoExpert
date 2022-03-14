# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
		length = len(string)
		
		for i in range(length):
			suffix = self.root
			
			for j in range(i, length):
				if string[j] not in suffix:
					suffix[string[j]] = {}
					
				suffix = suffix[string[j]]
				
			suffix[self.endSymbol] = True					
			
    def contains(self, string):
		suffix = self.root
		
        for c in string:
			if c in suffix:
				suffix = suffix[c]
			else:
				return False
		
		return self.endSymbol in suffix
