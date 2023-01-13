from Trie import Trie

#countdownSolver finds all the word that can be made using a 9 letter long string, so as to work as a solver for the
# gameshow COUNTDOWN, it does this by generating a Trie from all the permutations, and iterating
#the whole dictionary through it
def countdownSolver(letters):
    def permute(word):
        if len(word) == 1:
            return [word]

        permutations = []
        for i, letter in enumerate(word):
            remaining_word = word[:i] + word[i + 1:]
            for permutation in permute(remaining_word):
                permutations.append(letter + permutation)
        return permutations
    letters=letters.upper()
    t = Trie()
    for end in permute(letters):
        t.insert(end)
    answer = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}

    with open("dictionary.txt") as file:
        while (line := file.readline()):
            line = line.strip()
            if t.search(line):
                answer[str(len(line))].append(line)
    #The answer is returned with the highest scoring words first
    return answer

