class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        x, y = 0, 1
        x_counter, y_counter = 0, 1
        array = [nums[x]]
        triplets = 0

        for n in nums:

            # This line restarts the array and add the value of nums[x] to it
            array = [nums[x]]

            while True:
                
                # This line validates that y have a valid number to avoid an Error
                if y >= len(nums):
                    break

                # This block compares values, adds them to the array and check for triplets completion.
                if nums[x] != nums[y]:

                    if nums[y] not in array:
                        array.append(nums[y])

                    if len(array) == 3:
                        triplets += 1
                        break

                # This line increments the value of y
                y += 1
            # This lines increments x and y counters and restart x and y
            x_counter += 1
            y_counter += 1
            x, y = x_counter, y_counter
        
        return triplets
