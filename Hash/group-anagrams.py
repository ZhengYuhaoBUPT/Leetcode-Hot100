class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # make hashtable
        hashtable = collections.defaultdict(list)

        # for every str in strs, we need to add it in to hashtable
        # but in order
        for mystr in strs:
            # for mystr, get the sorted order as the key
            # we need to notice that in this mystr is not changed
            mykey = "".join(sorted(mystr))

            # use the original mystr as the value
            hashtable[mykey].append(mystr)

        return list(hashtable.values())
