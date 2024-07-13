class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1 :
            return True

        
        def dfs(cour):
            if cour in _set:
                return False
            if cour in visited:
                return True
            _set.add(cour)
            for x in graph[cour]:
                if not dfs(x):
                    return False
            _set.remove(cour)
            visited.add(cour)
            return True


        _set = set()
        visited = set()
        graph = collections.defaultdict(list)
        for cour, pre in prerequisites:
            graph[cour].append(pre)
        
        for x in list(graph):
            if not dfs(x):
                return False
        return True

        
        