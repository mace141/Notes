// [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, maxValue, that takes in array of numbers as an argument. 
// The function should return the largest number in the array.
//
// Solve this without using any built-in array methods.
//
// You can assume that the array is non-empty.
//
// test_00:
// maxValue([4, 7, 2, 8, 10, 9]); // -> 10
//
// test_01:
// maxValue([10, 5, 40, 40.3]); // -> 40.3
//
// test_02:
// maxValue([-5, -2, -1, -11]); // -> -1
//
// test_03:
// maxValue([42]); // -> 42
//
// test_04:
// maxValue([1000, 8]); // -> 1000
//
// test_05:
// maxValue([1000, 8, 9000]); // -> 9000

const maxValue = (nums) => {
  let i = 0;
  let max = nums[i];

  while (nums[i]) {
    if (nums[i] > max) {
      max = nums[i]
    }
    i++
  }
  
  return max;
};

// ========================= Solution =========================
//
// const maxValue = (nums) => {
//   let maximum = -Infinity;
//
//   for (let num of nums) {
//     if (num > maximum) maximum = num;
//   }
//
//   return maximum;
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #2 is prime ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, isPrime, that takes in a number as an argument. The function 
// should return a boolean indicating whether or not the given number is prime.
//
// A prime number is a number that is only divisible two distinct numbers: 1 and itself.
//
// For example, 7 is a prime because it is only divisible by 1 and 7. For example, 
// 6 is not a prime because it is divisible by 1, 2, 3, and 6.
//
// You can assume that the input number is a positive integer.
//
// test_00:
// isPrime(2); // -> true
//
// test_01:
// isPrime(3); // -> true
//
// test_02:
// isPrime(4); // -> false
//
// test_03:
// isPrime(5); // -> true
//
// test_04:
// isPrime(6); // -> false
//
// test_05:
// isPrime(7); // -> true
//
// test_06:
// isPrime(8); // -> false
//
// test_07:
// isPrime(25); // -> false
//
// test_08:
// isPrime(31); // -> true
//
// test_09:
// isPrime(2017); // -> true
//
// test_10:
// isPrime(2048); // -> false
//
// test_11:
// isPrime(1); // -> false

