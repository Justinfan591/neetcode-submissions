class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort everything to decending order
        cars = []
        ans = 1
        for i in range(0, len(position)): 
            pos, spee = position[i], speed[i]
            cars.append((pos,spee))
        cars.sort(reverse = True) #decending order for position
        curMaxTime = (target - cars[0][0])/cars[0][1]
        for i in range(1, len(position)): 
            pos, spee = cars[i][0], cars[i][1]
            time = (target - pos)/spee
            if time > curMaxTime: 
                ans += 1
                curMaxTime = time
        return ans

        
