class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:  

        look_up = collections.defaultdict(dict)

        for (x, y), value in zip(equations, values):
            look_up[x][y] = value
            look_up[y][x] = 1.0 / value

        def DFS(x, y, visit):
            if x not in look_up or y not in look_up:
                return -1.0
            
            if y in look_up[x]: 
                return look_up[x][y]
            
            for i in look_up[x]:
                if i in visit:
                    continue
                visit.add(i) 
                tmp = DFS(i, y, visit)

                if tmp == -1.0: 
                    continue 
                else:
                    return look_up[x][i] * tmp
                
            return -1.0

        res=[]
        for x, y in queries:
            res.append(DFS(x, y, set()))
        
        return res