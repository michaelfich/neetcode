class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0
        product_left = [[1] for _ in range(size)]

        while i < size:
            if i == 0:
                product_left[i] = nums[i]
            else:
                product_left[i] = product_left[i - 1] * nums[i]
            i += 1

        product_right = [[1] for _ in range(size)]

        while i > 0:
            i -= 1
            if i == size - 1:
                product_right[i] = nums[i]
            else:
                product_right[i] = product_right[i + 1] * nums[i]

        product_except_self = []

        while i < size:
            if i == 0:
                # first element
                before_num = 1
                after_num = product_right[i + 1]
            elif i == size - 1:
                # last element
                before_num = product_left[i - 1]
                after_num = 1
            else:
                # middle element
                before_num = product_left[i - 1]
                after_num = product_right[i + 1]
            # product of nums before and nums after the current element
            product_except_self.append(before_num * after_num)
            i += 1

        return product_except_self