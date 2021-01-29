from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    shorter = nums1
    longer = nums2
    if len(shorter) > len(longer):
        shorter, longer = longer, shorter
    
    shorter_min = 0
    shorter_max = len(shorter)
    # print(shorter)
    while shorter_min <= shorter_max:
        shorter_index = (shorter_max + shorter_min) // 2
        longer_index = (len(longer) + len(shorter) + 1 ) // 2 - shorter_index
        # print(shorter_index)

        if shorter_index > 0 and shorter[shorter_index - 1] > longer[longer_index]:
            shorter_max = shorter_index - 1

        elif shorter_index < len(shorter) and longer[longer_index - 1] > shorter[shorter_index]:
            shorter_min = shorter_index + 1
        
        else:
            max_left = 0
            if shorter_index == 0:
                max_left = longer[longer_index - 1]
            elif longer_index == 0:
                max_left = shorter[shorter_index - 1]
            else:
                max_left = max(shorter[shorter_index - 1], longer[longer_index - 1])

            if (len(shorter) + len(longer)) % 2 == 1:
                return max_left

            min_right = 0
            if longer_index == len(longer):
                min_right = shorter[shorter_index]
            elif shorter_index == len(shorter):
                min_right = longer[longer_index]
            else:
                min_right = min(shorter[shorter_index], longer[longer_index])

            return (max_left + min_right) / 2.0

    raise ValueError

if __name__ == '__main__':
    print('yolo')
    print(findMedianSortedArrays([1,2,3], [4,5]))
    print(findMedianSortedArrays([1,4,5],[2,3]))
    print(findMedianSortedArrays([1], []))
