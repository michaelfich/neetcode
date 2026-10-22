from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key = num in nums, value = occurences of num
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        # bucket sort of nums
        buckets = [[] for _ in range(0, len(nums) + 1)]

        # place each digit in nums into a bucket based on number of occurences
        for num, occurrences in freq.items():
            buckets[occurrences].append(num)
        
        # loop over buckets, in reverse order, to get the most frequent elements
        top_k_elements = []
        for bucket in reversed(buckets):
            for num in bucket:
                top_k_elements.append(num)
                if len(top_k_elements) == k:
                    return top_k_elements
        
        return []