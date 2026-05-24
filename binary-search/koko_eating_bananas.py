class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles) # this represents the max no of babanas koko can eat in an hr 
        while(left<right):
            k=(left+right)//2
            hr=0
            for pile in piles:
                hr+= ceil(pile/k)
            print(f'k:{k}, hr:{hr}')
            if hr<=h:
                right=k
            else:
                left=k+1
            print(f'left:{left}, right:{right}')

        return left


        
