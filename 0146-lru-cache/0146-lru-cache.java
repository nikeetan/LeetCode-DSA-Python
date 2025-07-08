/*
Capacity : 2

{2 : Node2, 3 : Node3 }

doubly linked list
h - > Node - >  Node -> tail

h - >Node1-> Node3 -> tail
Node2 = prev key val next
O(1)
O(1)
*/ 
class Node{
    int key, value;
    Node prev, next;
    Node(int key, int value){
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}
class LRUCache {
    private HashMap<Integer, Node> map;
    private Node head, tail;
    private int capacity;
    public LRUCache(int capacity) {
        this.map = new HashMap<>(capacity);
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        this.head.next = tail;
        this.tail.prev = head;
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if(!map.containsKey(key)){
            return -1; 
        }
        else{
            Node node = map.get(key);
            remove(node);
            add(node);
            return node.value; 
        }
        
    }
    
    public void put(int key, int value) {
        if(!map.containsKey(key)){
            Node newNode = new Node(key, value);
            if (map.size() == capacity){
                remove(head.next);
            }
            add(newNode);
        }
        else{
            Node presentNode = map.get(key);
            presentNode.value = value;
            remove(presentNode);
            add(presentNode);
        }
    }

    public void remove(Node node)
    {
        Node prevNode = node.prev;
        prevNode.next = node.next;
        node.next.prev = prevNode;
        map.remove(node.key);
    }
    public void add(Node newNode){
        Node prevNode = tail.prev;
        prevNode.next = newNode;
        newNode.prev = prevNode;
        tail.prev = newNode;
        newNode.next = tail;
        map.put(newNode.key, newNode);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */