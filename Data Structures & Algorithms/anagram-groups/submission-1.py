class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        returned_dict = {}
        for s in strs: # iterate list
            in_order = "".join(sorted(s))
            sorted_list.append(in_order) # add values  
            # Check if the sorted word appears as a key
            if(in_order in returned_dict.keys()):
                # If it does, add it to the list of the associated key 
                val = returned_dict.get(in_order)
                val.append(s)
            else:
                returned_dict[in_order] = [s]
        returned_list = []
        for key_val in returned_dict.values():
            returned_list.append(key_val)
        return returned_list





        # Have the characters sorted 
        # Do not worry about anagrams
        # 
        # Now have to iterate through list finding matches 
        # Just realized I have to create a copy of the list.
        # Original words still needed
        # 
        # Hashmap with the key as the word, value as a list of it's anagrams
        # Will never be empty, the word itself is in the list
        # 
        # 
        # 