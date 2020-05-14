Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
             
             
code:
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not len(tickets) or not len(tickets[0]):
            return []
        
        graph = collections.defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
            
        for src in graph:
            graph[src].sort(reverse=True)
        
        stack = []
        res = []
        stack.append("JFK")
        
        while stack:
            elem = stack[-1]
            
            if elem in graph and graph[elem]: 
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
        
        return res[::-1]
