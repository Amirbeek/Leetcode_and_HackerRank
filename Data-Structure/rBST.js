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

    rContains(value, currentNode = this.root){
        if (currentNode === null) return false
        if (value === currentNode.value) return  currentNode
        if (value < currentNode.value){
            return this.rContains(value, currentNode.left)
        }else{
            return this.rContains(value, currentNode.right)
        }
    }
    #rInsert(value, currentNode = this.root){
        if (currentNode === null) return new Node(value)
        if (value < currentNode.value){
            currentNode.left = this.#rInsert(value, currentNode.left);
        }else if (value > currentNode.value){
            currentNode.right = this.#rInsert(value, currentNode.right);
        }
        return currentNode

    }
    rInsert(value){
        if (this.root === null) this.root = new Node(value)
        this.#rInsert(value)
    }
    minValue(currentNode ){
        while(currentNode.left !== null){
            currentNode = currentNode.left;
        }
        return currentNode;
    }
    #deleteNode(value, currentNode) {
        if (currentNode === null) return null;

        if (value < currentNode.value) {
            currentNode.left = this.#deleteNode(value, currentNode.left);
        } else if (value > currentNode.value) {
            currentNode.right = this.#deleteNode(value, currentNode.right);
        } else {
            // Tugun topildi, endi uni o'chiramiz
            if (currentNode.left === null && currentNode.right === null) {
                return null;
            } else if (currentNode.right === null) {
                currentNode = currentNode.left;
            } else if (currentNode.left === null) {
                currentNode = currentNode.right;
            } else {
                // O'ng kichik daraxtdan minimal qiymatni topamiz
                let subTreeMin = this.minValue(currentNode.right);
                currentNode.value = subTreeMin;
                // Endi o'ng kichik daraxtdan minimal qiymatni o'chiramiz
                currentNode.right = this.#deleteNode(subTreeMin, currentNode.right);
            }
        }
        return currentNode;
    }

    deleteNode(value){
        this.root = this.#deleteNode(value, this.root)
    }

}
let myTree = new BST()
myTree.rInsert(2)
myTree.rInsert(1)
myTree.rInsert(3)
// console.log(myTree)
console.log("\nRoot " + myTree.root.value)

console.log("\nRoot -> Left " + myTree.root.left.value);

console.log("\nRoot -> Right " + myTree.root.right.value);
// console.log(myTree.root)