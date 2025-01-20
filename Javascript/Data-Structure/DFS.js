class Node{
    constructor(value) {
        this.value = value
        this.left =  null
        this.right = null
    }
}
class BST{
    constructor() {
        this.root = null
    }
    insert(value){
        const newNode = new Node(value);
        if (this.root == null) {
            this.root = newNode
            return this
        }
        let temp = this.root
        while(true){
            if (newNode.value === temp.value) return undefined
            if (newNode.value < temp.value){
                if (temp.left === null){
                    temp.left = newNode
                    return this
                }
                temp = temp.left
            }else{
                if (temp.right === null){
                    temp.right = newNode
                    return this
                }
                temp = temp.right
            }
        }
    }


    BFS(){
        let currentNode = this.root
        let queue = []
        let result = []
        queue.push(currentNode)
        while(queue.length){
            currentNode =  queue.shift()
            result.push(currentNode.value)
            if (currentNode.left) queue.push(currentNode.left)
            if (currentNode.right) queue.push(currentNode.right)
        }
        return result
    }
    DFSreOrder(){
        let result = []
        function traversal(currentNode) {
            result.push(currentNode.value)
            if (currentNode.left) traversal(currentNode.left)
            if (currentNode.right) traversal(currentNode.right)
        }
        traversal(this.root)
        return result
    }
    DFSPostOrder(){
        let result = []
        function traverse(currentNode) {
            if (currentNode.left) traverse(currentNode.left)
            if (currentNode.right) traverse(currentNode.right)
            result.push(currentNode.value)
        }
        traverse(this.root)
        return result
    }
    DFSInOrder(){
        let result = []
        function traverse(currentNode) {
            if (currentNode.left) traverse(currentNode.left)
            result.push(currentNode.value)
            if (currentNode.right) traverse(currentNode.right)
        }
        traverse(this.root)
        return result
    }
}
let myTree = new BST()
myTree.insert(47)
myTree.insert(21)
myTree.insert(76)
myTree.insert(18)
myTree.insert(27)
myTree.insert(52)
myTree.insert(82)

console.log("BST :   "+[47,21,76,18,27,52,82])
console.log("DFS ReOrder:  "+myTree.DFSreOrder())
console.log("DFS PostOrder:  "+myTree.DFSPostOrder())
console.log("DFS InOrder:  "+myTree.DFSInOrder())