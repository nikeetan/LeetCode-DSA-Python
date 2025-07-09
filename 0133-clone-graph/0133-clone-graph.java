/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null){
            return node;
        }
        Deque<Node> queue = new ArrayDeque<>();
        HashMap<Node, Node> Nodemap = new HashMap<>();
        queue.add(node);
        Nodemap.put(node, new Node(node.val, new ArrayList<>()));
        while(!queue.isEmpty()){
            Node currNode = queue.removeFirst(); 
            List<Node> neighborslist;
            neighborslist = currNode.neighbors;
            for(Node neiNode : neighborslist){
                if(!Nodemap.containsKey(neiNode)){
                    queue.add(neiNode);
                    Nodemap.put(neiNode, new Node(neiNode.val, new ArrayList<>()));
                }
                Nodemap.get(currNode).neighbors.add(Nodemap.get(neiNode));
            }
        }
        return Nodemap.get(node);
    }
}