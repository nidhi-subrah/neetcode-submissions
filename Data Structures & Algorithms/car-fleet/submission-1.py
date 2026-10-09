class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions and speeds, and sort by position in descending order (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        prev_time = 0  # Time taken by the fleet ahead
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If the current car takes longer than the fleet ahead, it cannot catch up.
            # Thus, it forms a new fleet.
            if time_to_target > prev_time:
                fleets += 1
                prev_time = time_to_target
                
        return fleets






        