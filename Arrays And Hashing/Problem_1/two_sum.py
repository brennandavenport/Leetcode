class solution(object):
    def twosum(self, target, array):
        map = {}
        for cur in range(len(array)):
            x = target - array[cur]
            if map.get(x) == None:
                map[array[cur]] = cur
            else:
                return [map.get(x), cur]
        return None
            

s = solution()
arr = [2,7,11,15,15]
son = s.twosum(30, arr)
print(son)
