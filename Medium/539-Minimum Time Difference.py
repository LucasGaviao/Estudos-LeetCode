class Hora:
    def __init__(self, h="00:00"):
        self.hora = int(h[:2])
        self.min = int(h[3:])

    def toMin(self):
        return 60*self.hora + self.min
    def __str__(self):
        return str(self.hora) + ":" + str(self.min)

    '''def __sub__(self, outro):
        novo = Hora()
        novo.hora = self.hora - outro.hora
        
        novo.min = self.min - outro.min
        if novo.min < 0:
            novo.min = 60 + novo.min
            novo.hora -= 1
        if novo.hora < 0:
            novo.hora = 24 + novo.hora
        return novo'''

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [Hora(timePoints[i]).toMin() for i in range(len(timePoints))]
        timePoints.sort()
        m = 720
        for i in range(1, len(timePoints)):
            m = min(m, min(timePoints[i]-timePoints[i-1],timePoints[i-1]+1440-timePoints[i]))
            if m == 0:
                return m
        m = min(m, min(timePoints[-1]-timePoints[0],timePoints[0]+1440-timePoints[-1]))
        return m