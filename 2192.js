// 2192. All Ancestors of a Node in a Directed Acyclic Graph
/*
You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG). The nodes are numbered from 0 to n - 1 (inclusive).
You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a unidirectional edge from fromi to toi in the graph.
Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.
A node u is an ancestor of another node v if u can reach v via a set of edges.
*/

var getAncestors = function(n, edges) {
    const output = []
    const heads = new Set()
    for (let i = 0; i < n; i++) {
        output.push(new Set())
        heads.add(i)
    }
    const dirs = {}
    for (const edge of edges) {
        const from = edge[0]
        const to = edge[1]
        heads.delete(to)
        if (dirs[from]) {
            dirs[from].push(to)
        } else {
            dirs[from] = [to]
        }
    }
    let q = Array.from(heads)
    while (q.length) {
        const qLen = q.length
        const nxt = new Set()
        for (let i = 0; i < qLen; i++) {
            const val = q.shift()
            const children = dirs[val] || []
            for (const child of children) {
                output[child].add(val)
                const ancestors = output[val]
                for (const ancestor of ancestors) {
                    output[child].add(ancestor)
                }
                nxt.add(child)
            }
        }
        q = Array.from(nxt)
    }
    for (let i = 0; i < n; i++) {
        output[i] = Array.from(output[i])
        output[i].sort((a, b) => a - b)
    }
    return output
};

console.log(getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))
console.log(getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]))