const isPrime = (n) => {
  if (n < 2) return false;
  
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  
  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #3 uncompress ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, uncompress, that takes in a string as an argument. The input 
// string will be formatted into multiple groups according to the following pattern:
//
// <number><char>
//
// for example, '2c' or '3a'.
// The function should return an uncompressed version of the string where each 
// 'char' of a group is repeated 'number' times concecutively. You may assume that 
// the input string is well-formed according to the previously mentioned pattern.
//
// test_00:
// uncompress("2c3a1t"); // -> 'ccaaat'
//
// test_01:
// uncompress("4s2b"); // -> 'ssssbb'
//
// test_02:
// uncompress("2p1o5p"); // -> 'ppoppppp'
//
// test_03:
// uncompress("3n12e2z"); // -> 'nnneeeeeeeeeeeezz'

const uncompress = (s) => {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  let result = "";
  let numStr = "";

  for (let i = 0; i < s.length; i++) {
    if (!alphabet.includes(s[i])) {
      numStr += s[i];
    } else {
      for (let j = 0; j < parseInt(numStr); j++) {
        result += s[i];
      }
      numStr = "";
    }
  }

  return result;
};

// ========================= Solution =========================
// using two pointers
// const uncompress = (s) => {
//   let result = [];
//   const numbers = '0123456789';
//   let i = 0;
//   let j = 0;
//   while (j < s.length) {
//     if (numbers.includes(s[j])) {
//       j += 1;
//     } else {
//       const num = Number(s.slice(i, j));
//       for (let count = 0; count < num; count += 1) {
//         result.push(s[j]);
//       }
//       j += 1;
//       i = j;
//     }
//   }
//   return result.join('');
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #4 compress ]]]]]]]]]]]]]]]]]]]]]]]]]
//
// Write a function, compress, that takes in a string as an argument. The function 
// should return a compressed version of the string where consecutive occurences
// of the same characters are compressed into the number of occurences followed 
// by the character. Single character occurences should not be changed.
//
// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'
// You can assume that the input only contains alphabetic characters.
//
// test_00:
// compress('ccaaatsss'); // -> '2c3at3s'
//
// test_01:
// compress('ssssbbz'); // -> '4s2bz'
//
// test_02:
// compress('ppoppppp'); // -> '2po5p'
//
// test_03:
// compress('nnneeeeeeeeeeeezz'); // -> '3n12e2z'

const compress = (s) => {
  let i = 0;
  let j = 1;
  let result = "";

  while (j <= s.length) {
    if (s[j] !== s[i]) {
      if (j - i === 1) {
        result += s[i];
      } else {
        result += (j - i) + s[i];
      }
      i = j;
    }
    j++;
  }

  return result;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #5 anagrams ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, anagrams, that takes in two strings as arguments. The function
// should return a boolean indicating whether or not the strings are anagrams. 
// Anagrams are strings that contain the same characters, but in any order.
//
// test_00:
// anagrams('restful', 'fluster'); // -> true
//
// test_01:
// anagrams('cats', 'tocs'); // -> false
//
// test_02:
// anagrams('monkeyswrite', 'newyorktimes'); // -> true
//
// test_03:
// anagrams('paper', 'reapa'); // -> false
//
// test_04:
// anagrams('elbow', 'below'); // -> true
//
// test_05:
// anagrams('tax', 'taxi'); // -> false

const anagrams = (s1, s2) => {
  const count = {};

  for (let char of s1) {
    if (count[char]) {
      count[char] += 1;
    } else {
      count[char] = 1;
    }
  }

  for (let char of s2) {
    if (count[char]) {
      count[char] -= 1;
    } else {
      return false
    }
  }

  for (let char in count) {
    if (count[char] !== 0) return false;
  }

  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #6 most frequent char ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, mostFrequentChar, that takes in a string as an argument. The
// function should return the most frequent character of the string. If there are 
// ties, return the character that appears earlier in the string.
//
// You can assume that the input string is non-empty.
//
// test_00:
// mostFrequentChar('bookeeper'); // -> 'e'
//
// test_01:
// mostFrequentChar('david'); // -> 'd'
//
// test_02:
// mostFrequentChar('abby'); // -> 'b'
//
// test_03:
// mostFrequentChar('mississippi'); // -> 'i'
//
// test_04:
// mostFrequentChar('potato'); // -> 'o'
//
// test_05:
// mostFrequentChar('eleventennine'); // -> 'e'

const mostFrequentChar = (s) => {
  const count = {};
  let result = "";

  for (let char of s) {
    if (count[char]) {
      count[char] += 1;
    } else {
      count[char] = 1;
    }
  }

  for (let char in count) {
    if (!result.length || count[char] > count[result]) {
      result = char;
    }
  }

  return result;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #7 pair sum ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, pairSum, that takes in an array and a target sum as 
// arguments. The function should return an array containing a pair of indices 
// whose elements sum to the given target. The indices returned must be unique.
//
// Be sure to return the indices, not the elements themselves.
//
// There is guaranteed to be one such pair that sums to the target.
//
// test_00:
// pairSum([3, 2, 5, 4, 1], 8); // -> [0, 2]
//
// test_01:
// pairSum([4, 7, 9, 2, 5, 1], 5); // -> [0, 5]
//
// test_02:
// pairSum([4, 7, 9, 2, 5, 1], 3); // -> [3, 5]
//
// test_03:
// pairSum([1, 6, 7, 2], 13); // -> [1, 2]
//
// test_04:
// pairSum([9, 9], 18); // -> [0, 1]
//
// test_05:
// pairSum([6, 4, 2, 8 ], 12); // -> [1, 3]

const pairSum = (numbers, targetSum) => {
  const differences = {};

  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    const diff = targetSum - num;
    if (diff in differences) {
      return [differences[diff], i];
    }
    differences[num] = i;
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #8 pair product ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, pairProduct, that takes in an array and a target product as
// arguments. The function should return an array containing a pair of indices 
// whose elements multiply to the given target. The indices returned must be unique.
//
// Be sure to return the indices, not the elements themselves.
//
// There is guaranteed to be one such pair whose product is the target.
//
// test_00:
// pairProduct([3, 2, 5, 4, 1], 8); // -> [1, 3]
//
// test_01:
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
//
// test_02:
// pairProduct([4, 7, 9, 2, 5, 1], 5); // -> [4, 5]
//
// test_03:
// pairProduct([4, 7, 9, 2, 5, 1], 35); // -> [1, 4]
//
// test_04:
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
//
// test_05:
// pairProduct([4, 6, 8, 2], 16); // -> [2, 3]

const pairProduct = (numbers, targetProduct) => {
  const quotients = {};
  
  for (let i = 0; i < numbers.length; i++) {
    let num = numbers[i];
    let quot = targetProduct / num;
    if (quotients[quot]) {
      return [quotients[quot], i];
    }
    quotients[num] = i;
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #9 intersection ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, intersection, that takes in two arrays, a,b, as arguments. 
// The function should return a new array containing elements that are in both of 
// the two arrays.
//
// You may assume that each input array does not contain duplicate elements.
//
// test_00:
// intersection([4,2,1,6], [3,6,9,2,10]) // -> [2,6]
//
// test_01:
// intersection([2,4,6], [4,2]) // -> [2,4]
//
// test_02:
// intersection([4,2,1], [1,2,4,6]) // -> [1,2,4]
//
// test_03:
// intersection([0,1,2], [10,11]) // -> []
//
// test_04:
// const a = [];
// const b = [];
// for (let i = 0; i < 50000; i += 1) {
//   a.push(i);
//   b.push(i);
// }
// intersection(a, b) // -> [0,1,2,3,..., 49999]

const intersection = (a, b) => {
  const result = [];
  const setA = new Set(a);

  for (let num of b) {
    if (setA.has(num)) {
      result.push(num);
    }
  }

  return result;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #10 fivesort ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, fiveSort, that takes in an array of numbers as an argument.
// The function should rearrange elements of the array such that all 5s appear at 
// the end. Your function should perform this operation in-place by mutating the 
// original array. The function should return the array.
//
// Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.
//
//
// test_00
// fiveSort([12, 5, 1, 5, 12, 7]);
// -> [12, 7, 1, 12, 5, 5] 
//
// test_01
// fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
//
// test_02
// fiveSort([5, 5, 5, 1, 1, 1, 4]);
// -> [4, 1, 1, 1, 5, 5, 5] 
//
// test_03
// fiveSort([5, 5, 6, 5, 5, 5, 5]);
// -> [6, 5, 5, 5, 5, 5, 5] 
//
// test_04
// fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
// -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

const fiveSort = (nums) => {
  let i = 0;
  let j = nums.length - 1;

  while (i <= j) {
    if (nums[i] === 5 && nums[j] !== 5) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
      j--;
    } else if (nums[j] === 5) {
      j--;
    } else {
      i++;
    }
  }

  return nums;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #11 linked list values ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, linkedListValues, that takes in the head of a linked list 
// as an argument. The function should return an array containing all values of 
// the nodes in the linked list.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// linkedListValues(a); // -> [ 'a', 'b', 'c', 'd' ]
//
// test_01:
// const x = new Node("x");
// const y = new Node("y");
//
// x.next = y;
//
// x -> y
//
// linkedListValues(x); // -> [ 'x', 'y' ]
//
// test_02:
// const q = new Node("q");
//
// q
//
// linkedListValues(q); // -> [ 'q' ]
//
// test_03:
// linkedListValues(null); // -> [ ]

const linkedListValues = (head) => {
  const result = [];
  let currNode = head;

  while (currNode) {
    result.push(currNode.val);
    currNode = currNode.next;
  }

  return result;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #12 sum list ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, sumList, that takes in the head of a linked list containing 
// numbers as an argument. The function should return the total sum of all values 
// in the linked list.
//
// test_00:
// const a = new Node(2);
// const b = new Node(8);
// const c = new Node(3);
// const d = new Node(-1);
// const e = new Node(7);
//
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
//
// 2 -> 8 -> 3 -> -1 -> 7
//
// sumList(a); // 19
//
// test_01:
// const x = new Node(38);
// const y = new Node(4);
//
// x.next = y;
//
// 38 -> 4
//
// sumList(x); // 42
//
// test_02:
// const z = new Node(100);
//
// 100
//
// sumList(z); // 100
//
// test_03:
// sumList(null); // 0

const sumList = (head) => {
  let sum = 0;
  let currNode = head;

  while (currNode) {
    sum += currNode.val;
    currNode = currNode.next;
  }

  return sum;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #13 linked list find ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, linkedListFind, that takes in the head of a linked list and
// a target value. The function should return a boolean indicating whether or not
// the linked list contains the target.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// linkedListFind(a, "c"); // true
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// linkedListFind(a, "d"); // true
//
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// linkedListFind(a, "q"); // false
//
// test_03:
// const node1 = new Node("jason");
// const node2 = new Node("leneli");
//
// node1.next = node2;
//
// jason -> leneli
//
// linkedListFind(node1, "jason"); // true
//
// test_04:
// const node1 = new Node(42);
//
// 42
//
// linkedListFind(node1, 42); // true
//
// test_05:
// const node1 = new Node(42);
//
// 42
//
// linkedListFind(node1, 100); // false

const linkedListFind = (head, target) => {
  if (head === null) return false;
  if (head.val === target) return true;

  return linkedListFind(head.next, target);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #14 get node value ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, getNodeValue, that takes in the head of a linked list and 
// an index. The function should return the value of the linked list at the 
// specified index.
//
// If there is no node at the given index, then return null.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// getNodeValue(a, 2); // 'c'
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// getNodeValue(a, 3); // 'd'
//
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// getNodeValue(a, 7); // null
//
// test_03:
// const node1 = new Node("banana");
// const node2 = new Node("mango");
//
// node1.next = node2;
//
// banana -> mango
//
// getNodeValue(node1, 0); // 'banana'
//
// test_04:
// const node1 = new Node("banana");
// const node2 = new Node("mango");
//
// node1.next = node2;
//
// banana -> mango
//
// getNodeValue(node1, 1); // 'mango'

// ========================= Iterative =========================
const getNodeValue = (head, index) => { // Time: O(n), Space: O(1)
  let nodeIdx = 0;
  let currNode = head;

  while (currNode !== null) {
    if (nodeIdx === index) return currNode.val;
    currNode = currNode.next;
    nodeIdx++;
  }

  return null;
};

// ========================= Recursive =========================
const getNodeValue = (head, index) => { // Time: O(n), Space: O(n)
  if (index === 0) return head.val;
  if (head === null) return null;

  return getNodeValue(head.next, index - 1);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #15 reverse list ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, reverseList, that takes in the head of a linked list as an 
// argument. The function should reverse the order of the nodes in the linked 
// list in-place and return the new head of the reversed linked list.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
//
// a -> b -> c -> d -> e -> f
//
// reverseList(a); // f -> e -> d -> c -> b -> a
//
// test_01:
// const x = new Node("x");
// const y = new Node("y");
//
// x.next = y;
//
// x -> y
//
// reverseList(x); // y -> x
//
// test_02:
// const p = new Node("p");
//
// p
//
// reverseList(p); // p

// ========================= Iterative =========================
const reverseList = (head) => { // Time: O(n), Space: O(1)
  let currNode = head;
  let prevNode = null;

  while (currNode !== null) {
    const nextNode = currNode.next;
    currNode.next = prevNode;
    prevNode = currNode;
    currNode = nextNode;
  }

  return prevNode;
};

// ========================= Recursive =========================
const reverseList = (head, prev = null) => { // Time: O(n), Space: O(n)
  if (head === null) return prev;
  
  const nextNode = head.next;
  head.next = prev;
  return reverseList(nextNode, head);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #16 zipper list ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, zipperLists, that takes in the head of two linked lists as 
// arguments. The function should zipper the two lists together into single linked 
// list by alternating nodes. If one of the linked lists is longer than the other, 
// the resulting list should terminate with the remaining nodes. The function 
// should return the head of the zippered linked list.
//
// Do this in-place, by mutating the original Nodes.
//
// You may assume that both input lists are non-empty.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// a.next = b;
// b.next = c;
// a -> b -> c
//
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// x -> y -> z
//
// zipperLists(a, x);
// a -> x -> b -> y -> c -> z
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// a -> b -> c -> d -> e -> f
//
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// x -> y -> z
//
// zipperLists(a, x);
// a -> x -> b -> y -> c -> z -> d -> e -> f
//
// test_02:
// const s = new Node("s");
// const t = new Node("t");
// s.next = t;
// s -> t
//
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// const four = new Node(4);
// one.next = two;
// two.next = three;
// three.next = four;
// 1 -> 2 -> 3 -> 4
//
// zipperLists(s, one);
// s -> 1 -> t -> 2 -> 3 -> 4
//
// test_03:
// const w = new Node("w");
//
// w
//
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// 1 -> 2 -> 3 
// 
// zipperLists(w, one);
// w -> 1 -> 2 -> 3
//
// test_04:
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// 1 -> 2 -> 3 
//
// const w = new Node("w");
// w
//
// zipperLists(one, w);
// 1 -> w -> 2 -> 3

// ========================= Iterative =========================
const zipperLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(1)
  let tail = head1;
  let current1 = head1.next;
  let current2 = head2;
  let count = 0;

  while (current1 !== null && current2 !== null) {
    if (count % 2 === 0) {
      tail.next = current2;
      current2 = current2.next;
    } else {
      tail.next = current1;
      current1 = current1.next;
    }
    tail = tail.next;
    count++;
  }

  if (current1 === null) tail.next = current2;
  if (current2 === null) tail.next = current1;

  return head1;
};

// ========================= Recursive =========================
const zipperLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(min(n, m))
  if (head1 === null && head2 === null) return null;
  if (head1 === null) return head2;
  if (head2 === null) return head1;

  const next1 = head1.next;
  const next2 = head2.next;
  head1.next = head2;
  head2.next = zipperLists(next1, next2);
  return head1;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #17 merge lists ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, mergeLists, that takes in the head of two sorted linked 
// lists as arguments. The function should merge the two lists together into single 
// sorted linked list. The function should return the head of the merged linked list.
//
// Do this in-place, by mutating the original Nodes.
//
// You may assume that both input lists are non-empty and contain increasing sorted numbers.
//
// test_00:
// const a = new Node(5);
// const b = new Node(7);
// const c = new Node(10);
// const d = new Node(12);
// const e = new Node(20);
// const f = new Node(28);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 5 -> 7 -> 10 -> 12 -> 20 -> 28
//
// const q = new Node(6);
// const r = new Node(8);
// const s = new Node(9);
// const t = new Node(25);
// q.next = r;
// r.next = s;
// s.next = t;
// 6 -> 8 -> 9 -> 25
//
// mergeLists(a, q);
// 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
//
// test_01:
// const a = new Node(5);
// const b = new Node(7);
// const c = new Node(10);
// const d = new Node(12);
// const e = new Node(20);
// const f = new Node(28);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 5 -> 7 -> 10 -> 12 -> 20 -> 28
//
// const q = new Node(1);
// const r = new Node(8);
// const s = new Node(9);
// const t = new Node(10);
// q.next = r;
// r.next = s;
// s.next = t;
// 1 -> 8 -> 9 -> 10
//
// mergeLists(a, q);
// 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 
//
// test_02:
// const h = new Node(30);
// 30
//
// const p = new Node(15);
// const q = new Node(67);
// p.next = q;
// 15 -> 67
//
// mergeLists(h, p);
// 15 -> 30 -> 67

// ========================= Iterative =========================
const mergeLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(1)
  const dummyHead = new Node(null);
  let tail = dummyHead;
  let current1 = head1;
  let current2 = head2;

  while (current1 !== null && current2 !== null) {
    if (current1.val < current2.val) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }

    tail = tail.next;
  }

  if (current1 === null) tail.next = current2;
  if (current2 === null) tail.next = current1;

  return dummyHead.next;
};

// ========================= Recursive =========================
const mergeLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(min(n, m))
  if (head1 === null && head2 === null) return null;
  if (head1 === null) return head2;
  if (head2 === null) return head1;

  if (head1.val < head2.val) {
    const next1 = head1.next;
    head1.next = mergeLists(next1, head2);
    return head1;
  } else {
    const next2 = head2.next;
    head2.next = mergeLists(next2, head1);
    return head2;
  } 
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #18 is univalue list ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, isUnivalueList, that takes in the head of a linked list as 
// an argument. The function should return a boolean indicating whether or not the 
// linked list contains exactly one unique value.
//
// You may assume that the input list is non-empty.
//
// test_00:
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(7);
//
// a.next = b;
// b.next = c;
//
// 7 -> 7 -> 7
//
// isUnivalueList(a); // true
//
// test_01:
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(4);
//
// a.next = b;
// b.next = c;
//
// 7 -> 7 -> 4
//
// isUnivalueList(a); // false
//
// test_02:
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(2);
// const x = new Node(2);
// const y = new Node(2);
//
// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;
//
// 2 -> 2 -> 2 -> 2 -> 2
//
// isUnivalueList(u); // true
//
// test_03:
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(3);
// const x = new Node(3);
// const y = new Node(2);
//
// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;
//
// 2 -> 2 -> 3 -> 3 -> 2
//
// isUnivalueList(u); // false
//
// test_04:
// const z = new Node('z');
//
// z
//
// isUnivalueList(z); // true

// ========================= Iterative =========================
const isUnivalueList = (head) => { // Time: O(n), Space: O(1)
  const value = head.val;
  let currNode = head;

  while (currNode !== null) {
    if (currNode.val !== value) return false;
    currNode = currNode.next;
  }

  return true;
};

// ========================= Recursive =========================
const isUnivalueList = (head, prev = head) => { // Time: O(n), Space: O(n)
  if (head === null) return true;

  if (head.val === prev.val) {
    return isUnivalueList(head.next, head);
  } else {
    return false;
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #19 longest streak ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, longestStreak, that takes in the head of a linked list as 
// an argument. The function should return the length of the longest consecutive 
// streak of the same value within the list.
// 
// test_00:
// const a = new Node(5);
// const b = new Node(5);
// const c = new Node(7);
// const d = new Node(7);
// const e = new Node(7);
// const f = new Node(6);
// 
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 
// 5 -> 5 -> 7 -> 7 -> 7 -> 6
// 
// longestStreak(a); // 3
//
// test_01:
// const a = new Node(3);
// const b = new Node(3);
// const c = new Node(3);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(9);
//
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
//
// 3 -> 3 -> 3 -> 3 -> 9 -> 9
//
// longestStreak(a); // 4
//
// test_02:
// const a = new Node(9);
// const b = new Node(9);
// const c = new Node(1);
// const d = new Node(9);
// const e = new Node(9);
// const f = new Node(9);
//
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
//
// 9 -> 9 -> 1 -> 9 -> 9 -> 9
//
// longestStreak(a); // 3
//
// test_03:
// const a = new Node(5);
// const b = new Node(5);
//
// a.next = b;
//
// 5 -> 5
//
// longestStreak(a); // 2
//
// test_04:
// const a = new Node(4);
//
// 4
//
// longestStreak(a); // 1
//
// test_05:
// longestStreak(null); // 0

const longestStreak = (head) => { // Time: O(n), Space: O(1)
  let greatestStreak = 0;
  let currentStreak = 0;
  let currNode = head;
  let prevNode = head;
  
  while (currNode !== null) {
    if (currNode.val === prevNode.val) {
      currentStreak++;
    } else {
      currentStreak = 1;
    }
    if (currentStreak > greatestStreak) {
      greatestStreak = currentStreak;
    }
    prevNode = currNode;
    currNode = currNode.next;
  } 
  
  return greatestStreak;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #20 remove node ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, removeNode, that takes in the head of a linked list and a 
// target value as arguments. The function should delete the node containing the 
// target value from the linked list and return the head of the resulting linked 
// list. If the target appears multiple times in the linked list, only remove the 
// first instance of the target in the list.
//
// Do this in-place.
//
// You may assume that the input list is non-empty.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
//
// a -> b -> c -> d -> e -> f
//
// removeNode(a, "c");
// a -> b -> d -> e -> f
//
// test_01:
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
//
// x.next = y;
// y.next = z;
//
// x -> y -> z
//
// removeNode(x, "z");
// x -> y
//
// test_02:
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");
//
// q.next = r;
// r.next = s;
//
// q -> r -> s
//
// removeNode(q, "q");
// r -> s
//
// test_03:
// const node1 = new Node("h");
// const node2 = new Node("i");
// const node3 = new Node("j");
// const node4 = new Node("i");
//
// node1.next = node2;
// node2.next = node3;
// node3.next = node4;
//
// h -> i -> j -> i
//
// removeNode(node1, "i");
// h -> j -> i
//
// test_04:
// const t = new Node("t");
//
// t
//
// removeNode(t, "t");
// null

// ========================= Iterative =========================
const removeNode = (head, targetVal) => { // Time: O(n), Space: O(1)
  let currNode = head;
  let prevNode = new Node(null);
  let dummyHead = prevNode;
  prevNode.next = head;

  while (currNode !== null) {
    if (currNode.val === targetVal) {
      prevNode.next = currNode.next;
      break;
    }
    prevNode = currNode;
    currNode = currNode.next;
  }

  return dummyHead.next;
};

// ========================= Recursive =========================
const removeNode = (head, targetVal) => { // Time: O(n), Space: O(n)
  if (head === null) return null;
  if (head.val === targetVal) return head.next;

  head.next = removeNode(head.next, targetVal);
  return head;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #21 insert node ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, insertNode, that takes in the head of a linked list, a 
// value, and an index. The function should insert a new node with the value into 
// the list at the specified index. Consider the head of the linked list as index 
// 0. The function should return the head of the resulting linked list.
//
// Do this in-place.
//
// You may assume that the input list is non-empty and the index is not greater 
// than the length of the input list.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// insertNode(a, 'x', 2);
// a -> b -> x -> c -> d
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// insertNode(a, 'v', 3);
// a -> b -> c -> v -> d
//
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
//
// a.next = b;
// b.next = c;
// c.next = d;
//
// a -> b -> c -> d
//
// insertNode(a, 'm', 4);
// a -> b -> c -> d -> m
//
// test_03:
// const a = new Node("a");
// const b = new Node("b");
//
// a.next = b;
//
// a -> b
//
// insertNode(a, 'z', 0);
// z -> a -> b 

// ========================= Iterative =========================
const insertNode = (head, value, index) => { // Time: O(n), Space: O(1)
  let count = 0;
  let currNode = new Node(null);
  let dummyHead = currNode;
  dummyHead.next = head;

  while (count <= index) {
    if (count === index) {
      const nextNode = currNode.next;
      currNode.next = new Node(value);
      currNode.next.next = nextNode;
    }
    currNode = currNode.next;
    count++;
  }

  return dummyHead.next;
};

// ========================= Recursive =========================
const insertNode = (head, value, index, count = 0) => { // Time: O(n), Space: O(n)
  if (index === 0) {
    const newNode = new Node(value);
    newNode.next = head;
    return newNode;
  }

  if (count === index - 1) {
    const nextNode = head.next;
    head.next = new Node(value);
    head.next.next = nextNode;
    return head;
  }

  insertNode(head.next, value, index, count + 1);
  return head;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #22 create linked list ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, createLinkedList, that takes in an array of values as an 
// argument. The function should create a linked list containing each element of 
// the array as the values of the nodes. The function should return the head of 
// the linked list.
//
// test_00:
// createLinkedList(["h", "e", "y"]);
// h -> e -> y
//
// test_01:
// createLinkedList([1, 7, 1, 8]);
// 1 -> 7 -> 1 -> 8
//
// test_02:
// createLinkedList(["a"]);
// a
//
// test_03:
// createLinkedList([]);
// null

// ========================= Iterative =========================
const createLinkedList = (values) => {
  const dummyHead = new Node(null);
  let tail = dummyHead;
  
  for (let val of values) {
    tail.next = new Node(val);
    tail = tail.next;
  }
  
  return dummyHead.next;
};

// ========================= Recursive =========================
const createLinkedList = (values, i = 0) => {
  if (i === values.length) return null;
  const newNode = new Node(values[i]);
  newNode.next = createLinkedList(values, i + 1);
  return newNode;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #23 add lists ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, addLists, that takes in the head of two linked lists, each 
// representing a number. The nodes of the linked lists contain digits as values. 
// The nodes in the input lists are reversed; this means that the least significant 
// digit of the number is the head. The function should return the head of a new 
// linked listed representing the sum of the input lists. The output list should 
// have it's digits reversed as well.
//
// Say we wanted to compute 621 + 354 normally. The sum is 975:
//
//    621
//  + 354
//  -----
//    975
//
// Then, the reversed linked list format of this problem would appear as:
//
//     1 -> 2 -> 6
//  +  4 -> 5 -> 3
//  --------------
//     5 -> 7 -> 9
//
// test_00:
//   621
// + 354
// -----
//   975
//
// const a1 = new Node(1);
// const a2 = new Node(2);
// const a3 = new Node(6);
// a1.next = a2;
// a2.next = a3;
// 1 -> 2 -> 6
//
// const b1 = new Node(4);
// const b2 = new Node(5);
// const b3 = new Node(3);
// b1.next = b2;
// b2.next = b3;
// 4 -> 5 -> 3
//
// addLists(a1, b1);
// 5 -> 7 -> 9
//
// test_01:
//  7541
// +  32
// -----
//  7573
//
// const a1 = new Node(1);
// const a2 = new Node(4);
// const a3 = new Node(5);
// const a4 = new Node(7);
// a1.next = a2;
// a2.next = a3;
// a3.next = a4;
// 1 -> 4 -> 5 -> 7
//
// const b1 = new Node(2);
// const b2 = new Node(3);
// b1.next = b2;
// 2 -> 3 
//
// addLists(a1, b1);
// 3 -> 7 -> 5 -> 7
//
// test_02:
//   39
// + 47
// ----
//   86
//
// const a1 = new Node(9);
// const a2 = new Node(3);
// a1.next = a2;
// 9 -> 3
//
// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// 7 -> 4
//
// addLists(a1, b1);
// 6 -> 8
//
// test_03:
//   89
// + 47
// ----
//  136
//
// const a1 = new Node(9);
// const a2 = new Node(8);
// a1.next = a2;
// 9 -> 8
//
// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// 7 -> 4
//
// addLists(a1, b1);
// 6 -> 3 -> 1
//
// test_04:
//   999
//  +  6
//  ----
//  1005
//
// const a1 = new Node(9);
// const a2 = new Node(9);
// const a3 = new Node(9);
// a1.next = a2;
// a2.next = a3;
// 9 -> 9 -> 9
//
// const b1 = new Node(6);
// 6
//
// addLists(a1, b1);
// 5 -> 0 -> 0 -> 1

// ========================= Iterative =========================
const addLists = (head1, head2) => { // Time: O(max(n, m)), Space: O(max(n, m))
  const sumHead = new Node(null);
  let currNode = sumHead;
  let curr1 = head1;
  let curr2 = head2;
  let carry = 0;

  while (curr1 !== null || curr2 !== null || carry !== 0) {
    let val1 = curr1 === null ? 0 : curr1.val;
    let val2 = curr2 === null ? 0 : curr2.val;
    let sum = val1 + val2 + carry;
    let num = sum % 10;
  
    carry = (sum > 9) ? 1 : 0;

    currNode.next = new Node(num);
    currNode = currNode.next;
    if (curr1 !== null) curr1 = curr1.next;
    if (curr2 !== null) curr2 = curr2.next;
  }

  return sumHead.next;
};

// ========================= Recursive =========================
const addLists = (head1, head2, carry = 0) => { // Time: O(max(n, m)), Space: O(max(n, m))
  if (head1 === null && head2 === null && carry === 0) return null;

  let val1 = head1 === null ? 0 : head1.val;
  let val2 = head2 === null ? 0 : head2.val;
  let sum = val1 + val2 + carry;
  carry = sum > 9 ? 1 : 0;
  
  let num = sum % 10;
  const head = new Node(num);
  const curr1 = head1 === null ? null : head1.next;
  const curr2 = head2 === null ? null : head2.next;
  head.next = addLists(curr1, curr2, carry);

  return head;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #24 depth first values ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, depthFirstValues, that takes in the root of a binary tree. 
// The function should return an array containing all values of the tree in 
// depth-first order.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// depthFirstValues(a); 
//    -> ['a', 'b', 'd', 'e', 'c', 'f']
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g
//
// depthFirstValues(a); 
//    -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
// test_02:
// const a = new Node('a');
//      a
// depthFirstValues(a); 
//    -> ['a']
// test_03:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
//
// a.right = b;
// b.left = c;
// c.right = d;
// d.right = e;
//
//      a
//       \
//        b
//       /
//      c
//       \
//        d
//         \
//          e
//
// depthFirstValues(a); 
//    -> ['a', 'b', 'c', 'd', 'e']
// test_04:
// howHigh(null); 
//    -> []


// ========================= Iterative =========================
const depthFirstValues = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return [];

  const values = [];
  const stack = [root];

  while (stack.length > 0) {
    const node = stack.pop();
    values.push(node.val);

    if (node.right !== null) stack.push(node.right);
    if (node.left !== null) stack.push(node.left);
  }

  return values;
};

// ========================= Recursive =========================
const depthFirstValues = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return [];

  return [root.val].concat(depthFirstValues(root.left))
                   .concat(depthFirstValues(root.right));
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #25 breadth first values ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, breadthFirstValues, that takes in the root of a binary tree.
// The function should return an array containing all values of the tree in 
// breadth-first order.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// breadthFirstValues(a); 
//    -> ['a', 'b', 'c', 'd', 'e', 'f']
//
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// breadthFirstValues(a); 
//   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
//
// test_02:
// const a = new Node('a');
//
//      a
//
// breadthFirstValues(a); 
//    -> ['a']
//
// test_03:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const x = new Node('x');
//
// a.right = b;
// b.left = c;
// c.left = x;
// c.right = d;
// d.right = e;
//
//      a
//       \
//        b
//       /
//      c
//    /  \
//   x    d
//         \
//          e
//
// breadthFirstValues(a); 
//    -> ['a', 'b', 'c', 'x', 'd', 'e']
//
// test_04:
// howHigh(null); 
//    -> []

// ========================= Iterative =========================
const breadthFirstValues = (root) => { // Time: O(n^2), Space: O(n)
  if (root === null) return [];
  
  const queue = [root];
  const values = [];
  
  while (queue.length > 0) {
    const node = queue.shift();
    values.push(node.val);
    
    if (node.left !== null) queue.push(node.left);
    if (node.right !== null) queue.push(node.right);
  }
  
  return values;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #26 tree includes ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, treeIncludes, that takes in the root of a binary tree and 
// a target value. The function should return a boolean indicating whether or 
// not the value is contained in the tree.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// treeIncludes(a, "e"); // -> true
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// treeIncludes(a, "a"); // -> true
//
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// treeIncludes(a, "n"); // -> false
//
// test_03:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// treeIncludes(a, "f"); // -> true
//
// test_04:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// treeIncludes(a, "p"); // -> false
//
// test_05:
// treeIncludes(null, "b"); // -> false

// ========================= Breadth First =========================
const treeIncludes = (root, target) => { // Time: O(n^2), Space: O(n)
  if (root === null) return false;

  const queue = [root];
  while (queue.length > 0) {
    const node = queue.shift();

    if (node.val === target) return true;
    if (node.left !== null) queue.push(node.left);
    if (node.right !== null) queue.push(node.right);
  }

  return false;
};

// ========================= Depth First =========================
const treeIncludes = (root, target) => { // Time: O(n), Space: O(n)
  if (root === null) return false;
  if (root.val === target) return true;
  return treeIncludes(root.left. target) || treeIncludes(root.right. target);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #27 tree sum ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, treeSum, that takes in the root of a binary tree that 
// contains number values. The function should return the total sum of all values
// in the tree.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
//
// treeSum(a); // -> 21
//
// test_01:
// const a = new Node(1);
// const b = new Node(6);
// const c = new Node(0);
// const d = new Node(3);
// const e = new Node(-6);
// const f = new Node(2);
// const g = new Node(2);
// const h = new Node(2);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      1
//    /   \
//   6     0
//  / \     \
// 3   -6    2
//    /       \
//   2         2
//
// treeSum(a); // -> 10
//
// test_02:
// treeSum(null); // -> 0

// ========================= Depth First =========================
const treeSum = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return 0;

  return root.val + treeSum(root.left) + treeSum(root.right);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #28 tree min value ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, treeMinValue, that takes in the root of a binary tree that 
// contains number values. The function should return the minimum value within 
// the tree.
//
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
//
// treeMinValue(a); // -> -2
//
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(3);
// const d = new Node(4);
// const e = new Node(14);
// const f = new Node(12);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//       5
//    /    \
//   11     3
//  / \      \
// 4   15     12
//
// treeMinValue(a); // -> 3
//
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(-2);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     /       \
//    -2       -2
//
// tree_min_value(a); // -> -13
//
// test_03:
// const a = new Node(42);
//
//        42
//
// tree_min_value(a); // -> 42

// ========================= Depth First Recursive =========================
const treeMinValue = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return Infinity;

  const minLeft = treeMinValue(root.left);
  const minRight = treeMinValue(root.right);

  return Math.min(root.val, minLeft, minRight);
};

// ========================= Depth First Iterative =========================
const treeMinValue = (root) => { // Time: O(n), Space: O(n)
  let minValue = Infinity;
  const stack = [root];

  while (stack.length) {
    const node = stack.pop();

    if (node.val < minValue) minValue = node.val;
    if (node.left !== null) stack.push(node.left);
    if (node.right !== null) stack.push(node.right);
  }

  return minValue;
};

// ========================= Breadth First =========================
const treeMinValue = (root) => { // Time: O(n^2), Space: O(n)
  let minValue = Infinity;
  const queue = [root];

  while (queue.length > 0) {
    const node = queue.shift();

    if (node.val < minValue) minValue = node.val;
    if (node.left !== null) queue.push(node.left);
    if (node.right !== null) queue.push(node.right);
  }

  return minValue;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #29 max path sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, maxPathSum, that takes in the root of a binary tree that 
// contains number values. The function should return the maximum sum of any root
// to leaf path within the tree.
//
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      3
//    /   \
//   11    4
//  / \     \
// 4   -2    1
//
// maxPathSum(a); // -> 18
//
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//
//       5
//     /   \
//    11   54
//  /   \
// 20   15
//      / \
//     1  3
//
// maxPathSum(a); // -> 59
//
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(-13);
// const g = new Node(-1);
// const h = new Node(-2);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0    -13
//     /       \
//    -1       -2
//
// maxPathSum(a); // -> -8
//
// test_03:
// const a = new Node(42);
//
//        42
//
// maxPathSum(a); // -> 42

// ========================= Depth First =========================
const maxPathSum = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return -Infinity;
  if (root.left === null && root.right === null) return root.val;

  return root.val + Math.max(maxPathSum(root.left), maxPathSum(root.right));
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #30 path finder ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, pathFinder, that takes in the root of a binary tree and a 
// target value. The function should return an array representing a path to the 
// target value. If the target value is not found in the tree, then return null.
//
// You may assume that the tree contains unique values.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// pathFinder(a, 'e'); // -> [ 'a', 'b', 'e' ]
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// pathFinder(a, 'p'); // -> null
//
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// pathFinder(a, "c"); // -> ['a', 'c']
//
// test_03:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// pathFinder(a, "h"); // -> ['a', 'c', 'f', 'h']
//
// test_04:
// const x = new Node("x");
//
//      x
//
// pathFinder(x, "x"); // -> ['x']
//
// test_05:
// pathFinder(null, "x"); // -> null
//
// test_06:
// const root = new Node(0);
// let curr = root;
// for (let i = 1; i <= 6000; i += 1) {
//   curr.right = new Node(i);
//   curr = curr.right;
// }
//
//      0
//       \
//        1
//         \
//          2
//           \
//            3
//             .
//              .
//               .
//              5999
//                \
//                6000
//
// pathFinder(root, 3451); // -> [0, 1, 2, 3, ..., 3450, 3451]

// ========================= My Solution =========================
const pathFinder = (root, target, cameFrom = {}) => { // Time: O(n^2), Space: O(n)
  if (root === null) return null;
  if (root.val === target) return [root.val];
  cameFrom[root] = null;
  const path = [];

  const queue = [root];
  while (queue.length) {
    const node = queue.shift();
    if (node.val === target) break;

    if (node.left !== null) {
      cameFrom[node.left.val] = node.val;
      if (node.left.val === target) break;
      queue.push(node.left);
    }
    if (node.right !== null) {
      cameFrom[node.right.val] = node.val;
      if (node.right.val === target) break;
      queue.push(node.right);
    }
  }
  
  if (cameFrom[target] === undefined) return null;

  let currNode = cameFrom[target];
  while (currNode !== null) {
    path.unshift(currNode);
    currNode = cameFrom[currNode];
  }

  return [...path, target];
};

// ========================= Alvin's Depth First Solution =========================
const pathFinder = (root, target) => { // Time: O(n), Space: O(n)
  const result = pathFinderHelper(root, target);
  if (result === null) {
    return null;
  } else {
    return result.reverse();
  }
};

const pathFinderHelper = (root, target) => {
  if (root === null) return null;
  if (root.val === target) return [ root.val ];
  
  const leftPath = pathFinderHelper(root.left, target);
  if (leftPath !== null) {
    leftPath.push(root.val);
    return leftPath;
  }
  
  const rightPath = pathFinderHelper(root.right, target);
  if (rightPath !== null) {
    rightPath.push(root.val);
    return rightPath;
  }
  
  return null;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #31 tree value count ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, treeValueCount, that takes in the root of a binary tree and
// a target value. The function should return the number of times that the target
// occurs in the tree.
//
// test_00:
// const a = new Node(12);
// const b = new Node(6);
// const c = new Node(6);
// const d = new Node(4);
// const e = new Node(6);
// const f = new Node(12);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//     12
//    /  \
//   6    6
//  / \    \
// 4   6    12
//
// treeValueCount(a,  6); // -> 3
//
// test_01:
// const a = new Node(12);
// const b = new Node(6);
// const c = new Node(6);
// const d = new Node(4);
// const e = new Node(6);
// const f = new Node(12);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//     12
//    /  \
//   6    6
//  / \    \
// 4   6    12
//
// treeValueCount(a,  12); // -> 2
//
// test_02:
// const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1
// treeValueCount(a, 1); // -> 4
//
// test_03:
// const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1
//
// treeValueCount(a, 9); // -> 0
//
// test_04:
// treeValueCount(null, 42); // -> 0

// ========================= Depth First =========================
const treeValueCount = (root, target) => { // Time: O(n), Space: O(n)
  if (root === null) return 0;

  const leftCount = treeValueCount(root.left, target);
  const rightCount = treeValueCount(root.right, target);

  return (root.val === target ? 1 : 0) + leftCount + rightCount;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #32 how high ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, howHigh, that takes in the root of a binary tree. The 
// function should return a number representing the height of the tree.
//
// The height of a binary tree is defined as the maximal number of edges from 
// the root node to any leaf node.
//
// If the tree is empty, return -1.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// howHigh(a); // -> 2
//
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g
//
// howHigh(a); // -> 3
//
// test_02:
// const a = new Node('a');
// const c = new Node('c');
//
// a.right = c;
//
//      a
//       \
//        c
//
// howHigh(a); // -> 1
//
// test_03:
// const a = new Node('a');
//
//      a
//
// howHigh(a); // -> 0

// ========================= Recursive =========================
const howHigh = (root) => { // Time: O(n), Space: O(n)
  if (root === null) return -1;

  const leftHeight = howHigh(root.left);
  const rightHeight = howHigh(root.right);

  return 1 + Math.max(leftHeight, rightHeight);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #33 bottom right value ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, bottomRightValue, that takes in the root of a binary tree. 
// The function should return the right-most value in the bottom-most level of 
// the tree.
//
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(10);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//       3
//    /    \
//   11     10
//  / \      \
// 4   -2     1
//
// bottomRightValue(a); // -> 1
//
// test_01:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(6);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     / \       
//    -2  6
//
// bottomRightValue(a); // -> 6
//
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(6);
// const i = new Node(7);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     / \    /   
//    -2  6  7 
//
// bottomRightValue(a); // -> 7
//
// test_03
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
//
// a.left = b;
// a.right = c;
// b.right = d;
// d.left = e;
// e.right = f;
//
//      a
//    /   \ 
//   b     c
//    \
//     d
//    /
//   e
//  /
// f
//       
// bottomRightValue(a); // -> 'f'
//
// test_04
// const a = new Node(42);
//
//      42
//
// bottomRightValue(a); // -> 42

// ========================= Breadth First =========================
const bottomRightValue = (root) => { // Time: O(n^2), Space: O(n)
  let node;
  const queue = [root];

  while (queue.length) {
    node = queue.shift();

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }

  return node.val;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #34 all tree paths ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, allTreePaths, that takes in the root of a binary tree. The
// function should return a 2-Dimensional array where each subarray represents a
// root-to-leaf path in the tree.
//
// The order within an individual path must start at the root and end at the leaf,
// but the relative order of among paths in the outer array does not matter.
//
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// allTreePaths(a); // ->
// [ 
//   [ 'a', 'b', 'd' ], 
//   [ 'a', 'b', 'e' ], 
//   [ 'a', 'c', 'f' ] 
// ] 
//
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// const i = new Node('i');
//
// a.l//eft = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//
//         a
//      /    \
//     b      c
//   /  \      \
//  d    e      f
//      / \    /   
//     g  h   i 
//
// allTreePaths(a); // ->
// [ 
//   [ 'a', 'b', 'd' ], 
//   [ 'a', 'b', 'e', 'g' ], 
//   [ 'a', 'b', 'e', 'h' ], 
//   [ 'a', 'c', 'f', 'i' ] 
// ] 
//
// test_02:
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// const u = new Node('u');
// const v = new Node('v');
//
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//
//      q
//    /   \ 
//   r     s
//    \
//     t
//    /
//   u
//  /
// v
//
// allTreePaths(q); // ->
// [ 
//   [ 'q', 'r', 't', 'u', 'v' ], 
//   [ 'q', 's' ] 
// ] 
//
// test_03:
// const z = new Node('z');
//
//      z
//
// console.log(allTreePaths(z)); // -> 
// [
//   ['z']
// ]

// ========================= Depth First =========================
const allTreePaths = (root) => { 
  if (root === null) return [];
  if (root.left === null && root.right === null) return [[root.val]];
  
  const paths = [];
  allTreePaths(root.left).forEach(path => {
    paths.push([ root.val, ...path]);
  });
  allTreePaths(root.right).forEach(path => {
    paths.push([ root.val, ...path]);
  });

  return paths;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #35 tree levels ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, treeLevels, that takes in the root of a binary tree. The 
// function should return a 2-Dimensional array where each subarray represents a
// level of the tree.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// treeLevels(a); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f']
// ]
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// const i = new Node("i");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//
//         a
//      /    \
//     b      c
//   /  \      \
//  d    e      f
//      / \    /
//     g  h   i
//
// treeLevels(a); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f'],
//   ['g', 'h', 'i']
// ]
//
// test_02:
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");
// const t = new Node("t");
// const u = new Node("u");
// const v = new Node("v");
//
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//
//      q
//    /   \
//   r     s
//    \
//     t
//    /
//   u
//  /
// v
//
// treeLevels(q); //->
// [
//   ['q'],
//   ['r', 's'],
//   ['t'],
//   ['u'],
//   ['v']
// ]
//
//
// test_03:
// treeLevels(null); // -> []

// ========================= Breadth First =========================
const treeLevels = (root) => { // Time: O(n^2), Space: O(n)
  if (root === null) return [];

  const levelsArr = [];
  const queue = [{ node: root, level: 0 }];
  
  while (queue.length) {
    const { node, level } = queue.shift();

    if (levelsArr[level]) {
      levelsArr[level].push(node.val)
    } else {
      levelsArr[level] = [ node.val ];
    }

    if (node.left) queue.push({ node: node.left, level: level + 1 });
    if (node.right) queue.push({ node: node.right, level: level + 1 });
  }

  return levelsArr;
};

// ========================= Depth First =========================
const treeLevels = (root, levelsArr = [], level = 0) => { // Time: O(n), Space: O(n)
  if (root === null) return [];

  if (levelsArr[level]) {
    levelsArr[level].push(root.val);
  } else {
    levelsArr[level] = [root.val];
  }

  treeLevels(root.left, levelsArr, level + 1);
  treeLevels(root.right, levelsArr, level + 1);
  
  return levelsArr;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #36 level averages ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, levelAverages, that takes in the root of a binary tree that
// contains number values. The function should return an array containing the 
// average value of each level.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
//
// levelAverages(a); // -> [ 3, 7.5, 1 ] 
//
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//
//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3
//
// levelAverages(a); // -> [ 5, 32.5, 17.5, 2 ] 
//
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(45);
// const g = new Node(-1);
// const h = new Node(-2);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0     45
//     /       \
//    -1       -2
//
// levelAverages(a); // -> [ -1, -5.5, 14, -1.5 ]
//
// test_03:
// const q = new Node(13);
// const r = new Node(4);
// const s = new Node(2);
// const t = new Node(9);
// const u = new Node(2);
// const v = new Node(42);
//
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//
//        13
//      /   \
//     4     2
//      \
//       9
//      /
//     2
//    /
//   42
//
// levelAverages(q); // -> [ 13, 3, 9, 2, 42 ]
//
// test_04:
// levelAverages(null); // -> [ ]

// ========================= Breadth First =========================
const levelAverages = (root) => { // Time: O(n^2), Space: O(n)
  if (root === null) return [];

  const levelsArr = [];
  const queue = [{ node: root, level: 0 }];

  while (queue.length) {
    const { node, level } = queue.shift();
    if (levelsArr[level]) {
      levelsArr[level].push(node.val);
    } else {
      levelsArr[level] = [node.val];
    }

    if (node.left) queue.push({ node: node.left, level: level + 1 });
    if (node.right) queue.push({ node: node.right, level: level + 1 });
  }

  return levelsArr.map(level => level.reduce((a, b) => a + b) / level.length);
};

// ========================= Depth First =========================
const levelAverages = (root, levelsArr = [], level = 0) => { // Time: O(n), Space: O(n)
  if (root === null) return [];

  if (levelsArr[level]) {
    levelsArr[level].push(root.val);
  } else {
    levelsArr[level] = [root.val];
  }

  levelAverages(root.left, levelsArr, level + 1);
  levelAverages(root.right, levelsArr, level + 1);

  return levelsArr.map(level => level.reduce((a, b) => a + b) / level.length);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #37 leaf list ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, leafList, that takes in the root of a binary tree and 
// returns an array containing the values of all leaf nodes in left-to-right order.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//
// leafList(a); // -> [ 'd', 'e', 'f' ] 
//
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
//
// leafList(a); // -> [ 'd', 'g', 'h' ]
//
// test_02:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
//
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//
//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3
//
// leafList(a); // -> [ 20, 1, 3, 54 ]
//
// test_03:
// const x = new Node('x');
//
//      x
//
// leafList(x); // -> [ 'x' ]
//
// test_04:
// leafList(null); // -> [ ]

// ========================= Depth First =========================
const leafList = (root, leaves = []) => { // Time: O(n), Space: O(n)
  if (root == null) return [];

  if (root.left == null && root.right == null) leaves.push(root.val);
  if (root.left) leafList(root.left, leaves);
  if (root.right) leafList(root.right, leaves);

  return leaves;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #38 has path ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, hasPath, that takes in an object representing the adjacency
// list of a directed acyclic graph and two nodes (src, dst). The function should
// return a boolean indicating whether or not there exists a directed path between
// the source and destination nodes.
//
// test_00:
// const graph = {
//   f: ['g', 'i'],
//   g: ['h'],
//   h: [],
//   i: ['g', 'k'],
//   j: ['i'],
//   k: []
// };
//
// hasPath(graph, 'f', 'k'); // true
//
// test_01:
// const graph = {
//   f: ['g', 'i'],
//   g: ['h'],
//   h: [],
//   i: ['g', 'k'],
//   j: ['i'],
//   k: []
// };
//
// hasPath(graph, 'f', 'j'); // false
//
// test_02:
// const graph = {
//   f: ['g', 'i'],
//   g: ['h'],
//   h: [],
//   i: ['g', 'k'],
//   j: ['i'],
//   k: []
// };
//
// hasPath(graph, 'i', 'h'); // true
//
// test_03:
// const graph = {
//   v: ['x', 'w'],
//   w: [],
//   x: [],
//   y: ['z'],
//   z: [],  
// };
//
// hasPath(graph, 'v', 'w'); // true
//
// test_04:
// const graph = {
//   v: ['x', 'w'],
//   w: [],
//   x: [],
//   y: ['z'],
//   z: [],  
// };
//
// hasPath(graph, 'v', 'z'); // false

// ========================= Breadth First =========================
const hasPath = (graph, src, dst) => { // Time: O(e^2), Space: O(n)
  const queue = [src];

  while (queue.length) {
    const node = queue.shift();
    if (node === dst) return true;

    graph[node].forEach(neighbor => queue.push(neighbor));
  }

  return false;
};

// ========================= Depth First =========================
const hasPath = (graph, src, dst) => { // Time: O(e), Space: O(n)
  if (src === dst) return true;

  for (let neighbor of graph[src]) {
    if (hasPath(graph, neighbor, dst) === true) return true;
  }

  return false;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #39 undirected path ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, undirectedPath, that takes in an array of edges for an 
// undirected graph and two nodes (nodeA, nodeB). The function should return a 
// boolean indicating whether or not there exists a path between nodeA and nodeB.
//
// test_00:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
//
// undirectedPath(edges, 'j', 'm'); // -> true
//
// test_01:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
//
// undirectedPath(edges, 'm', 'j'); // -> true
//
// test_02:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
//
// undirectedPath(edges, 'l', 'j'); // -> true
//
// test_03:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
//
// undirectedPath(edges, 'k', 'o'); // -> false
// test_04:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
//
// undirectedPath(edges, 'i', 'o'); // -> false
//
// test_05:
// const edges = [
//   ['b', 'a'],
//   ['c', 'a'],
//   ['b', 'c'],
//   ['q', 'r'],
//   ['q', 's'],
//   ['q', 'u'],
//   ['q', 't'],
// ];
//
// undirectedPath(edges, 'a', 'b'); // -> true
//
// test_06:
// const edges = [
//   ['b', 'a'],
//   ['c', 'a'],
//   ['b', 'c'],
//   ['q', 'r'],
//   ['q', 's'],
//   ['q', 'u'],
//   ['q', 't'],
// ];
//
// undirectedPath(edges, 'a', 'c'); // -> true
//
// test_07:
// const edges = [
//   ['b', 'a'],
//   ['c', 'a'],
//   ['b', 'c'],
//   ['q', 'r'],
//   ['q', 's'],
//   ['q', 'u'],
//   ['q', 't'],
// ];
//
// undirectedPath(edges, 'r', 't'); // -> true
//
// test_08:
// const edges = [
//   ['b', 'a'],
//   ['c', 'a'],
//   ['b', 'c'],
//   ['q', 'r'],
//   ['q', 's'],
//   ['q', 'u'],
//   ['q', 't'],
// ];
//
// undirectedPath(edges, 'r', 'b'); // -> false

// ========================= Depth First =========================
const undirectedPath = (edges, nodeA, nodeB) => { // Time: O(e), Space: O(n)
  const graph = {};
  edges.forEach(edge => {
    const [ node1, node2 ] = edge;

    if (!node1 in graph) {
      graph[node1].push(node2);
    } else {
      graph[node1] = [node2];
    }
    if (!node2 in graph) {
      graph[node2].push(node1);
    } else {
      graph[node2] = [node1];
    }
  });

  return validPath(graph, nodeA, nodeB);
};

const validPath = (graph, nodeA, nodeB, visited = new Set()) => { // Time: O(e), Space: O(n)
  if (nodeA === nodeB) return true;
  visited.add(nodeA);

  for (let neighbor of graph[nodeA]) {
    if (!visited.has(neighbor)) {
      if (validPath(graph, neighbor, nodeB, visited) === true) return true;
    }  
  }  

  return false;
};  

// [[[[[[[[[[[[[[[[[[[[[[[[[ #40 connected components count ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, connectedComponentsCount, that takes in the adjacency list 
// of an undirected graph. The function should return the number of connected 
// components within the graph.
//
// test_00:
// connectedComponentsCount({
//   0: [8, 1, 5],
//   1: [0],
//   5: [0, 8],
//   8: [0, 5],
//   2: [3, 4],
//   3: [2, 4],
//   4: [3, 2]
// }); // -> 2
//
// test_01:
// connectedComponentsCount({
//   1: [2],
//   2: [1,8],
//   6: [7],
//   9: [8],
//   7: [6, 8],
//   8: [9, 7, 2]
// }); // -> 1
//
// test_02:
// connectedComponentsCount({
//   3: [],
//   4: [6],
//   6: [4, 5, 7, 8],
//   8: [6],
//   7: [6],
//   5: [6],
//   1: [2],
//   2: [1]
// }); // -> 3
//
// test_03:
// connectedComponentsCount({}); // -> 0
//
// test_04:
// connectedComponentsCount({
//   0: [4,7],
//   1: [],
//   2: [],
//   3: [6],
//   4: [0],
//   6: [3],
//   7: [0],
//   8: []
// }); // -> 5

// ========================= Depth First =========================
const connectedComponentsCount = (graph) => { // Time: O(e), Space: O(n)
  let count = 0;
  
  const visited = new Set();
  for (let node in graph) {
    if (exploreComponent(graph, node, visited) === true) count++;
  }
  
  return count;
};

const exploreComponent = (graph, node, visited) => { // Time: O(e), Space: O(n)
  if (visited.has(parseInt(node))) return false;
  visited.add(parseInt(node));

  for (let neighbor of graph[node]) {
    exploreComponent(graph, neighbor, visited);
  }

  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #41 largest component ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, largestComponent, that takes in the adjacency list of an 
// undirected graph. The function should return the size of the largest connected
// component in the graph.
//
// test_00:
// largestComponent({
//   0: ['8', '1', '5'],
//   1: ['0'],
//   5: ['0', '8'],
//   8: ['0', '5'],
//   2: ['3', '4'],
//   3: ['2', '4'],
//   4: ['3', '2']
// }); // -> 4
//
// test_01:
// largestComponent({
//   1: ['2'],
//   2: ['1','8'],
//   6: ['7'],
//   9: ['8'],
//   7: ['6', '8'],
//   8: ['9', '7', '2']
// }); // -> 6
//
// test_02:
// largestComponent({
//   3: [],
//   4: ['6'],
//   6: ['4', '5', '7', '8'],
//   8: ['6'],
//   7: ['6'],
//   5: ['6'],
//   1: ['2'],
//   2: ['1']
// }); // -> 5
//
// test_03:
// largestComponent({}); // -> 0
//
// test_04:
// largestComponent({
//   0: ['4','7'],
//   1: [],
//   2: [],
//   3: ['6'],
//   4: ['0'],
//   6: ['3'],
//   7: ['0'],
//   8: []
// }); // -> 3

// ========================= Depth First =========================
const largestComponent = (graph) => { // Time: O(e), Space: O(n)
  let largest = 0;

  const visited = new Set();
  for (let node in graph) {
    const componentSize = exploreComponent(graph, node, visited);
    if (componentSize > largest) largest = componentSize;
  }

  return largest;
};

const exploreComponent = (graph, node, visited, size = 0) => {
  if (visited.has(node)) return size;
  visited.add(node);
  size++;

  for (let neighbor of graph[node]) {
    size += exploreComponent(graph, neighbor, visited);
  }
  
  return size;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #42 shortest path ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, shortestPath, that takes in an array of edges for an 
// undirected graph and two nodes (nodeA, nodeB). The function should return the
// length of the shortest path between A and B. Consider the length as the number
// of edges in the path, not the number of nodes. If there is no path between A 
// and B, then return -1.
//
// test_00:
// const edges = [
//   ['w', 'x'],
//   ['x', 'y'],
//   ['z', 'y'],
//   ['z', 'v'],
//   ['w', 'v']
// ];
//
// shortestPath(edges, 'w', 'z'); // -> 2
//
// test_01:
// const edges = [
//   ['w', 'x'],
//   ['x', 'y'],
//   ['z', 'y'],
//   ['z', 'v'],
//   ['w', 'v']
// ];
//
// shortestPath(edges, 'y', 'x'); // -> 1
//
// test_02:
// const edges = [
//   ['a', 'c'],
//   ['a', 'b'],
//   ['c', 'b'],
//   ['c', 'd'],
//   ['b', 'd'],
//   ['e', 'd'],
//   ['g', 'f']
// ];
//
// shortestPath(edges, 'a', 'e'); // -> 3
//
// test_03:
// const edges = [
//   ['a', 'c'],
//   ['a', 'b'],
//   ['c', 'b'],
//   ['c', 'd'],
//   ['b', 'd'],
//   ['e', 'd'],
//   ['g', 'f']
// ];
//
// shortestPath(edges, 'e', 'c'); // -> 2
//
// test_04:
// const edges = [
//   ['a', 'c'],
//   ['a', 'b'],
//   ['c', 'b'],
//   ['c', 'd'],
//   ['b', 'd'],
//   ['e', 'd'],
//   ['g', 'f']
// ];
//
// shortestPath(edges, 'b', 'g'); // -> -1
//
// test_05:
// const edges = [
//   ['c', 'n'],
//   ['c', 'e'],
//   ['c', 's'],
//   ['c', 'w'],
//   ['w', 'e'],
// ];
//
// shortestPath(edges, 'w', 'e'); // -> 1
//
// test_06:
// const edges = [
//   ['c', 'n'],
//   ['c', 'e'],
//   ['c', 's'],
//   ['c', 'w'],
//   ['w', 'e'],
// ];
//
// shortestPath(edges, 'n', 'e'); // -> 2
//
// test_07:
// const edges = [
//   ['m', 'n'],
//   ['n', 'o'],
//   ['o', 'p'],
//   ['p', 'q'],
//   ['t', 'o'],
//   ['r', 'q'],
//   ['r', 's']
// ];
//
// shortestPath(edges, 'm', 's'); // -> 6

const shortestPath = (edges, nodeA, nodeB) => {
  const graph = buildGraph(edges);
  const visited = new Set();
  const queue = [{ node: nodeA, length: 0 }];

  while (queue.length) {
    const { node, length } = queue.shift();
    if (node === nodeB) return length;
    visited.add(node);

    for (let neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        queue.push({ node: neighbor, length: length + 1 });
      }
    }
  }

  return -1;
};

const buildGraph = (edges) => {
  const graph = {};
  for (let edge of edges) {
    const [ node1, node2 ] = edge;
    if (graph[node1]) {
      graph[node1].push(node2);
    } else {
      graph[node1] = [node2];
    }
    if (graph[node2]) {
      graph[node2].push(node1);
    } else {
      graph[node2] = [node1];
    }
  }
  return graph;
};