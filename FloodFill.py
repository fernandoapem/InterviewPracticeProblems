from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        self.recursiveFlood(image,sr,sc,color,startingColor)
        return image
    def recursiveFlood(self,image: List[List[int]], sr: int, sc: int, color: int, ogColor: int):
        if (sr not in range(0,len(image))) or (sc not in range(0,len(image[sr]))) or (image[sr][sc] == color) or (image[sr][sc] != ogColor):
            return
        image[sr][sc] = color
        self.recursiveFlood(image,sr+1,sc,color,ogColor)
        self.recursiveFlood(image,sr-1,sc,color,ogColor) 
        self.recursiveFlood(image,sr,sc-1,color,ogColor) 
        self.recursiveFlood(image,sr,sc+1,color,ogColor)
p = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
image2 = [[0,0,0],[0,0,0]]
print(p.floodFill(image,1,1,2))
print(p.floodFill(image2,0,0,0)) 