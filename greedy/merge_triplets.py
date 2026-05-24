class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        achieved=set()
        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]>target[1] or triplet[2]>target[2]:
                continue
        
            for k in range(len(triplet)):
                if triplet[k]==target[k]:
                    achieved.add(k)

            if  len(achieved)==3:
                return True
        
        return False
