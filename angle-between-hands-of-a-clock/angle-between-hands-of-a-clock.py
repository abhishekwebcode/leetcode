class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12:
            hour = 0
        hourangle = ( (hour/12)*360 ) + minutes/2
        minuteangle = (minutes/60)*360
        print(hourangle,minuteangle)
        deg = abs(hourangle-minuteangle)
        return min(deg,abs(360-deg))