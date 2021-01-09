/* Binary Search Tree */

class Node {
  constructor(data, animal, question, left = null, right = null) {
    this.data = data;
    this.left = left;
    this.right = right;
    // this.x = x;
    // this.y = y;
    // this.level = level
    this.animal = animal
    this.question = question
  }
}



class BST {
  constructor() {
    this.root = null;
  }
  add(data, animal, question) {
    const node = this.root;
    let levelDepth = 1
    let counterLeft = 0
    let counterRight = 0
    let iter = 0
    if (node === null) {
      this.root = new Node(data, animal, question);
      return;
    } else {

      const searchTree = function (node) {
        // console.log(data);
        if (data != [] && data[iter] == 0) {
          if (node.left === null) {
            levelDepth++
            counterLeft++
            iter++

            node.left = new Node(data, animal, question);
            // console.log(levelDepth,"levelDepth-left");
            // console.log(node.data,node.x,"rigth",node.level);
            return;
          } else if (node.left !== null) {
            levelDepth++
            counterLeft++
            iter++
            // console.log(node.data,node.x,"left",node.level);
            return searchTree(node.left);
          }
        } else if (data != [] && data[iter] == 1) {
          if (node.right === null) {
            levelDepth++
            counterRight++
            iter++

            // console.log(levelDepth,"levelDepth-right");
            node.right = new Node(data, animal, question);
            // find nivel
            // console.log(node.data,node.x,"rigth",node.level);
            return;
          } else if (node.right !== null) {
            levelDepth++
            counterRight++
            iter++
            // console.log(node.data,node.x,"rigth",node.level);
            return searchTree(node.right);
          }
        } else {
          return null;
        }
      };
      return searchTree(node);
    }
  }
}



// Convert array to tree

const btsJSON = require('./scraperData.json');
const bst = new BST();
for (var i = 0; i < btsJSON.length; i++) {
  bst.add(btsJSON[i].pattern, btsJSON[i].animal, btsJSON[i].question);
}


let stringTree = JSON.stringify(bst)
console.log(stringTree);

fs = require('fs');
fs.writeFile('treeData.json', stringTree, function (err) {
  if (err) return console.log(err);
});

