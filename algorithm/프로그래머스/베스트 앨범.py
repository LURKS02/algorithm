import heapq
from collections import defaultdict

def solution(genres, plays):
    genreCount = defaultdict(int)
    songCount = defaultdict(list)

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        genreCount[genre] += play

        heapq.heappush(songCount[genre], (-play, i))

    items = list(genreCount.items())
    items.sort(key=lambda x: (-x[1]))

    answer = []
    for item in items:
        genre = item[0]
        answer.append(heapq.heappop(songCount[genre])[1])
        if len(songCount[genre]) > 0:
            answer.append(heapq.heappop(songCount[genre])[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))