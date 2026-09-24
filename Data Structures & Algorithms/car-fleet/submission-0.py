class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p,s) for p,s in zip(position,speed)],reverse=True)
        # sorted in descending position (ascending distance to target)
        # if the car in front of me would finish earlier: im a new fleet
        # if the car in front of me would finish later: join its fleet

        numFleets = 0
        currentFleetTime = 0
        for p,s in cars:
            time = (target-p) / s
            if time > currentFleetTime:
                numFleets+=1
                currentFleetTime = time
        return numFleets
        