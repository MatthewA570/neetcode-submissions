from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # would this not be just linear time complexity with
        # another HashMap with key = int and val = count
        count: dict[int, int] = {}
        returned_list = []
        for val in nums:
            if(val in count.keys()):
                count[val] += 1
            else:
                count[val] = 1
        # now have to find the highest frequency vals in dictionary 
        sorted_dict = dict(sorted(count.items(), key=itemgetter(1), reverse=True))
        print(sorted_dict)
        for i in range(k):
            val = list(sorted_dict)[i]
            returned_list.append(val)
        return returned_list
        
        

