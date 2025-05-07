class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        x, y = 0, 1
        x_counter, y_counter = 0, 1
        array = [nums[x]]
        triplets = 0

        for n in nums:

            print('------------------------------')
            array = [nums[x]]
            while True:
                
                print(f'Array: {array}')
                print(f'x value = {nums[x]}')
                #print(f'y value = {nums[y]}')

                if y >= len(nums):
                    print('len validation')
                    break

                if nums[x] != nums[y]:
                    print('Comparison true')

                    if nums[y] not in array:
                        print('Looking for y in array')
                        array.append(nums[y])
                        print('Array: ', array)

                    if len(array) == 3:
                        print('len of array')
                        triplets += 1
                        break

                print('adding 1 to y')
                y += 1
            print("Finished while loop")

            print(f'Triplets in this completed loop: {triplets}')
            x_counter += 1
            y_counter += 1
            x, y = x_counter, y_counter
            #array = [nums[x]]

        print('Finished For loop')    
        print(f'Triplets: {triplets}')
        return triplets
