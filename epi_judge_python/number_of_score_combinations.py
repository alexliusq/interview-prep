from typing import List

from test_framework import generic_test

## works but is stupid slow
# def num_combinations_for_final_score(final_score: int,
#                                      individual_play_scores: List[int]) -> int:
#     def next_play(sum, play_index):
#         if play_index == len(individual_play_scores):
#             if sum == final_score:
#                 result[0] += 1
#             return
#         play_points = individual_play_scores[play_index]
#         max_plays = (final_score - sum) // play_points
#         for possible_play_count in range(0, max_plays + 1):
#             next_play(sum + possible_play_count * play_points, play_index + 1)

#     result = [0]
#     print(final_score, individual_play_scores)
#     next_play(0, 0)
#     return result[0]

## naive implementation 2
# def num_combinations_for_final_score(final_score: int,
#                                      individual_play_scores: List[int]) -> int:
#     def combinations_for_score(score):
#         current_set = set([])
#         for index, play in enumerate(individual_play_scores):
#             if score - play < 0:
#                 continue
#             possible_combinations = result[score - play]
#             for combination in possible_combinations:
#                 incremented = list(combination)
#                 incremented[index] += 1
#                 current_set.add(tuple(incremented))
#                 # print(result)
#         result.append(current_set)

#     score_0 = tuple([0] * len(individual_play_scores))

#     result: List[set] = [set([score_0])]

#     for score in range(1, final_score + 1):
#         combinations_for_score(score)
#     # print(result)
#     return len(result[final_score])

def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:


    result = [[1] + [0] * final_score for _ in range(len(individual_play_scores))]
    # print(result)
    for play_index, play in enumerate(individual_play_scores):
        for score_index in range(1, final_score + 1):
            num_combinations = 0
            if score_index >= play:
                num_combinations += result[play_index][score_index  - play]
            if play_index >= 1:
                num_combinations += result[play_index - 1][score_index]
            result[play_index][score_index] = num_combinations
    # print(result)
    return result[len(individual_play_scores) - 1][final_score]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
