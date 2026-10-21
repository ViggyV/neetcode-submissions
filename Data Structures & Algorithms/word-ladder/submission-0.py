class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not endWord in wordList:
            return 0
        wLen = len(beginWord)
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(wLen):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)


        #bfs
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(wLen):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1

        return 0

