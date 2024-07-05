class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.con = combinationLength
        self.combina = []
        self.combina = self.combina_f(characters, combinationLength)
        self.id = -1

    def combina_f(self, char, c):
        # de quy

        if c == 1:
            ls = []
            for i in range(len(char)):
                ls.append(char[i])
            return ls
        else:
            ls = []
            for i in range(len(char) - c + 1):
                str_ = char[i + 1:]
                ls2 = self.combina_f(str_, c - 1)
                for j in range(len(ls2)):
                    ls.append(char[i] + ls2[j])
            return ls

    def next(self) -> str:
        if self.id < len(self.combina):
            self.id += 1
            return self.combina[self.id]

    def hasNext(self) -> bool:
        if self.id < len(self.combina) - 1:
            return True
        return False