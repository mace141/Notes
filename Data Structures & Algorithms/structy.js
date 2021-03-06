// [[[[[[[[[[[[[[[[[[[[[[[[[ #1 max value ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, maxValue, that takes in array of numbers as an argument. 
// The function should return the largest number in the array.
// Solve this without using any built-in array methods.
// You can assume that the array is non-empty.
//
// test_00:
// maxValue([4, 7, 2, 8, 10, 9]); // -> 10
// test_01:
// maxValue([10, 5, 40, 40.3]); // -> 40.3
// test_02:
// maxValue([-5, -2, -1, -11]); // -> -1
// test_03:
// maxValue([42]); // -> 42
// test_04:
// maxValue([1000, 8]); // -> 1000
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
// const maxValue = (nums) => {
//   let maximum = -Infinity;
//   for (let num of nums) {
//     if (num > maximum) maximum = num;
//   }
//   return maximum;
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #2 is prime ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, isPrime, that takes in a number as an argument. The function 
// should return a boolean indicating whether or not the given number is prime.
// A prime number is a number that is only divisible two distinct numbers: 1 and itself.
// For example, 7 is a prime because it is only divisible by 1 and 7. For example, 
// 6 is not a prime because it is divisible by 1, 2, 3, and 6.
// You can assume that the input number is a positive integer.
//
// test_00:
// isPrime(2); // -> true
// test_01:
// isPrime(3); // -> true
// test_02:
// isPrime(4); // -> false
// test_03:
// isPrime(5); // -> true
// test_04:
// isPrime(6); // -> false
// test_05:
// isPrime(7); // -> true
// test_06:
// isPrime(8); // -> false
// test_07:
// isPrime(25); // -> false
// test_08:
// isPrime(31); // -> true
// test_09:
// isPrime(2017); // -> true
// test_10:
// isPrime(2048); // -> false
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
// <number><char>
// for example, '2c' or '3a'.
// The function should return an uncompressed version of the string where each 
// 'char' of a group is repeated 'number' times concecutively. You may assume that 
// the input string is well-formed according to the previously mentioned pattern.
//
// test_00:
// uncompress("2c3a1t"); // -> 'ccaaat'
// test_01:
// uncompress("4s2b"); // -> 'ssssbb'
// test_02:
// uncompress("2p1o5p"); // -> 'ppoppppp'
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
// Write a function, compress, that takes in a string as an argument. The function 
// should return a compressed version of the string where consecutive occurences
// of the same characters are compressed into the number of occurences followed 
// by the character. Single character occurences should not be changed.
// 'aaa' compresses to '3a'
// 'cc' compresses to '2c'
// 't' should remain as 't'
// You can assume that the input only contains alphabetic characters.
//
// test_00:
// compress('ccaaatsss'); // -> '2c3at3s'
// test_01:
// compress('ssssbbz'); // -> '4s2bz'
// test_02:
// compress('ppoppppp'); // -> '2po5p'
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
// test_01:
// anagrams('cats', 'tocs'); // -> false
// test_02:
// anagrams('monkeyswrite', 'newyorktimes'); // -> true
// test_03:
// anagrams('paper', 'reapa'); // -> false
// test_04:
// anagrams('elbow', 'below'); // -> true
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
// You can assume that the input string is non-empty.
//
// test_00:
// mostFrequentChar('bookeeper'); // -> 'e'
// test_01:
// mostFrequentChar('david'); // -> 'd'
// test_02:
// mostFrequentChar('abby'); // -> 'b'
// test_03:
// mostFrequentChar('mississippi'); // -> 'i'
// test_04:
// mostFrequentChar('potato'); // -> 'o'
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
// Be sure to return the indices, not the elements themselves.
// There is guaranteed to be one such pair that sums to the target.
//
// test_00:
// pairSum([3, 2, 5, 4, 1], 8); // -> [0, 2]
// test_01:
// pairSum([4, 7, 9, 2, 5, 1], 5); // -> [0, 5]
// test_02:
// pairSum([4, 7, 9, 2, 5, 1], 3); // -> [3, 5]
// test_03:
// pairSum([1, 6, 7, 2], 13); // -> [1, 2]
// test_04:
// pairSum([9, 9], 18); // -> [0, 1]
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
// Be sure to return the indices, not the elements themselves.
// There is guaranteed to be one such pair whose product is the target.
//
// test_00:
// pairProduct([3, 2, 5, 4, 1], 8); // -> [1, 3]
// test_01:
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
// test_02:
// pairProduct([4, 7, 9, 2, 5, 1], 5); // -> [4, 5]
// test_03:
// pairProduct([4, 7, 9, 2, 5, 1], 35); // -> [1, 4]
// test_04:
// pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
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
// You may assume that each input array does not contain duplicate elements.
//
// test_00:
// intersection([4,2,1,6], [3,6,9,2,10]) // -> [2,6]
// test_01:
// intersection([2,4,6], [4,2]) // -> [2,4]
// test_02:
// intersection([4,2,1], [1,2,4,6]) // -> [1,2,4]
// test_03:
// intersection([0,1,2], [10,11]) // -> []
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
// Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.
//
// test_00
// fiveSort([12, 5, 1, 5, 12, 7]);
// -> [12, 7, 1, 12, 5, 5] 
// test_01
// fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
// test_02
// fiveSort([5, 5, 5, 1, 1, 1, 4]);
// -> [4, 1, 1, 1, 5, 5, 5] 
// test_03
// fiveSort([5, 5, 6, 5, 5, 5, 5]);
// -> [6, 5, 5, 5, 5, 5, 5] 
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
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// linkedListValues(a); // -> [ 'a', 'b', 'c', 'd' ]
// test_01:
// const x = new Node("x");
// const y = new Node("y");
// x.next = y;
// x -> y
// linkedListValues(x); // -> [ 'x', 'y' ]
// test_02:
// const q = new Node("q");
// q
// linkedListValues(q); // -> [ 'q' ]
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
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// 2 -> 8 -> 3 -> -1 -> 7
// sumList(a); // 19
// test_01:
// const x = new Node(38);
// const y = new Node(4);
// x.next = y;
// 38 -> 4
// sumList(x); // 42
// test_02:
// const z = new Node(100);
// 100
// sumList(z); // 100
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
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// linkedListFind(a, "c"); // true
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// linkedListFind(a, "d"); // true
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// linkedListFind(a, "q"); // false
// test_03:
// const node1 = new Node("jason");
// const node2 = new Node("leneli");
// node1.next = node2;
// jason -> leneli
// linkedListFind(node1, "jason"); // true
// test_04:
// const node1 = new Node(42);
// 42
// linkedListFind(node1, 42); // true
// test_05:
// const node1 = new Node(42);
// 42
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
// If there is no node at the given index, then return null.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// getNodeValue(a, 2); // 'c'
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// getNodeValue(a, 3); // 'd'
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// getNodeValue(a, 7); // null
// test_03:
// const node1 = new Node("banana");
// const node2 = new Node("mango");
// node1.next = node2;
// banana -> mango
// getNodeValue(node1, 0); // 'banana'
// test_04:
// const node1 = new Node("banana");
// const node2 = new Node("mango");
// node1.next = node2;
// banana -> mango
// getNodeValue(node1, 1); // 'mango'

// ========================= Iterative =========================
// Time: O(n), Space: O(1)
const getNodeValue = (head, index) => {
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
// Time: O(n), Space: O(n)
const getNodeValue = (head, index) => {
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
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// a -> b -> c -> d -> e -> f
// reverseList(a); // f -> e -> d -> c -> b -> a
// test_01:
// const x = new Node("x");
// const y = new Node("y");
// x.next = y;
// x -> y
// reverseList(x); // y -> x
// test_02:
// const p = new Node("p");
// p
// reverseList(p); // p

// ========================= Iterative =========================
// Time: O(n), Space: O(1)
const reverseList = (head) => {
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
// Time: O(n), Space: O(n)
const reverseList = (head, prev = null) => {
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
// Do this in-place, by mutating the original Nodes.
// You may assume that both input lists are non-empty.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// a.next = b;
// b.next = c;
// a -> b -> c
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// x -> y -> z
// zipperLists(a, x);
// a -> x -> b -> y -> c -> z
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
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// x -> y -> z
// zipperLists(a, x);
// a -> x -> b -> y -> c -> z -> d -> e -> f
// test_02:
// const s = new Node("s");
// const t = new Node("t");
// s.next = t;
// s -> t
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// const four = new Node(4);
// one.next = two;
// two.next = three;
// three.next = four;
// 1 -> 2 -> 3 -> 4
// zipperLists(s, one);
// s -> 1 -> t -> 2 -> 3 -> 4
// test_03:
// const w = new Node("w");
// w
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// 1 -> 2 -> 3 
// 
// zipperLists(w, one);
// w -> 1 -> 2 -> 3
// test_04:
// const one = new Node(1);
// const two = new Node(2);
// const three = new Node(3);
// one.next = two;
// two.next = three;
// 1 -> 2 -> 3 
// const w = new Node("w");
// w
// zipperLists(one, w);
// 1 -> w -> 2 -> 3

// ========================= Iterative =========================
// Time: O(min(n, m)), Space: O(1)
const zipperLists = (head1, head2) => {
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
// Time: O(min(n, m)), Space: O(min(n, m))
const zipperLists = (head1, head2) => {
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
// Do this in-place, by mutating the original Nodes.
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
// const q = new Node(6);
// const r = new Node(8);
// const s = new Node(9);
// const t = new Node(25);
// q.next = r;
// r.next = s;
// s.next = t;
// 6 -> 8 -> 9 -> 25
// mergeLists(a, q);
// 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28 
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
// const q = new Node(1);
// const r = new Node(8);
// const s = new Node(9);
// const t = new Node(10);
// q.next = r;
// r.next = s;
// s.next = t;
// 1 -> 8 -> 9 -> 10
// mergeLists(a, q);
// 1 -> 5 -> 7 -> 8 -> 9 -> 10 -> 10 -> 12 -> 20 -> 28 
// test_02:
// const h = new Node(30);
// 30
// const p = new Node(15);
// const q = new Node(67);
// p.next = q;
// 15 -> 67
// mergeLists(h, p);
// 15 -> 30 -> 67

// ========================= Iterative =========================
// Time: O(min(n, m)), Space: O(1)
const mergeLists = (head1, head2) => {
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
// Time: O(min(n, m)), Space: O(min(n, m))
const mergeLists = (head1, head2) => {
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
// You may assume that the input list is non-empty.
//
// test_00:
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(7);
// a.next = b;
// b.next = c;
// 7 -> 7 -> 7
// isUnivalueList(a); // true
// test_01:
// const a = new Node(7);
// const b = new Node(7);
// const c = new Node(4);
// a.next = b;
// b.next = c;
// 7 -> 7 -> 4
// isUnivalueList(a); // false
// test_02:
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(2);
// const x = new Node(2);
// const y = new Node(2);
// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;
// 2 -> 2 -> 2 -> 2 -> 2
// isUnivalueList(u); // true
// test_03:
// const u = new Node(2);
// const v = new Node(2);
// const w = new Node(3);
// const x = new Node(3);
// const y = new Node(2);
// u.next = v;
// v.next = w;
// w.next = x;
// x.next = y;
// 2 -> 2 -> 3 -> 3 -> 2
// isUnivalueList(u); // false
// test_04:
// const z = new Node('z');
// z
// isUnivalueList(z); // true

// ========================= Iterative =========================
// Time: O(n), Space: O(1)
const isUnivalueList = (head) => {
  const value = head.val;
  let currNode = head;

  while (currNode !== null) {
    if (currNode.val !== value) return false;
    currNode = currNode.next;
  }

  return true;
};

// ========================= Recursive =========================
// Time: O(n), Space: O(n)
const isUnivalueList = (head, prev = head) => {
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
// test_01:
// const a = new Node(3);
// const b = new Node(3);
// const c = new Node(3);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(9);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 3 -> 3 -> 3 -> 3 -> 9 -> 9
// longestStreak(a); // 4
// test_02:
// const a = new Node(9);
// const b = new Node(9);
// const c = new Node(1);
// const d = new Node(9);
// const e = new Node(9);
// const f = new Node(9);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 9 -> 9 -> 1 -> 9 -> 9 -> 9
// longestStreak(a); // 3
// test_03:
// const a = new Node(5);
// const b = new Node(5);
// a.next = b;
// 5 -> 5
// longestStreak(a); // 2
// test_04:
// const a = new Node(4);
// 4
// longestStreak(a); // 1
// test_05:
// longestStreak(null); // 0

// Time: O(n), Space: O(1)
const longestStreak = (head) => {
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
// Do this in-place.
// You may assume that the input list is non-empty.
//
// test_00:
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
// removeNode(a, "c");
// a -> b -> d -> e -> f
// test_01:
// const x = new Node("x");
// const y = new Node("y");
// const z = new Node("z");
// x.next = y;
// y.next = z;
// x -> y -> z
// removeNode(x, "z");
// x -> y
// test_02:
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");
// q.next = r;
// r.next = s;
// q -> r -> s
// removeNode(q, "q");
// r -> s
// test_03:
// const node1 = new Node("h");
// const node2 = new Node("i");
// const node3 = new Node("j");
// const node4 = new Node("i");
// node1.next = node2;
// node2.next = node3;
// node3.next = node4;
// h -> i -> j -> i
// removeNode(node1, "i");
// h -> j -> i
// test_04:
// const t = new Node("t");
// t
// removeNode(t, "t");
// null

// ========================= Iterative =========================
// Time: O(n), Space: O(1)
const removeNode = (head, targetVal) => {
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
// Time: O(n), Space: O(n)
const removeNode = (head, targetVal) => {
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
// Do this in-place.
// You may assume that the input list is non-empty and the index is not greater 
// than the length of the input list.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// insertNode(a, 'x', 2);
// a -> b -> x -> c -> d
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// insertNode(a, 'v', 3);
// a -> b -> c -> v -> d
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d
// insertNode(a, 'm', 4);
// a -> b -> c -> d -> m
// test_03:
// const a = new Node("a");
// const b = new Node("b");
// a.next = b;
// a -> b
// insertNode(a, 'z', 0);
// z -> a -> b 

// ========================= Iterative =========================
// Time: O(n), Space: O(1)
const insertNode = (head, value, index) => {
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
// Time: O(n), Space: O(n)
const insertNode = (head, value, index, count = 0) => {
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
// test_01:
// createLinkedList([1, 7, 1, 8]);
// 1 -> 7 -> 1 -> 8
// test_02:
// createLinkedList(["a"]);
// a
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
// Say we wanted to compute 621 + 354 normally. The sum is 975:
//    621
//  + 354
//  -----
//    975
// Then, the reversed linked list format of this problem would appear as:
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
// const a1 = new Node(1);
// const a2 = new Node(2);
// const a3 = new Node(6);
// a1.next = a2;
// a2.next = a3;
// 1 -> 2 -> 6
// const b1 = new Node(4);
// const b2 = new Node(5);
// const b3 = new Node(3);
// b1.next = b2;
// b2.next = b3;
// 4 -> 5 -> 3
// addLists(a1, b1);
// 5 -> 7 -> 9
// test_01:
//  7541
// +  32
// -----
//  7573
// const a1 = new Node(1);
// const a2 = new Node(4);
// const a3 = new Node(5);
// const a4 = new Node(7);
// a1.next = a2;
// a2.next = a3;
// a3.next = a4;
// 1 -> 4 -> 5 -> 7
// const b1 = new Node(2);
// const b2 = new Node(3);
// b1.next = b2;
// 2 -> 3 
// addLists(a1, b1);
// 3 -> 7 -> 5 -> 7
// test_02:
//   39
// + 47
// ----
//   86
// const a1 = new Node(9);
// const a2 = new Node(3);
// a1.next = a2;
// 9 -> 3
// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// 7 -> 4
// addLists(a1, b1);
// 6 -> 8
// test_03:
//   89
// + 47
// ----
//  136
// const a1 = new Node(9);
// const a2 = new Node(8);
// a1.next = a2;
// 9 -> 8
// const b1 = new Node(7);
// const b2 = new Node(4);
// b1.next = b2;
// 7 -> 4
// addLists(a1, b1);
// 6 -> 3 -> 1
// test_04:
//   999
//  +  6
//  ----
//  1005
// const a1 = new Node(9);
// const a2 = new Node(9);
// const a3 = new Node(9);
// a1.next = a2;
// a2.next = a3;
// 9 -> 9 -> 9
// const b1 = new Node(6);
// 6
// addLists(a1, b1);
// 5 -> 0 -> 0 -> 1

// ========================= Iterative =========================
// Time: O(max(n, m)), Space: O(max(n, m))
const addLists = (head1, head2) => {
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
// Time: O(max(n, m)), Space: O(max(n, m))
const addLists = (head1, head2, carry = 0) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g
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
// a.right = b;
// b.left = c;
// c.right = d;
// d.right = e;
//      a
//       \
//        b
//       /
//      c
//       \
//        d
//         \
//          e
// depthFirstValues(a); 
//    -> ['a', 'b', 'c', 'd', 'e']
// test_04:
// howHigh(null); 
//    -> []


// ========================= Iterative =========================
// Time: O(n), Space: O(n)
const depthFirstValues = (root) => {
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
// Time: O(n), Space: O(n)
const depthFirstValues = (root) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// breadthFirstValues(a); 
//    -> ['a', 'b', 'c', 'd', 'e', 'f']
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// breadthFirstValues(a); 
//   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
// test_02:
// const a = new Node('a');
//      a
// breadthFirstValues(a); 
//    -> ['a']
// test_03:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const x = new Node('x');
// a.right = b;
// b.left = c;
// c.left = x;
// c.right = d;
// d.right = e;
//      a
//       \
//        b
//       /
//      c
//    /  \
//   x    d
//         \
//          e
// breadthFirstValues(a); 
//    -> ['a', 'b', 'c', 'x', 'd', 'e']
// test_04:
// howHigh(null); 
//    -> []

// ========================= Iterative =========================
// Time: O(n^2), Space: O(n)
// Time is n^2 because of JavaScript's shift function
const breadthFirstValues = (root) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// treeIncludes(a, "e"); // -> true
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// treeIncludes(a, "a"); // -> true
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// treeIncludes(a, "n"); // -> false
// test_03:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// treeIncludes(a, "f"); // -> true
// test_04:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// treeIncludes(a, "p"); // -> false
// test_05:
// treeIncludes(null, "b"); // -> false

// ========================= Breadth First =========================
// Time: O(n^2), Space: O(n)
const treeIncludes = (root, target) => {
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
// Time: O(n), Space: O(n)
const treeIncludes = (root, target) => {
  if (root === null) return false;
  if (root.val === target) return true;
  return treeIncludes(root.left, target) || treeIncludes(root.right, target);
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
// treeSum(a); // -> 21
// test_01:
// const a = new Node(1);
// const b = new Node(6);
// const c = new Node(0);
// const d = new Node(3);
// const e = new Node(-6);
// const f = new Node(2);
// const g = new Node(2);
// const h = new Node(2);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      1
//    /   \
//   6     0
//  / \     \
// 3   -6    2
//    /       \
//   2         2
// treeSum(a); // -> 10
// test_02:
// treeSum(null); // -> 0

// ========================= Depth First =========================
// Time: O(n), Space: O(n)
const treeSum = (root) => {
  if (root === null) return 0;

  return root.val + treeSum(root.left) + treeSum(root.right);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #28 tree min value ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, treeMinValue, that takes in the root of a binary tree that 
// contains number values. The function should return the minimum value within 
// the tree.
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
// treeMinValue(a); // -> -2
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(3);
// const d = new Node(4);
// const e = new Node(14);
// const f = new Node(12);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//       5
//    /    \
//   11     3
//  / \      \
// 4   15     12
// treeMinValue(a); // -> 3
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(-2);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     /       \
//    -2       -2
// tree_min_value(a); // -> -13
// test_03:
// const a = new Node(42);
//        42
// tree_min_value(a); // -> 42

// ========================= Depth First Recursive =========================
// Time: O(n), Space: O(n)
const treeMinValue = (root) => {
  if (root === null) return Infinity;

  const minLeft = treeMinValue(root.left);
  const minRight = treeMinValue(root.right);

  return Math.min(root.val, minLeft, minRight);
};

// ========================= Depth First Iterative =========================
// Time: O(n), Space: O(n)
const treeMinValue = (root) => {
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
// Time: O(n^2), Space: O(n)
const treeMinValue = (root) => {
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
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(4);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      3
//    /   \
//   11    4
//  / \     \
// 4   -2    1
// maxPathSum(a); // -> 18
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//       5
//     /   \
//    11   54
//  /   \
// 20   15
//      / \
//     1  3
// maxPathSum(a); // -> 59
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(-13);
// const g = new Node(-1);
// const h = new Node(-2);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0    -13
//     /       \
//    -1       -2
// maxPathSum(a); // -> -8
// test_03:
// const a = new Node(42);
//        42
// maxPathSum(a); // -> 42

// ========================= Depth First =========================
// Time: O(n), Space: O(n)
const maxPathSum = (root) => {
  if (root === null) return -Infinity;
  if (root.left === null && root.right === null) return root.val;

  return root.val + Math.max(maxPathSum(root.left), maxPathSum(root.right));
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #30 path finder ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, pathFinder, that takes in the root of a binary tree and a 
// target value. The function should return an array representing a path to the 
// target value. If the target value is not found in the tree, then return null.
// You may assume that the tree contains unique values.
//
// test_00:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// pathFinder(a, 'e'); // -> [ 'a', 'b', 'e' ]
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// pathFinder(a, 'p'); // -> null
// test_02:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// pathFinder(a, "c"); // -> ['a', 'c']
// test_03:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// pathFinder(a, "h"); // -> ['a', 'c', 'f', 'h']
// test_04:
// const x = new Node("x");
//      x
// pathFinder(x, "x"); // -> ['x']
// test_05:
// pathFinder(null, "x"); // -> null
// test_06:
// const root = new Node(0);
// let curr = root;
// for (let i = 1; i <= 6000; i += 1) {
//   curr.right = new Node(i);
//   curr = curr.right;
// }
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
// pathFinder(root, 3451); // -> [0, 1, 2, 3, ..., 3450, 3451]

// ========================= My Solution =========================
// Time: O(n^2), Space: O(n)
const pathFinder = (root, target, cameFrom = {}) => {
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
// Time: O(n), Space: O(n)
const pathFinder = (root, target) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//     12
//    /  \
//   6    6
//  / \    \
// 4   6    12
// treeValueCount(a,  6); // -> 3
// test_01:
// const a = new Node(12);
// const b = new Node(6);
// const c = new Node(6);
// const d = new Node(4);
// const e = new Node(6);
// const f = new Node(12);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//     12
//    /  \
//   6    6
//  / \    \
// 4   6    12
// treeValueCount(a,  12); // -> 2
// test_02:
// const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1
// treeValueCount(a, 1); // -> 4
// test_03:
// const a = new Node(7);
// const b = new Node(5);
// const c = new Node(1);
// const d = new Node(1);
// const e = new Node(8);
// const f = new Node(7);
// const g = new Node(1);
// const h = new Node(1);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1
// treeValueCount(a, 9); // -> 0
// test_04:
// treeValueCount(null, 42); // -> 0

// ========================= Depth First =========================
// Time: O(n), Space: O(n)
const treeValueCount = (root, target) => {
  if (root === null) return 0;

  const leftCount = treeValueCount(root.left, target);
  const rightCount = treeValueCount(root.right, target);

  return (root.val === target ? 1 : 0) + leftCount + rightCount;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #32 how high ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, howHigh, that takes in the root of a binary tree. The 
// function should return a number representing the height of the tree.
// The height of a binary tree is defined as the maximal number of edges from 
// the root node to any leaf node.
// If the tree is empty, return -1.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// howHigh(a); // -> 2
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /
//   g
// howHigh(a); // -> 3
// test_02:
// const a = new Node('a');
// const c = new Node('c');
// a.right = c;
//      a
//       \
//        c
// howHigh(a); // -> 1
// test_03:
// const a = new Node('a');
//      a
// howHigh(a); // -> 0

// ========================= Recursive =========================
// Time: O(n), Space: O(n)
const howHigh = (root) => {
  if (root === null) return -1;

  const leftHeight = howHigh(root.left);
  const rightHeight = howHigh(root.right);

  return 1 + Math.max(leftHeight, rightHeight);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #33 bottom right value ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, bottomRightValue, that takes in the root of a binary tree. 
// The function should return the right-most value in the bottom-most level of 
// the tree.
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node(3);
// const b = new Node(11);
// const c = new Node(10);
// const d = new Node(4);
// const e = new Node(-2);
// const f = new Node(1);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//       3
//    /    \
//   11     10
//  / \      \
// 4   -2     1
// bottomRightValue(a); // -> 1
// test_01:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(-4);
// const f = new Node(-13);
// const g = new Node(-2);
// const h = new Node(6);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     / \       
//    -2  6
// bottomRightValue(a); // -> 6
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   -4   -13
//     / \    /   
//    -2  6  7 
// bottomRightValue(a); // -> 7
// test_03
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// a.left = b;
// a.right = c;
// b.right = d;
// d.left = e;
// e.right = f;
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
// test_04
// const a = new Node(42);
//      42
// bottomRightValue(a); // -> 42

// ========================= Breadth First =========================
// Time: O(n^2), Space: O(n)
const bottomRightValue = (root) => {
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
// The order within an individual path must start at the root and end at the leaf,
// but the relative order of among paths in the outer array does not matter.
// You may assume that the input tree is non-empty.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// allTreePaths(a); // ->
// [ 
//   [ 'a', 'b', 'd' ], 
//   [ 'a', 'b', 'e' ], 
//   [ 'a', 'c', 'f' ] 
// ] 
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
// a.l//eft = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//         a
//      /    \
//     b      c
//   /  \      \
//  d    e      f
//      / \    /   
//     g  h   i 
// allTreePaths(a); // ->
// [ 
//   [ 'a', 'b', 'd' ], 
//   [ 'a', 'b', 'e', 'g' ], 
//   [ 'a', 'b', 'e', 'h' ], 
//   [ 'a', 'c', 'f', 'i' ] 
// ] 
// test_02:
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// const u = new Node('u');
// const v = new Node('v');
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//      q
//    /   \ 
//   r     s
//    \
//     t
//    /
//   u
//  /
// v
// allTreePaths(q); // ->
// [ 
//   [ 'q', 'r', 't', 'u', 'v' ], 
//   [ 'q', 's' ] 
// ] 
// test_03:
// const z = new Node('z');
//      z
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// treeLevels(a); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f']
// ]
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
// f.left = i;
//         a
//      /    \
//     b      c
//   /  \      \
//  d    e      f
//      / \    /
//     g  h   i
// treeLevels(a); // ->
// [
//   ['a'],
//   ['b', 'c'],
//   ['d', 'e', 'f'],
//   ['g', 'h', 'i']
// ]
// test_02:
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");
// const t = new Node("t");
// const u = new Node("u");
// const v = new Node("v");
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//      q
//    /   \
//   r     s
//    \
//     t
//    /
//   u
//  /
// v
// treeLevels(q); //->
// [
//   ['q'],
//   ['r', 's'],
//   ['t'],
//   ['u'],
//   ['v']
// ]
// test_03:
// treeLevels(null); // -> []

// ========================= Breadth First =========================
// Time: O(n^2), Space: O(n)
const treeLevels = (root) => {
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
// Time: O(n), Space: O(n)
const treeLevels = (root, levelsArr = [], level = 0) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1
// levelAverages(a); // -> [ 3, 7.5, 1 ] 
// test_01:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3
// levelAverages(a); // -> [ 5, 32.5, 17.5, 2 ] 
// test_02:
// const a = new Node(-1);
// const b = new Node(-6);
// const c = new Node(-5);
// const d = new Node(-3);
// const e = new Node(0);
// const f = new Node(45);
// const g = new Node(-1);
// const h = new Node(-2);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0     45
//     /       \
//    -1       -2
// levelAverages(a); // -> [ -1, -5.5, 14, -1.5 ]
// test_03:
// const q = new Node(13);
// const r = new Node(4);
// const s = new Node(2);
// const t = new Node(9);
// const u = new Node(2);
// const v = new Node(42);
// q.left = r;
// q.right = s;
// r.right = t;
// t.left = u;
// u.right = v;
//        13
//      /   \
//     4     2
//      \
//       9
//      /
//     2
//    /
//   42
// levelAverages(q); // -> [ 13, 3, 9, 2, 42 ]
// test_04:
// levelAverages(null); // -> [ ]

// ========================= Breadth First =========================
// Time: O(n^2), Space: O(n)
const levelAverages = (root) => {
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
// Time: O(n), Space: O(n)
const levelAverages = (root, levelsArr = [], level = 0) => {
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
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
// leafList(a); // -> [ 'd', 'e', 'f' ] 
// test_01:
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// f.right = h;
//      a
//    /   \
//   b     c
//  / \     \
// d   e     f
//    /       \
//   g         h
// leafList(a); // -> [ 'd', 'g', 'h' ]
// test_02:
// const a = new Node(5);
// const b = new Node(11);
// const c = new Node(54);
// const d = new Node(20);
// const e = new Node(15);
// const f = new Node(1);
// const g = new Node(3);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// e.left = f;
// e.right = g;
//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3
// leafList(a); // -> [ 20, 1, 3, 54 ]
// test_03:
// const x = new Node('x');
//      x
// leafList(x); // -> [ 'x' ]
// test_04:
// leafList(null); // -> [ ]

// ========================= Depth First =========================
// Time: O(n), Space: O(n)
const leafList = (root, leaves = []) => {
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
// hasPath(graph, 'f', 'k'); // true
// test_01:
// const graph = {
//   f: ['g', 'i'],
//   g: ['h'],
//   h: [],
//   i: ['g', 'k'],
//   j: ['i'],
//   k: []
// };
// hasPath(graph, 'f', 'j'); // false
// test_02:
// const graph = {
//   f: ['g', 'i'],
//   g: ['h'],
//   h: [],
//   i: ['g', 'k'],
//   j: ['i'],
//   k: []
// };
// hasPath(graph, 'i', 'h'); // true
// test_03:
// const graph = {
//   v: ['x', 'w'],
//   w: [],
//   x: [],
//   y: ['z'],
//   z: [],  
// };
// hasPath(graph, 'v', 'w'); // true
// test_04:
// const graph = {
//   v: ['x', 'w'],
//   w: [],
//   x: [],
//   y: ['z'],
//   z: [],  
// };
// hasPath(graph, 'v', 'z'); // false

// ========================= Breadth First =========================
// Time: O(e^2), Space: O(n)
const hasPath = (graph, src, dst) => {
  const queue = [src];

  while (queue.length) {
    const node = queue.shift();
    if (node === dst) return true;

    graph[node].forEach(neighbor => queue.push(neighbor));
  }

  return false;
};

// ========================= Depth First =========================
// Time: O(e), Space: O(n)
const hasPath = (graph, src, dst) => {
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
// undirectedPath(edges, 'j', 'm'); // -> true
// test_01:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
// undirectedPath(edges, 'm', 'j'); // -> true
// test_02:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
// undirectedPath(edges, 'l', 'j'); // -> true
// test_03:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
// undirectedPath(edges, 'k', 'o'); // -> false
// test_04:
// const edges = [
//   ['i', 'j'],
//   ['k', 'i'],
//   ['m', 'k'],
//   ['k', 'l'],
//   ['o', 'n']
// ];
// undirectedPath(edges, 'i', 'o'); // -> false
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
// undirectedPath(edges, 'a', 'b'); // -> true
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
// undirectedPath(edges, 'a', 'c'); // -> true
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
// undirectedPath(edges, 'r', 't'); // -> true
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
// undirectedPath(edges, 'r', 'b'); // -> false

// ========================= Depth First =========================
// Time: O(e), Space: O(n)
const undirectedPath = (edges, nodeA, nodeB) => {
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

// Time: O(e), Space: O(n)
const validPath = (graph, nodeA, nodeB, visited = new Set()) => {
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
// test_01:
// connectedComponentsCount({
//   1: [2],
//   2: [1,8],
//   6: [7],
//   9: [8],
//   7: [6, 8],
//   8: [9, 7, 2]
// }); // -> 1
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
// test_03:
// connectedComponentsCount({}); // -> 0
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
// Time: O(e), Space: O(n)
const connectedComponentsCount = (graph) => {
  let count = 0;
  
  const visited = new Set();
  for (let node in graph) {
    if (exploreComponent(graph, node, visited) === true) count++;
  }
  
  return count;
};

// Time: O(e), Space: O(n)
const exploreComponent = (graph, node, visited) => {
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
// test_01:
// largestComponent({
//   1: ['2'],
//   2: ['1','8'],
//   6: ['7'],
//   9: ['8'],
//   7: ['6', '8'],
//   8: ['9', '7', '2']
// }); // -> 6
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
// test_03:
// largestComponent({}); // -> 0
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
// Time: O(e), Space: O(n)
const largestComponent = (graph) => {
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
// shortestPath(edges, 'w', 'z'); // -> 2
// test_01:
// const edges = [
//   ['w', 'x'],
//   ['x', 'y'],
//   ['z', 'y'],
//   ['z', 'v'],
//   ['w', 'v']
// ];
// shortestPath(edges, 'y', 'x'); // -> 1
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
// shortestPath(edges, 'a', 'e'); // -> 3
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
// shortestPath(edges, 'e', 'c'); // -> 2
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
// shortestPath(edges, 'b', 'g'); // -> -1
// test_05:
// const edges = [
//   ['c', 'n'],
//   ['c', 'e'],
//   ['c', 's'],
//   ['c', 'w'],
//   ['w', 'e'],
// ];
// shortestPath(edges, 'w', 'e'); // -> 1
// test_06:
// const edges = [
//   ['c', 'n'],
//   ['c', 'e'],
//   ['c', 's'],
//   ['c', 'w'],
//   ['w', 'e'],
// ];
// shortestPath(edges, 'n', 'e'); // -> 2
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
// shortestPath(edges, 'm', 's'); // -> 6

// ========================= Breadth First =========================
// Time: O(e), Space: O(n)
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

// [[[[[[[[[[[[[[[[[[[[[[[[[ #43 island count ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, islandCount, that takes in a grid containing Ws and Ls. W 
// represents water and L represents land. The function should return the number
// of islands on the grid. An island is a vertically or horizontally connected 
// region of land.
//
// test_00:
// const grid = [
//   ['W', 'L', 'W', 'W', 'W'],
//   ['W', 'L', 'W', 'W', 'W'],
//   ['W', 'W', 'W', 'L', 'W'],
//   ['W', 'W', 'L', 'L', 'W'],
//   ['L', 'W', 'W', 'L', 'L'],
//   ['L', 'L', 'W', 'W', 'W'],
// ];
// islandCount(grid); // -> 3
// test_01:
// const grid = [
//   ['L', 'W', 'W', 'L', 'W'],
//   ['L', 'W', 'W', 'L', 'L'],
//   ['W', 'L', 'W', 'L', 'W'],
//   ['W', 'W', 'W', 'W', 'W'],
//   ['W', 'W', 'L', 'L', 'L'],
// ];
// islandCount(grid); // -> 4
// test_02:
// const grid = [
//   ['L', 'L', 'L'],
//   ['L', 'L', 'L'],
//   ['L', 'L', 'L'],
// ];
// islandCount(grid); // -> 1
// test_03:
// const grid = [
//   ['W', 'W'],
//   ['W', 'W'],
//   ['W', 'W'],
// ];
// islandCount(grid); // -> 0

// ========================= Breadth First =========================
const islandCount = (grid) => {
  const visited = new Set();
  let count = 0;

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid.length; c++) {
      if (grid[r][c] === 'L' && exploreLand(grid, r, c, visited)) {
        count++;
      } 
    }
  }
  
  return count;
};

const exploreLand = (grid, r, c, visited) => {
  if (visited.has(`${r}-${c}`)) return false;
  const queue = [`${r}-${c}`];

  while (queue.length) {
    const land = queue.shift();
    visited.add(land);
    const [ r, c ] = land.split('-').map(n => parseInt(n));

    if (grid[r - 1] && grid[r - 1][c] === 'L' && !visited.has(`${r - 1}-${c}`)) {
      queue.push(`${r - 1}-${c}`);
    }
    if (grid[r][c + 1] === 'L' && !visited.has(`${r}-${c + 1}`)) {
      queue.push(`${r}-${c + 1}`);
    }
    if (grid[r + 1] && grid[r + 1][c] === 'L' && !visited.has(`${r + 1}-${c}`)) {
      queue.push(`${r + 1}-${c}`);
    }
    if (grid[r][c - 1] === 'L' && !visited.has(`${r}-${c - 1}`)) {
      queue.push(`${r}-${c - 1}`);
    }
  }

  return true
};

// ========================= Depth First =========================
// Time: O(rc), Space: O(rc)
const islandCount = (grid) => {
  const visited = new Set();
  let count = 0;

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === 'L' && exploreLand(grid, r, c, visited)) {
        count++;
      }
    }
  }

  return count;
};

const exploreLand = (grid, r, c, visited) => {
  if (grid[r][c] === 'W') return false;
  if (visited.has(`${r}-${c}`)) return false;
  
  visited.add(`${r}-${c}`);

  if (grid[r - 1] && grid[r - 1][c]) {
    exploreLand(grid, r - 1, c, visited);
  }
  if (grid[r][c + 1]) {
    exploreLand(grid, r, c + 1, visited);
  }
  if (grid[r + 1] && grid[r + 1][c]) {
    exploreLand(grid, r + 1, c, visited);
  }
  if (grid[r][c - 1]) {
    exploreLand(grid, r, c - 1, visited);
  }

  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #44 minimum island ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, minimumIsland, that takes in a grid containing Ws and Ls. 
// W represents water and L represents land. The function should return the size
// of the smallest island. An island is a vertically or horizontally connected 
// region of land.
// You may assume that the grid contains at least one island.
//
// test_00:
// const grid = [
//   ['W', 'L', 'W', 'W', 'W'],
//   ['W', 'L', 'W', 'W', 'W'],
//   ['W', 'W', 'W', 'L', 'W'],
//   ['W', 'W', 'L', 'L', 'W'],
//   ['L', 'W', 'W', 'L', 'L'],
//   ['L', 'L', 'W', 'W', 'W'],
// ];
// minimumIsland(grid); // -> 2
// test_01:
// const grid = [
//   ['L', 'W', 'W', 'L', 'W'],
//   ['L', 'W', 'W', 'L', 'L'],
//   ['W', 'L', 'W', 'L', 'W'],
//   ['W', 'W', 'W', 'W', 'W'],
//   ['W', 'W', 'L', 'L', 'L'],
// ];
// minimumIsland(grid); // -> 1
// test_02:
// const grid = [
//   ['L', 'L', 'L'],
//   ['L', 'L', 'L'],
//   ['L', 'L', 'L'],
// ];
// minimumIsland(grid); // -> 9
// test_03:
// const grid = [
//   ['W', 'W'],
//   ['L', 'L'],
//   ['W', 'W'],
//   ['W', 'L']
// ];
// minimumIsland(grid); // -> 1

// ========================= Depth First =========================
// Time: O(rc), Space: O(rc)
const minimumIsland = (grid) => {
  const visited = new Set();
  let smallestSize = Infinity;

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid.length; c++) {
      if (grid[r][c] === 'L' && !visited.has(`${r}-${c}`)) {
        const currentSize = landSize(grid, r, c, visited);
        if (currentSize < smallestSize) smallestSize = currentSize;
      }
    }
  }

  return smallestSize;
};

const landSize = (grid, r, c, visited) => {
  if (grid[r][c] === 'W') return 0;
  if (visited.has(`${r}-${c}`)) return 0;

  visited.add(`${r}-${c}`);

  let count = 1;
  if (grid[r - 1] && grid[r - 1][c]) {
    count += landSize(grid, r - 1, c, visited);
  }
  if (grid[r] && grid[r][c + 1]) {
    count += landSize(grid, r, c + 1, visited);
  }
  if (grid[r + 1] && grid[r + 1][c]) {
    count += landSize(grid, r + 1, c, visited);
  }
  if (grid[r] && grid[r][c - 1]) {
    count += landSize(grid, r, c - 1, visited);
  }

  return count;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #45 closest carrot ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, closestCarrot, that takes in a grid, a starting row, and a 
// starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's 
// are carrots. The function should return a number representing the length of 
// the shortest path from the starting position to a carrot. You may move up, 
// down, left, or right, but cannot pass through walls (X). If there is no 
// possible path to a carrot, then return -1.
// 
//
// test_00:
// const grid = [
//   ['O', 'O', 'O', 'O', 'O'],
//   ['O', 'X', 'O', 'O', 'O'],
//   ['O', 'X', 'X', 'O', 'O'],
//   ['O', 'X', 'C', 'O', 'O'],
//   ['O', 'X', 'X', 'O', 'O'],
//   ['C', 'O', 'O', 'O', 'O'],
// ];
// 
// closestCarrot(grid, 1, 2); // -> 4
// test_01:
// const grid = [
//   ['O', 'O', 'O', 'O', 'O'],
//   ['O', 'X', 'O', 'O', 'O'],
//   ['O', 'X', 'X', 'O', 'O'],
//   ['O', 'X', 'C', 'O', 'O'],
//   ['O', 'X', 'X', 'O', 'O'],
//   ['C', 'O', 'O', 'O', 'O'],
// ];
// 
// closestCarrot(grid, 0, 0); // -> 5
// test_02:
// const grid = [
//   ['O', 'O', 'X', 'X', 'X'],
//   ['O', 'X', 'X', 'X', 'C'],
//   ['O', 'X', 'O', 'X', 'X'],
//   ['O', 'O', 'O', 'O', 'O'],
//   ['O', 'X', 'X', 'X', 'X'],
//   ['O', 'O', 'O', 'O', 'O'],
//   ['O', 'O', 'C', 'O', 'O'],
//   ['O', 'O', 'O', 'O', 'O'],
// ];
// 
// closestCarrot(grid, 3, 4); // -> 9
// test_03:
// const grid = [
//   ['O', 'O', 'X', 'O', 'O'],
//   ['O', 'X', 'X', 'X', 'O'],
//   ['O', 'X', 'C', 'C', 'O'],
// ];
// 
// closestCarrot(grid, 1, 4); // -> 2
// test_04:
// const grid = [
//   ['O', 'O', 'X', 'O', 'O'],
//   ['O', 'X', 'X', 'X', 'O'],
//   ['O', 'X', 'C', 'C', 'O'],
// ];
// 
// closestCarrot(grid, 2, 0); // -> -1

// ========================= Breadth First =========================
// Time: O(rc), Space: O(rc)
const closestCarrot = (grid, startRow, startCol) => {
  const visited = new Set();
  const queue = [{ row: startRow, col: startCol, distance: 0 }];
  const deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]];

  while (queue.length) {
    const { row, col, distance } = queue.shift();
    visited.add(`${row}-${col}`);

    if (grid[row][col] === 'C') return distance;

    for (let delta of deltas) {
      const [ r, c ] = delta;
      const newRow = row + r;
      const newCol = col + c;
      const validRow = newRow >= 0 && newRow < grid.length;
      const validCol = newCol >= 0 && newCol < grid[0].length;

      if (validRow && validCol && grid[newRow][newCol] !== 'X' && !visited.has(`${newRow}-${newCol}`)) {
        queue.push({ row: newRow, col: newCol, distance: distance + 1 });
      }
    }
  }

  return -1;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #46 longest path ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, longestPath, that takes in an adjacency list for a directed
// acyclic graph. The function should return the length of the longest path 
// within the graph. A path may start and end at any two nodes. The length of a
// path is considered the number of edges in the path, not the number of nodes.
//
// test_00:
// const graph = {
//   a: ['c', 'b'],
//   b: ['c'],
//   c: []
// };
// longestPath(graph); // -> 2
// test_01:
// const graph = {
//   a: ['c', 'b'],
//   b: ['c'],
//   c: [],
//   q: ['r'],
//   r: ['s', 'u', 't'],
//   s: ['t'],
//   t: ['u'],
//   u: []
// };
// longestPath(graph); // -> 4
// test_02:
// const graph = {
//   h: ['i', 'j', 'k'],
//   g: ['h'],
//   i: [],
//   j: [],
//   k: [],
//   x: ['y'],
//   y: []
// };
// longestPath(graph); // -> 2
// test_03:
// const graph = {
//   a: ['b'],
//   b: ['c'],
//   c: [],
//   e: ['f'],
//   f: ['g'],
//   g: ['h'],
//   h: []
// };
// longestPath(graph); // -> 3

// ========================= Depth First =========================
const longestPath = (graph) => {
  let longest = -Infinity;

  for (let start in graph) {
    const length = pathLength(graph, start);
    if (length > longest) longest = length;
  }

  return longest;
};

const pathLength = (graph, start) => {
  if (!graph[start].length) return 0;

  const lengths = [];
  for (let neighbor of graph[start]) {
    lengths.push(pathLength(graph, neighbor));
  }

  return 1 + Math.max(...lengths);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #47 semesters required ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, semestersRequired, that takes in a number of courses (n) and
// a list of prerequisites as arguments. Courses have ids ranging from 0 through
// n - 1. A single prerequisite of [A, B] means that course A must be taken 
// before course B. Return the minimum number of semesters required to complete
// all n courses. There is no limit on how many courses you can take in a single
// semester, as long the prerequisites of a course are satisfied before taking it.
// Note that given prerequisite [A, B], you cannot take course A and course B
// concurrently in the same semester. You must take A in some semester before B.
// You can assume that it is possible to eventually complete all courses.
//
// test_00:
// const numCourses = 6;
// const prereqs = [
//   [1, 2],
//   [2, 4],
//   [3, 5],
//   [0, 5],
// ];
// semestersRequired(numCourses, prereqs); // -> 3
// test_01:
// const numCourses = 7;
// const prereqs = [
//   [4, 3],
//   [3, 2],
//   [2, 1],
//   [1, 0],
//   [5, 2],
//   [5, 6],
// ];
// semestersRequired(numCourses, prereqs); // -> 5
// test_02:
// const numCourses = 5;
// const prereqs = [
//   [1, 0],
//   [3, 4],
//   [1, 2],
//   [3, 2],
// ];
// semestersRequired(numCourses, prereqs); // -> 2
// test_03:
// const numCourses = 12;
// const prereqs = [];
// semestersRequired(numCourses, prereqs); // -> 1
// test_04:
// const numCourses = 3;
// const prereqs = [
//   [0, 2],
//   [0, 1],
//   [1, 2],
// ];
// semestersRequired(numCourses, prereqs); // -> 3
// test_05:
// const numCourses = 6;
// const prereqs = [
//   [3, 4],
//   [3, 0],
//   [3, 1],
//   [3, 2],
//   [3, 5],
// ];
// semestersRequired(numCourses, prereqs); // -> 2

// ========================= Depth First =========================
// Time: O(p), Space: O(c)
const semestersRequired = (numCourses, prereqs) => {
  const graph = buildGraph(prereqs);
  let semsNeeded = 1;

  for (let course in graph) {
    const numSems = semesters(graph, course);
    if (numSems > semsNeeded) semsNeeded = numSems
  }

  return semsNeeded;
};

const buildGraph = (prereqs) => {
  const graph = {};

  for (let prereq of prereqs) {
    const [ pre, post ] = prereq;

    if (!graph[pre]) graph[pre] = [];
    graph[pre].push(post);
  }

  return graph;
};

const semesters = (graph, course) => {
  if (!graph[course]) return 1;

  let numSems = [];
  for (let postreq of graph[course]) {
    numSems.push(semesters(graph, postreq))
  }

  return 1 + Math.max(...numSems);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #48 best bridge ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, bestBridge, that takes in a grid as an argument. The grid 
// contains water (W) and land (L). There are exactly two islands in the grid. 
// An island is a vertically or horizontally connected region of land. Return 
// the minimum length bridge needed to connect the two islands. A bridge does not
// need to form a straight line.
//
// test_00:
// const grid = [
//   ["W", "W", "W", "L", "L"],
//   ["L", "L", "W", "W", "L"],
//   ["L", "L", "L", "W", "L"],
//   ["W", "L", "W", "W", "W"],
//   ["W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W"],
// ];
// bestBridge(grid); // -> 1
// test_01:
// const grid = [
//   ["W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W"],
//   ["L", "L", "W", "W", "L"],
//   ["W", "L", "W", "W", "L"],
//   ["W", "W", "W", "L", "L"],
//   ["W", "W", "W", "W", "W"],
// ];
// bestBridge(grid); // -> 2
// test_02:
// const grid = [
//   ["W", "W", "W", "W", "W"],
//   ["W", "W", "W", "L", "W"],
//   ["L", "W", "W", "W", "W"],
// ];
// bestBridge(grid); // -> 3
// test_03:
// const grid = [
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "L", "W", "W"],
//   ["W", "W", "W", "W", "L", "L", "W", "W"],
//   ["W", "W", "W", "W", "L", "L", "L", "W"],
//   ["W", "W", "W", "W", "W", "L", "L", "L"],
//   ["L", "W", "W", "W", "W", "L", "L", "L"],
//   ["L", "L", "L", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
// ];
// bestBridge(grid); // -> 3
// test_04:
// const grid = [
//   ["L", "L", "L", "L", "L", "L", "L", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "L", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "W", "W", "W", "W", "W", "W", "L"],
//   ["L", "L", "L", "L", "L", "L", "L", "L"],
// ];
// bestBridge(grid); // -> 2
// test_05:
// const grid = [
//   ["W", "L", "W", "W", "W", "W", "W", "W"],
//   ["W", "L", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "W", "W"],
//   ["W", "W", "W", "W", "W", "W", "L", "W"],
//   ["W", "W", "W", "W", "W", "W", "L", "L"],
//   ["W", "W", "W", "W", "W", "W", "W", "L"],
// ];
// bestBridge(grid); // -> 8

// ========================= My Solution (Breadth First; Slower than Alvin's) =========================
const bestBridge = (grid) => {
  const visited = new Set();
  let island = [];
  let length = 0;
  
  outerLoop:
  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      if (grid[r][c] === 'L') {
        island = recordLand(grid, visited, r, c);
        length = bridgeLength(grid, visited, island);
        break outerLoop;
      }
    }
  }

  return length;
};

const recordLand = (grid, visited, row, col) => {
  const island = [[row, col]];
  const queue = [[row, col]];
  const deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]];

  while (queue.length) {
    const [r, c] = queue.shift();
    visited.add(`${r}-${c}`);

    for (let delta of deltas) {
      const [y, x] = delta;
      const newRow = r + y;
      const newCol = c + x;
      const validY = newRow >= 0 && newRow < grid.length;
      const validX = newCol >= 0 && newCol < grid[0].length;

      if (validY && validX && grid[newRow][newCol] === 'L' && 
          !visited.has(`${newRow}-${newCol}`)) {
        queue.push([newRow, newCol]);
        island.push([newRow, newCol]);
      }
    }
  }
  
  return island;
};

const bridgeLength = (grid, visited, island) => {
  let minLength = Infinity;
  
  for (let landPos of island) {
    let visitedWater = new Set(visited);
    const queue = [{ pos: landPos, distance: -1 }];
    
    while (queue.length) {
      const { pos, distance } = queue.shift();
      const [r, c] = pos;
      visitedWater.add(`${r}-${c}`);
      
      if (grid[r][c] === 'L' && !visited.has(`${r}-${c}`)) {
        const currLength = distance;
        if (currLength < minLength) minLength = currLength;
      } else {
        const deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]];

        for (let delta of deltas) {
          const [y, x] = delta;
          const newRow = r + y;
          const newCol = c + x;
          const validY = newRow >= 0 && newRow < grid.length;
          const validX = newCol >= 0 && newCol < grid[0].length;
    
          if (validY && validX && !visitedWater.has(`${newRow}-${newCol}`)) {
            queue.push({ pos: [newRow, newCol], distance: distance + 1 });
          }
        }
      }
    }
  }

  return minLength;
};

// ========================= Depth & Breadth First =========================
// Time: O(rc), Space: O(rc)
const bestBridge = (grid) => {
  let mainIsland;
  for (let r = 0; r < grid.length; r += 1) {
    for (let c = 0; c < grid[0].length; c += 1) {
      const possibleIsland = traverseIsland(grid, r, c, new Set());
      if (possibleIsland.size > 0) {
        mainIsland = possibleIsland;
        break;
      }
    }
  }
  
  const visited = new Set(mainIsland);
  const queue = [];
  for (let pos of mainIsland) {
    const [ row, col ] = pos.split(',').map(Number);
    queue.push([row, col, 0]);
  }
  
  while (queue.length > 0) {
    const [ row, col, distance ] = queue.shift();
    
    const pos = row + ',' + col;
    if (grid[row][col] === 'L' && !mainIsland.has(pos)) return distance - 1;
    
    const deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    for (let delta of deltas) {
      const [ deltaRow, deltaCol ] = delta;
      const neighborRow = row + deltaRow;
      const neighborCol = col + deltaCol;
      const neighborPos = neighborRow + ',' + neighborCol;
      if (isInbounds(grid, neighborRow, neighborCol) && !visited.has(neighborPos)) {
        visited.add(neighborPos);
        queue.push([neighborRow, neighborCol, distance + 1]);
      }
    }
  }
};

const isInbounds = (grid, row, col) => {
  const rowInbounds = 0 <= row  && row < grid.length;
  const colInbounds = 0 <= col && col < grid[0].length;
  return rowInbounds && colInbounds;
};

const traverseIsland = (grid, row, col, visited) => {
  if (!isInbounds(grid, row, col) || grid[row][col] === 'W') return visited;
  
  const pos = row + ',' + col;
  if (visited.has(pos)) return visited;
  
  visited.add(pos);
  
  traverseIsland(grid, row - 1, col, visited);
  traverseIsland(grid, row + 1, col, visited);
  traverseIsland(grid, row, col - 1, visited);
  traverseIsland(grid, row, col + 1, visited);
  
  return visited;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #49 has cycle ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, hasCycle, that takes in an object representing the adjacency
// list of a directed graph. The function should return a boolean indicating 
// whether or not the graph contains a cycle.
//
// test_00:
// hasCycle({
//   a: ["b"],
//   b: ["c"],
//   c: ["a"],
// }); // -> true
// test_01:
// hasCycle({
//   a: ["b", "c"],
//   b: ["c"],
//   c: ["d"],
//   d: [],
// }); // -> false
// test_02:
// hasCycle({
//   a: ["b", "c"],
//   b: [],
//   c: [],
//   e: ["f"],
//   f: ["e"],
// }); // -> true
// test_03:
// hasCycle({
//   q: ["r", "s"],
//   r: ["t", "u"],
//   s: [],
//   t: [],
//   u: [],
//   v: ["w"],
//   w: [],
//   x: ["w"],
// }); // -> false
// test_04:
// hasCycle({
//   a: ["b"],
//   b: ["c"],
//   c: ["a"],
//   g: [],
// }); // -> true

// ========================= White-gray-black (DFS) =========================
// Time: O(e), Space: O(n)
const hasCycle = (graph) => {
  const visited = new Set();

  for (let node in graph) {
    if (inCycle(graph, node, visited)) return true;
  }

  return false;
};

const inCycle = (graph, node, visited, visiting = new Set()) => {
  if (visited.has(node)) return false;
  if (visiting.has(node)) return true;

  visiting.add(node);
  for (let neighbor of graph[node]) {
    if (inCycle(graph, neighbor, visited, visiting)) return true;
  }

  visiting.delete(node);
  visited.add(node);
  return false;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #50 prereqs possible ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, prereqsPossible, that takes in a number of courses (n) and
// prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A
// single prerequisite of [A, B] means that course A must be taken before course
// B. The function should return a boolean indicating whether or not it is
// possible to complete all courses.
// 
//
// test_00:
// const numCourses = 6;
// const prereqs = [
//   [0, 1],
//   [2, 3],
//   [0, 2],
//   [1, 3],
//   [4, 5],
// ];
// prereqsPossible(numCourses, prereqs); // -> true
// test_01:
// const numCourses = 6;
// const prereqs = [
//   [0, 1],
//   [2, 3],
//   [0, 2],
//   [1, 3],
//   [4, 5],
//   [3, 0],
// ];
// prereqsPossible(numCourses, prereqs); // -> false
// test_02:
// const numCourses = 5;
// const prereqs = [
//   [2, 4],
//   [1, 0],
//   [0, 2],
//   [0, 4],
// ];
// prereqsPossible(numCourses, prereqs); // -> true
// test_03:
// const numCourses = 6;
// const prereqs = [
//   [2, 4],
//   [1, 0],
//   [0, 2],
//   [0, 4],
//   [5, 3],
//   [3, 5],
// ];
// prereqsPossible(numCourses, prereqs); // -> false
// test_04:
// const numCourses = 8;
// const prereqs = [
//   [1, 0],
//   [0, 6],
//   [2, 0],
//   [0, 5],
//   [3, 7],
//   [4, 3],
// ];
// prereqsPossible(numCourses, prereqs); // -> true
// test_05:
// const numCourses = 8;
// const prereqs = [
//   [1, 0],
//   [0, 6],
//   [2, 0],
//   [0, 5],
//   [3, 7],
//   [7, 4],
//   [4, 3],
// ];
// prereqsPossible(numCourses, prereqs); // -> false
// test_06:
// const numCourses = 42;
// const prereqs = [[6, 36]];
// prereqsPossible(numCourses, prereqs); // -> true

// ========================= White-gray-black (DFS) =========================
// Time: O(p), Space: O(p)
const prereqsPossible = (numCourses, prereqs) => {
  const graph = buildGraph(prereqs);
  const visited = new Set();

  for (let course in graph) {
    if (inCycle(graph, visited, course)) return false;
  }
  
  return true;
};

const buildGraph = (prereqs) => {
  const graph = {};

  for (let prereq of prereqs) {
    const [ pre, post ] = prereq;

    if (!graph[pre]) graph[pre] = [];
    graph[pre].push(post);
  }

  return graph;
};

const inCycle = (graph, visited, course, visiting = new Set()) => {
  if (visiting.has(course)) return true;
  if (visited.has(course)) return false;
  if (graph[course] === undefined) return false;

  visiting.add(course);
  for (let nextCourse of graph[course]) {
    if (inCycle(graph, visited, nextCourse, visiting)) return true;
  }

  visiting.delete(course);
  visited.add(course);
  return false;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #51 fib ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function fib that takes in a number argument, n, and returns the n-th
// number of the Fibonacci sequence.
// The 0-th number of the sequence is 0.
// The 1-st number of the sequence is 1.
// To generate further numbers of the sequence, calculate the sum of previous two numbers.
// Solve this recursively.
// 
//
// test_00:
// fib(0); // -> 0
// test_01:
// fib(1); // -> 1
// test_02:
// fib(2); // -> 1
// test_03:
// fib(3); // -> 2
// test_04:
// fib(4); // -> 3
// test_05:
// fib(5); // -> 5
// test_06:
// fib(35); // -> 9227465
// test_07:
// fib(46); // -> 1836311903

// ========================= Memoization =========================
// Time: O(n), Space: O(n)
const fib = (n, memo = {}) => {
  if (n === 0) return 0;
  if (n === 1) return 1;
  if (n in memo) return memo[n];

  memo[n] = fib(n - 1) + fib(n - 2);

  return memo[n];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #52 tribonacci ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function tribonacci that takes in a number argument, n, and returns
// the n-th number of the Tribonacci sequence.
// The 0-th and 1-st numbers of the sequence are both 0.
// The 2-nd number of the sequence is 1.
// To generate further numbers of the sequence, calculate the sum of previous three numbers.
// Solve this recursively.
//
// test_00:
// tribonacci(0); // -> 0
// test_01:
// tribonacci(1); // -> 0
// test_02:
// tribonacci(2); // -> 1
// test_03:
// tribonacci(5); // -> 4
// test_04:
// tribonacci(7); // -> 13
// test_05:
// tribonacci(14); // -> 927
// test_06:
// tribonacci(20); // -> 35890
// test_07:
// tribonacci(37); // -> 1132436852

// ========================= Memoization =========================
// Time: O(n), Space: O(n)
const tribonacci = (n, memo = {}) => {
  if (n === 0 || n === 1) return 0;
  if (n === 2) return 1;
  if (n in memo) return memo[n];

  memo[n] = tribonacci(n - 1, memo) + tribonacci(n - 2, memo) + tribonacci(n - 3, memo);

  return memo[n];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #53 sum possible ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function sumPossible that takes in an amount and an array of positive
// numbers. The function should return a boolean indicating whether or not it is
// possible to create the amount by summing numbers of the array. You may reuse
// numbers of the array as many times as necessary.
// You may assume that the target amount is non-negative.
//
// test_00:
// sumPossible(8, [5, 12, 4]); // -> true, 4 + 4
// test_01:
// sumPossible(15, [6, 2, 10, 19]); // -> false
// test_02:
// sumPossible(13, [6, 2, 1]); // -> true
// test_03:
// sumPossible(103, [6, 20, 1]); // -> true
// test_04:
// sumPossible(12, []); // -> false
// test_05:
// sumPossible(12, [12]); // -> true
// test_06:
// sumPossible(0, []); // -> true
// test_07:
// sumPossible(271, [10, 8, 265, 24]); // -> false
// test_08:
// sumPossible(2017, [4, 2, 10]); // -> false

// ========================= Memoization =========================
// Time: O(a*n), Space: O(n)
const sumPossible = (amount, numbers, memo = {}) => {
  if (amount === 0) return true;
  if (amount in memo) return memo[amount];
  
  memo[amount] = false;
  for (let num of numbers) {
    if (num <= amount && sumPossible(amount - num, numbers, memo)) {
      memo[amount] = true;
    }
  }

  return memo[amount];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #54 min change ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function minChange that takes in an amount and an array of coins. The
// function should return the minimum number of coins required to create the
// amount. You may use each coin as many times as necessary.
// If it is not possible to create the amount, then return -1.
//
// test_00:
// minChange(8, [1, 5, 4, 12]); // -> 2, because 4+4 is the minimum coins possible
// test_01:
// minChange(13, [1, 9, 5, 14, 30]); // -> 5
// test_02:
// minChange(23, [2, 5, 7]); // -> 4
// test_03:
// minChange(102, [1, 5, 10, 25]); // -> 6
// test_04:
// minChange(200, [1, 5, 10, 25]); // -> 8
// test_05:
// minChange(2017, [4, 2, 10]); // -1
// test_06:
// minChange(271, [10, 8, 265, 24]); // -1
// test_07:
// minChange(0, [4, 2, 10]); // 0
// test_08:
// minChange(0, [])); // 0

// ========================= Memoization =========================
// Time: O(a*c), Space: O(c)
const minChange = (amount, coins) => {
  const min = _minChange(amount, coins);
  return min === Infinity ? -1 : min;
};

const _minChange = (amount, coins, memo = {}) => {
  if (amount === 0) return 0;
  if (amount in memo) return memo[amount];

  let min = Infinity;
  for (let coin of coins) {
    if (coin <= amount) {
      const numCoins = _minChange(amount - coin, coins, memo) + 1;
      min = Math.min(numCoins, min);
    }
  }

  return memo[amount] = min;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #55 count paths ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, countPaths, that takes in a grid as an argument. In the grid,
// 'X' represents walls and 'O' represents open spaces. You may only move down or
// to the right and cannot pass through walls. The function should return the
// number of ways possible to travel from the top-left corner of the grid to the
// bottom-right corner.
//
// test_00:
// const grid = [
//   ["O", "O"],
//   ["O", "O"],
// ];
// countPaths(grid); // -> 2
// test_01:
// const grid = [
//   ["O", "O", "X"],
//   ["O", "O", "O"],
//   ["O", "O", "O"],
// ];
// countPaths(grid); // -> 5
// test_02:
// const grid = [
//   ["O", "O", "O"],
//   ["O", "O", "X"],
//   ["O", "O", "O"],
// ];
// countPaths(grid); // -> 3
// test_03:
// const grid = [
//   ["O", "O", "O"],
//   ["O", "X", "X"],
//   ["O", "O", "O"],
// ];
// countPaths(grid); // -> 1
// test_04:
// const grid = [
//   ["O", "O", "X", "O", "O", "O"],
//   ["O", "O", "X", "O", "O", "O"],
//   ["X", "O", "X", "O", "O", "O"],
//   ["X", "X", "X", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O"],
// ];
// countPaths(grid); // -> 0
// test_05:
// const grid = [
//   ["O", "O", "X", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "X"],
//   ["X", "O", "O", "O", "O", "O"],
//   ["X", "X", "X", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O"],
// ];
// countPaths(grid); // -> 42
// test_06:
// const grid = [
//   ["O", "O", "X", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "X"],
//   ["X", "O", "O", "O", "O", "O"],
//   ["X", "X", "X", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "X"],
// ];
// countPaths(grid); // -> 0
// test_07:
// const grid = [
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
// ];
// countPaths(grid); // -> 40116600
// test_08:
// const grid = [
//   ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
//   ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
//   ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
//   ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
//   ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
// ];
// countPaths(grid); // -> 3190434

// ========================= Memoization =========================
// Time: O(r*c), Space: O(r*c)
const countPaths = (grid, r = 0, c = 0, memo = {}) => {
  const pos = `${r}-${c}`;
  if (pos in memo) return memo[pos];
  if (grid[grid.length - 1][grid[0].length - 1] === 'X') return 0;
  if (r === grid.length || c === grid[0].length || grid[r][c] === 'X') return 0;
  if (r === grid.length - 1 && c === grid[0].length - 1) return 1;

  memo[pos] = countPaths(grid, r + 1, c, memo) + countPaths(grid, r, c + 1, memo);
  return memo[pos];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #56 max path sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, maxPathSum, that takes in a grid as an argument. The
// function should return the maximum sum possible by traveling a path from the
// top-left corner to the bottom-right corner. You may only travel through the
// grid by moving down or right.
//
// test_00:
// const grid = [
//   [1, 3, 12],
//   [5, 1, 1],
//   [3, 6, 1],
// ];
// maxPathSum(grid); // -> 18
// test_01:
// const grid = [
//   [1, 2, 8, 1],
//   [3, 1, 12, 10],
//   [4, 0, 6, 3],
// ];
// maxPathSum(grid); // -> 36
// test_02:
// const grid = [
//   [1, 2, 8, 1],
//   [3, 10, 12, 10],
//   [4, 0, 6, 3],
// ];
// maxPathSum(grid); // -> 39
// test_03:
// const grid = [
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
// ];
// maxPathSum(grid); // -> 27
// test_04:
// const grid = [
//   [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
//   [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
//   [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
//   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
// ];
// maxPathSum(grid); // -> 56

// ========================= Memoization =========================
// Time: O(r*c), Space: O(r*c)
const maxPathSum = (grid, r = 0, c = 0, memo = {}) => {
  const pos = `${r}-${c}`;
  if (pos in memo) return memo[pos];
  if (r === grid.length || c === grid[0].length) return 0;
  if (r === grid.length - 1 && c === grid[0].length - 1) return grid[r][c];

  const rightPath = maxPathSum(grid, r, c + 1, memo);
  const downPath = maxPathSum(grid, r + 1, c, memo);
  memo[pos] = grid[r][c] + Math.max(rightPath, downPath);

  return memo[pos];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #57 non adjacent sum ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, nonAdjacentSum, that takes in an array of numbers as an
// argument. The function should return the maximum sum of non-adjacent elements
// in the array. There is no limit on how many elements can be taken into the sum
// as long as they are not adjacent.
// For example, given:
// [2, 4, 5, 12, 7]
// The maximum non-adjacent sum is 16, because 4 + 12. 
// 4 and 12 are not adjacent in the array.
//
// test_00:
// const nums = [2, 4, 5, 12, 7];
// nonAdjacentSum(nums); // -> 16
// test_01:
// const nums = [7, 5, 5, 12];
// nonAdjacentSum(nums); // -> 19
// test_02:
// const nums = [7, 5, 5, 12, 17, 29];
// nonAdjacentSum(nums); // -> 48
// test_03:
// const nums = [
//   72, 62, 10,  6, 20, 19, 42,
//   46, 24, 78, 30, 41, 75, 38,
//   23, 28, 66, 55, 12, 17, 9,
//   12, 3, 1, 19, 30, 50, 20
// ];
// nonAdjacentSum(nums); // -> 488
// test_04:
// const nums = [
//   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
//   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
//   83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
//   61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
//   30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
//   72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
//   42
// ];
// nonAdjacentSum(nums); // -> 1465

// ========================= Memoization =========================
// Time: O(n), Space: O(n)
const nonAdjacentSum = (nums, i = 0, memo = {}) => {
  if (i >= nums.length) return 0;
  if (i in memo) return memo[i];

  const include = nums[i] + nonAdjacentSum(nums, i + 2, memo);
  const exclude = nonAdjacentSum(nums, i + 1, memo);
  memo[i] = Math.max(include, exclude);

  return memo[i];
};

// ========================= Greedy (not guaranteed) =========================
// const nonAdjacentSum = (nums) => {
//   if (!nums.length) return 0;

//   const max = Math.max(...nums);
//   const maxIdx = nums.indexOf(max);
//   const spliceIdx = maxIdx === 0 ? 0 : maxIdx - 1;

//   nums.splice(spliceIdx, 3);
//   return max + nonAdjacentSum(nums);
// };

// [[[[[[[[[[[[[[[[[[[[[[[[[ #58 summing squares ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, summingSquares, that takes a target number as an argument.
// The function should return the minimum number of perfect squares that sum to
// the target. A perfect square is a number of the form (i*i) where i >= 1.
// For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
// Given 12:
// summingSquares(12) -> 3
// The minimum squares required for 12 is three, by doing 4 + 4 + 4.
// Another way to make 12 is 9 + 1 + 1 + 1, but that requires four perfect squares.
//
// test_00:
// summingSquares(8); // -> 2
// test_01:
// summingSquares(9); // -> 1
// test_02:
// summingSquares(12); // -> 3
// test_03:
// summingSquares(1); // -> 1
// test_04:
// summingSquares(31); // -> 4
// test_05:
// summingSquares(50); // -> 2
// test_06:
// summingSquares(68); // -> 2
// test_07:
// summingSquares(87); // -> 4

// ========================= Memoization =========================
// Time: O(n*sqrt(n)), Space: O(n)
const summingSquares = (n, memo = {}) => {
  if (n in memo) return memo[n];

  const root = Math.sqrt(n);
  if (root === Math.floor(root)) return 1;

  let numSquares = Infinity;
  for (let i = Math.floor(root); i > 0; i--) {
    if (i**2 <= n) {
      let num = 1 + summingSquares(n - i**2, memo);
      numSquares = Math.min(num, numSquares);
    }
  }

  return memo[n] = numSquares;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #59 counting change ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, countingChange, that takes in an amount and an array of
// coins. The function should return the number of different ways it is possible
// to make change for the given amount using the coins.
// You may reuse a coin as many times as necessary.
// For example,
// countingChange(4, [1,2,3]) -> 4
// There are four different ways to make an amount of 4:
// 1. 1 + 1 + 1 + 1
// 2. 1 + 1 + 2
// 3. 1 + 3
// 4. 2 + 2
//
// test_00:
// countingChange(4, [1, 2, 3]); // -> 4
// test_01:
// countingChange(8, [1, 2, 3]); // -> 10
// test_02:
// countingChange(24, [5, 7, 3]); // -> 5
// test_03:
// countingChange(13, [2, 6, 12, 10]); // -> 0
// test_04:
// countingChange(512, [1, 5, 10, 25]); // -> 20119
// test_05:
// countingChange(1000, [1, 5, 10, 25]); // -> 142511
// test_06:
// countingChange(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]); // -> 1525987916

// ========================= Memoization =========================
// Time: O(a*c), Space: O(a*c)
const countingChange = (amount, coins, i = 0, memo = {}) => {
  const key = amount + '-' + i;
  if (key in memo) return memo[key];
  if (amount === 0) return 1;

  const coin = coins[i];
  let numWays = 0;
  for (let qty = 0; (qty * coin) <= amount; qty++) {
    const remainder = amount - (qty * coin);
    numWays += countingChange(remainder, coins, i + 1, memo);
  }

  return memo[key] = numWays;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #60 array stepper ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, arrayStepper, that takes in an array of numbers as an
// argument. You start at the first position of the array. The function should
// return a boolean indicating whether or not it is possible reach the last
// position of the array. When situated at some position of the array, you may
// take a maximum number of steps based on the number at that position.
// For example, given:
//     idx =  0  1  2  3  4  5
// numbers = [2, 4, 2, 0, 0, 1]
// The answer is true.
// We start at idx 0, we could take 1 step or 2 steps forward.
// The correct choice is to take 1 step to idx 1.
// Then take 4 steps forward to the end at idx 5.
//
// test_00:
// arrayStepper([2, 4, 2, 0, 0, 1]); // -> true
// test_01:
// arrayStepper([2, 3, 2, 0, 0, 1]); // -> false
// test_02:
// arrayStepper([3, 1, 3, 1, 0, 1]); // -> true
// test_03:
// arrayStepper([4, 1, 5, 1, 1, 1, 0, 4]); // -> true
// test_04:
// arrayStepper([4, 1, 2, 1, 1, 1, 0, 4]); // -> false
// test_05:
// arrayStepper([1, 1, 1, 1, 1, 0]); // -> true
// test_06:
// arrayStepper([1, 1, 1, 1, 0, 0]); // -> false
// test_07:
// arrayStepper([ 
//   31, 30, 29, 28, 27,
//   26, 25, 24, 23, 22,
//   21, 20, 19, 18, 17,
//   16, 15, 14, 13, 12,
//   11, 10, 9, 8, 7, 6,
//   5, 3, 2, 1, 0, 0, 0
// ]); // -> false

// ========================= Memoization =========================
// Time: O(n^2), Space: O(n)
const arrayStepper = (nums, idx = 0, memo = {}) => {
  if (idx in memo) return memo[idx];
  if (idx >= nums.length - 1) return true;

  memo[idx] = false;
  for (let i = 0; i <= nums[idx]; i++) {
    if (arrayStepper(nums, idx + i, memo)) {
      memo[idx] = true;
    }
  }

  return memo[idx];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #61 max palin subsequence ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, maxPalinSubsequence, that takes in a string as an argument.
// The function should return the length of the longest subsequence of the string
// that is also a palindrome.
// A subsequence of a string can be created by deleting any characters of the
// string, while maintaining the relative order of characters.
//
// test_00:
// maxPalinSubsequence("luwxult"); // -> 5
// test_01:
// maxPalinSubsequence("xyzaxxzy"); // -> 6
// test_02:
// maxPalinSubsequence("lol"); // -> 3
// test_03:
// maxPalinSubsequence("boabcdefop"); // -> 3
// test_04:
// maxPalinSubsequence("z"); // -> 1
// test_05:
// maxPalinSubsequence("chartreusepugvicefree"); // -> 7
// test_06:
// maxPalinSubsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty"); // -> 15
// test_07:
// maxPalinSubsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"); // -> 31

// ========================= Memoization =========================
// Time: O(n^2), Space: O(n)
const maxPalinSubsequence = (str, i = 0, j = str.length - 1, memo = {}) => {
  const key = i + '-' + j;
  if (key in memo) return memo[key];
  if (i === j) return 1;
  if (i > j) return 0;

  if (str[i] === str[j]) {
    memo[key] = 2 + maxPalinSubsequence(str, i + 1, j - 1, memo);
  } else {
    memo[key] = Math.max(
      maxPalinSubsequence(str, i + 1, j, memo),
      maxPalinSubsequence(str, i, j - 1, memo)
    );
  }

  return memo[key];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #62 overlap subsequence ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, overlapSubsequence, that takes in two strings as arguments.
// The function should return the length of the longest overlapping subsequence.
// A subsequence of a string can be created by deleting any characters of the
// string, while maintaining the relative order of characters.
//
// test_00:
// overlapSubsequence("dogs", "daogt"); // -> 3
// test_01:
// overlapSubsequence("xcyats", "criaotsi"); // -> 4
// test_02:
// overlapSubsequence("xfeqortsver", "feeeuavoeqr"); // -> 5
// test_03:
// overlapSubsequence("kinfolklivemustache", "bespokekinfolksnackwave"); // -> 11
// test_04:
// overlapSubsequence(
//   "mumblecorebeardleggingsauthenticunicorn",
//   "succulentspughumblemeditationlocavore"
// ); // -> 15

// ========================= Memoization =========================
// Time: O(nm), Space: O(nm)
const overlapSubsequence = (str1, str2, i = 0, j = 0, memo = {}) => {
  const key = i + '-' + j;
  if (key in memo) return memo[key];
  if (i === str1.length || j === str2.length) return 0;

  if (str1[i] === str2[j]) {
    memo[key] = 1 + overlapSubsequence(str1, str2, i + 1, j + 1, memo);
  } else {
    memo[key] = Math.max(
      overlapSubsequence(str1, str2, i + 1, j, memo),
      overlapSubsequence(str1, str2, i, j + 1, memo)
    );
  }

  return memo[key];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #63 can concat ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, canConcat, that takes in a string and an array of words as
// arguments. The function should return boolean indicating whether or not it is
// possible to concatenate words of the array together to form the string.
// You may reuse words of the array as many times as needed.
//
// test_00:
// canConcat("oneisnone", ["one", "none", "is"]); // -> true
// test_01:
// canConcat("oneisnone", ["on", "e", "is"]); // -> false
// test_02:
// canConcat("oneisnone", ["on", "e", "is", "n"]); // -> true
// test_03:
// canConcat("foodisgood", ["is", "g", "ood", "f"]); // -> true
// test_04:
// canConcat("santahat", ["santah", "hat"]); // -> false
// test_05:
// canConcat("santahat", ["santah", "san", "hat", "tahat"]); // -> true
// test_06:
// canConcat("rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]); // -> false

// ========================= Memoization =========================
// Time: ~O(sw), Space: O(s)
const canConcat = (str, words, memo = {}) => {
  if (str in memo) return memo[str];
  if (!str.length) return true;
  
  for (let word of words) {
    const slicedStr = str.slice(word.length);
    if (str.startsWith(word) && canConcat(slicedStr, words, memo)) {
      memo[str] = true;
      return true;
    }
  }
  
  memo[str] = false;
  return memo[str];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #64 quickest concat ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, quickestConcat, that takes in a string and an array of words
// as arguments. The function should return the minimum number of words needed to
// build the string by concatenating the words.
// You may use words of the array as many times as needed.
//
// test_00:
// quickestConcat('caution', ['ca', 'ion', 'caut', 'ut']); // -> 2
// test_01:
// quickestConcat('caution', ['ion', 'caut', 'caution']); // -> 1
// test_02:
// quickestConcat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']); // -> 4
// test_03:
// quickestConcat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']); // -> 3
// test_04:
// quickestConcat('simchacindy', ['sim', 'simcha', 'acindy']); // -> -1
// test_05:
// quickestConcat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']); // -> 2
// test_06:
// quickestConcat('rongbetty', ['wrong', 'bet']); // -> -1
// test_07:
// quickestConcat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']); // -> 7

// ========================= Memoization =========================
// Time: ~O(sw), Space: O(s)
const _quickestConcat = (str, words, memo = {}) => {
  if (str in memo) return memo[str];
  if (!str.length) return 0;

  let minWords = Infinity;
  for (let word of words) {
    if (str.startsWith(word)) {
      const numWords = 1 + _quickestConcat(str.slice(word.length), words, memo);
      if (minWords > numWords) minWords = numWords;
    }
  }

  return memo[str] = minWords;
};

const quickestConcat = (str, words) => {
  const min = _quickestConcat(str, words);
  return min === Infinity ? -1 : min;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #65 paired parentheses ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, pairedParentheses, that takes in a string as an argument.
// The function should return a boolean indicating whether or not the string has
// well-formed parentheses.
// You may assume the string contains only alphabetic characters, '(', or ')'.
//
// test_00:
// pairedParentheses("(david)((abby))"); // -> true
// test_01:
// pairedParentheses("()rose(jeff"); // -> false
// test_02:
// pairedParentheses(")("); // -> false
// test_03:
// pairedParentheses("()"); // -> true
// test_04:
// pairedParentheses("(((potato())))"); // -> true
// test_05:
// pairedParentheses("(())(water)()"); // -> true
// test_06:
// pairedParentheses("(())(water()()"); // -> false
// test_07:
// pairedParentheses(""); // -> true

// ========================= Counter =========================
// Time: O(n), Space: O(1);
const pairedParentheses = (str) => {
  let count = 0;
  
  for (let char of str) {
    if (char === '(') {
      count++;
    } else if (char === ')') {
      if (count === 0) return false;
      count--;
    }
  }
  
  return !count
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #66 befitting brackets ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, befittingBrackets, that takes in a string as an argument.
// The function should return a boolean indicating whether or not the string
// contains correctly matched brackets.
// You may assume the string contains only characters: ( ) [ ] { }
//
// test_00:
// befittingBrackets('(){}[](())'); // -> true
// test_01:
// befittingBrackets('({[]})'); // -> true
// test_02:
// befittingBrackets('[][}'); // -> false
// test_03:
// befittingBrackets('{[]}({}'); // -> false
// test_04:
// befittingBrackets('[]{}(}[]'); // -> false
// test_05:
// befittingBrackets('[]{}()[]'); // -> true
// test_06:
// befittingBrackets(']{}'); // -> false
// test_07:
// befittingBrackets(''); // -> true

// ========================= Counter =========================
// Time: O(n), Space: O(1);
const befittingBrackets = (str) => {
  const count = {
    '(': 0,
    '[': 0,
    '{': 0
  };
  
  const pairing = {
    ')': '(',
    ']': '[',
    '}': '{'
  };

  for (let char of str) {
    if (char in count) {
      count[char] += 1;
    } else {
      if (count[pairing[char]] > 0) {
        count[pairing[char]] -= 1;
      } else {
        return false;
      }
    }
  }

  return Object.values(count).every(el => el === 0);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #67 decompress braces ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, decompressBraces, that takes in a compressed string as an
// argument. The function should return the string decompressed.
// The compression format of the input string is 'n{subString}', where the
// subString within braces should be repeated n times.
// You may assume that every number n is guaranteed to be an integer between 1
// through 9.
// You may assume that the input is valid and the decompressed string will only
// contain alphabetic characters.
//
// test_00:
// decompressBraces("2{q}3{tu}v"); 
// -> qqtututuv 
// test_01:
// decompressBraces("ch3{ao}"); 
// -> chaoaoao
// test_02:
// decompressBraces("2{y3{o}}s"); 
// -> yoooyooos
// test_03:
// decompressBraces("z3{a2{xy}b}"); 
// -> zaxyxybaxyxybaxyxyb 
// test_04:
// decompressBraces("2{3{r4{e}r}io}"); 
// -> reeeerreeeerreeeerioreeeerreeeerreeeerio 
// test_05:
// decompressBraces("go3{spinn2{ing}s}"); 
// -> gospinningingsspinningingsspinningings 
// test_06:
// decompressBraces("2{l2{if}azu}l"); 
// -> lififazulififazul 
// test_07:
// decompressBraces("3{al4{ec}2{icia}}"); 
// -> alececececiciaiciaalececececiciaiciaalececececiciaicia 

// ========================= Stack =========================
// Time: O((9^m) * s), Space: O((9^m) * s)
const decompressBraces = (str) => {
  const integers = '123456789';
  const stack = [];

  for (let char of str) {
    if (integers.includes(char)) {
      stack.push(Number(char));
    } else {
      if (char === '}') {
        stack.push(stringMultiply(stack));
      } else if (char !== '{') {
        stack.push(char);
      }
    }
  }

  return stack.join('');
};

const stringMultiply = (stack) => {
  let chars = '';

  while (typeof stack[stack.length - 1] !== 'number') {
    let s = stack.pop();
    chars = s + chars;
  }

  const num = stack.pop();
  let result = '';
  for (let i = 0; i < num; i++) {
    result += chars;
  }

  return result;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #68 nesting score ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, nestingScore, that takes in a string of brackets as an
// argument. The function should return the score of the string according to the
// following rules:
// [] is worth 1 point
// XY is worth m + n points where X, Y are substrings of well-formed brackets and m, n are their respective scores
// [S] is worth 2 * k points where S is a substring of well-formed brackets and k is the score of that substring
// You may assume that the input only contains well-formed square brackets.
//
// test_00:
// nestingScore("[]"); // -> 1
// test_01:
// nestingScore("[][][]"); // -> 3
// test_02:
// nestingScore("[[]]"); // -> 2
// test_03:
// nestingScore("[[][]]"); // -> 4
// test_04:
// nestingScore("[[][][]]"); // -> 6
// test_05:
// nestingScore("[[][]][]"); // -> 5
// test_06:
// nestingScore("[][[][]][[]]"); // -> 7
// test_07:
// nestingScore("[[[[[[[][]]]]]]][]"); // -> 129

// ========================= Stack =========================
// Time: O(n), Space: O(n)
const nestingScore = (str) => {
  const stack = [0];

  for (let char of str) {
    if (char === '[') {
      stack.push(0);
    } else {
      const last = stack.pop();
      if (last !== 0) {
        stack[stack.length - 1] += 2 * last;
      } else {
        stack[stack.length - 1] += 1;
      }
    }
  }

  return stack[0];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #69 subsets ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, subsets, that takes in an array an argument. The function
// should return a 2D array where each subarray represents one of the possible
// subsets of the array.
// The elements within the subsets and the subsets themselves may be returned in any order.
// You may assume that the input array contains unique elements.
//
// test_00:
// subsets(['a', 'b']); // ->
// [ 
//   [], 
//   [ 'b' ], 
//   [ 'a' ], 
//   [ 'a', 'b' ] 
// ]
// test_01:
// subsets(['a', 'b', 'c']); // ->
// [
//   [],
//   [ 'c' ],
//   [ 'b' ],
//   [ 'b', 'c' ],
//   [ 'a' ],
//   [ 'a', 'c' ],
//   [ 'a', 'b' ],
//   [ 'a', 'b', 'c' ]
// ]
// test_02:
// subsets(['x']); // ->
// [ 
//   [], 
//   [ 'x' ] 
// ]
// test_03:
// subsets([]); // ->
// [ 
//   []
// ]
// test_04:
// subsets(['q', 'r', 's', 't']); // ->
// [
//   [],
//   [ 't' ],
//   [ 's' ],
//   [ 's', 't' ],
//   [ 'r' ],
//   [ 'r', 't' ],
//   [ 'r', 's' ],
//   [ 'r', 's', 't' ],
//   [ 'q' ],
//   [ 'q', 't' ],
//   [ 'q', 's' ],
//   [ 'q', 's', 't' ],
//   [ 'q', 'r' ],
//   [ 'q', 'r', 't' ],
//   [ 'q', 'r', 's' ],
//   [ 'q', 'r', 's', 't' ]
// ]

// ========================= Recursive =========================
// Time: O(2*n), Space: O(2*n)
const subsets = (elements) => {
  if (!elements.length) return [[]];
  
  const subs = subsets(elements.slice(1));
  return subs.concat(subs.map(sub => sub.concat(elements[0])));
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #70 permutations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, permutations, that takes in an array an argument. The
// function should return a 2D array where each subarray represents one of the
// possible permutations of the array.
// The subarrays may be returned in any order.
// You may assume that the input array contains unique elements.
//
// test_00:
// permutations(['a', 'b', 'c']); // -> 
// [ 
//   [ 'a', 'b', 'c' ], 
//   [ 'b', 'a', 'c' ], 
//   [ 'b', 'c', 'a' ], 
//   [ 'a', 'c', 'b' ], 
//   [ 'c', 'a', 'b' ], 
//   [ 'c', 'b', 'a' ] 
// ] 
// test_01:
// permutations(['red', 'blue']); // ->
// [ 
//   [ 'red', 'blue' ], 
//   [ 'blue', 'red' ] 
// ]
// test_02:
// permutations([8, 2, 1, 4]); // ->
// [ 
//   [ 8, 2, 1, 4 ], [ 2, 8, 1, 4 ], 
//   [ 2, 1, 8, 4 ], [ 2, 1, 4, 8 ], 
//   [ 8, 1, 2, 4 ], [ 1, 8, 2, 4 ], 
//   [ 1, 2, 8, 4 ], [ 1, 2, 4, 8 ], 
//   [ 8, 1, 4, 2 ], [ 1, 8, 4, 2 ], 
//   [ 1, 4, 8, 2 ], [ 1, 4, 2, 8 ], 
//   [ 8, 2, 4, 1 ], [ 2, 8, 4, 1 ], 
//   [ 2, 4, 8, 1 ], [ 2, 4, 1, 8 ], 
//   [ 8, 4, 2, 1 ], [ 4, 8, 2, 1 ], 
//   [ 4, 2, 8, 1 ], [ 4, 2, 1, 8 ], 
//   [ 8, 4, 1, 2 ], [ 4, 8, 1, 2 ], 
//   [ 4, 1, 8, 2 ], [ 4, 1, 2, 8 ] 
// ] 
// test_03:
// permutations([]); // ->
// [
//  [ ]
// ]

// ========================= Recursive =========================
// Time: O(n!), Space: O(n!)
const permutations = (items) => {
  if (!items.length) return [[]];

  const first = items[0];
  const perms = permutations(items.slice(1));
  const allPerms = [];
  for (let perm of perms) {
    for (let i = 0; i <= perm.length; i++) {
      allPerms.push([...perm.slice(0, i), first, ...perm.slice(i)]);
    }
  }

  return allPerms;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #71 create combinations ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, createCombinations, that takes in an array and a length as
// arguments. The function should return a 2D array representing all of the
// combinations of the specifized length.
// The items within the combinations and the combinations themselves may be returned in any order.
// You may assume that the input array contains unique elements and 1 <= k <= items.length.
//
// test_00:
// createCombinations(["a", "b", "c"], 2); // ->
// [
//   [ 'a', 'b' ],
//   [ 'a', 'c' ],
//   [ 'b', 'c' ]
// ]
// test_01:
// createCombinations(["q", "r", "s", "t"], 2); // ->
// [
//   [ 'q', 'r' ],
//   [ 'q', 's' ],
//   [ 'q', 't' ],
//   [ 'r', 's' ],
//   [ 'r', 't' ],
//   [ 's', 't' ]
// ]
// test_02:
// createCombinations(['q', 'r', 's', 't'], 3)); // ->
// [
//   [ 'q', 'r', 's' ],
//   [ 'q', 'r', 't' ],
//   [ 'q', 's', 't' ],
//   [ 'r', 's', 't' ]
// ]
// test_03:
// createCombinations([1, 28, 94], 3); // ->
// [
//   [ 1, 28, 94 ]
// ]

// ========================= Recursive =========================
// Time: O(n! / k!(n-k)!), Space: O(n! / k!(n-k)!)
// "n choose k" = binomial coefficient
const createCombinations = (items, k) => {
  if (k === 0) return [[]];
  if (k > items.length) return [];
  if (k === items.length) return items;

  const first = items.slice(0, 1);
  const rest = items.slice(1);
  const combos1 = createCombinations(rest, k - 1);
  const combos2 = createCombinations(rest, k);
  
  return combos1.map(combo => first.concat(combo)).push(combos2);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #72 parenthetical possibilities ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, parentheticalPossibilities, that takes in a string as an
// argument. The function should return an array containing all of the strings
// that could be generated by expanding all parentheses of the string into its
// possibilities.
// For example, the possibilities for 'x(mn)yz' are 'xmyz', 'xnyz'.
//
// test_00:
// parentheticalPossibilities('x(mn)yz'); // -> 
// [ 'xmyz', 'xnyz' ]
// test_01:
// parentheticalPossibilities("(qr)ab(stu)c"); // ->
// [ 'qabsc', 'qabtc', 'qabuc', 'rabsc', 'rabtc', 'rabuc' ]
// test_02:
// parentheticalPossibilities("taco"); // ->
// ['taco']
// test_03:
// parentheticalPossibilities(""); // ->
// ['']
// test_04:
// parentheticalPossibilities("(etc)(blvd)(cat)"); // ->
// [
//  'ebc', 'eba', 'ebt', 'elc', 'ela',
//  'elt', 'evc', 'eva', 'evt', 'edc',
//  'eda', 'edt', 'tbc', 'tba', 'tbt',
//  'tlc', 'tla', 'tlt', 'tvc', 'tva',
//  'tvt', 'tdc', 'tda', 'tdt', 'cbc',
//  'cba', 'cbt', 'clc', 'cla', 'clt',
//  'cvc', 'cva', 'cvt', 'cdc', 'cda',
//  'cdt'
// ]

// ========================= My Solution (Memoization) =========================
// n: num letters, m: max letters in parentheses
// Time: ~O(m^n), Space: ~O(m^n)
const parentheticalPossibilities = (str) => {
  if (!str.length) return [''];
  const possibilities = [];
  let suffixes;

  if (str[0] !== '(') {
    suffixes = parentheticalPossibilities(str.slice(1));

    for (let i = 0; i < suffixes.length; i++) {
      possibilities.push(str[0] + suffixes[i]);
    }
  } else {
    const closeParenIdx = str.indexOf(')');
    const parenChars = str.slice(1, closeParenIdx);
    suffixes = parentheticalPossibilities(str.slice(closeParenIdx + 1));

    for (let char of parenChars) {
      for (let i = 0; i < suffixes.length; i++) {
        possibilities.push(char + suffixes[i]);
      }
    }
  }

  return possibilities;
};

// ========================= Alvin's Solution =========================
const parentheticalPossibilities = (s) => {
  if (s === "") return [""];

  const { remaining, chars } = getOptions(s);
  const suffixes = parentheticalPossibilities(remaining);
  const possibilities = [];

  for (let char of chars) {
    for (let suffix of suffixes) {
      possibilities.push(char + suffix);
    }
  }

  return possibilities;
};

const getOptions = (s) => {
  if (s[0] === "(") {
    const endIdx = s.indexOf(")");
    const remaining = s.slice(endIdx + 1);
    const chars = s.slice(1, endIdx).split("");
    return { remaining, chars };
  } else {
    const remaining = s.slice(1);
    const chars = [s[0]];
    return { remaining, chars };
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #73 substituting synonyms ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, substitutingSynonyms, that takes in a sentence and an object
// as arguments. The object contains words as keys whose values are arrays
// containing synonyms. The function should return an array containing all
// possible sentences that can be formed by substituting words of the sentence
// with their synonyms.
// You may return the possible sentences in any order, as long as you return
// all of them.
//
// test_00:
// const sentence = "follow the yellow brick road";
// const synonyms = {
//   follow: ["chase", "pursue"],
//   yellow: ["gold", "amber", "lemon"],
// };
// substituteSynonyms(sentence, synonyms);
// [
//   'chase the gold brick road',
//   'chase the amber brick road',
//   'chase the lemon brick road',
//   'pursue the gold brick road',
//   'pursue the amber brick road',
//   'pursue the lemon brick road'
// ]
// test_01:
// const sentence = "I think it's gonna be a long long time";
// const synonyms = {
//   think: ["believe", "reckon"],
//   long: ["lengthy", "prolonged"],
// };
// substituteSynonyms(sentence, synonyms);
// [
//   "I believe it's gonna be a lengthy lengthy time",
//   "I believe it's gonna be a lengthy prolonged time",
//   "I believe it's gonna be a prolonged lengthy time",
//   "I believe it's gonna be a prolonged prolonged time",
//   "I reckon it's gonna be a lengthy lengthy time",
//   "I reckon it's gonna be a lengthy prolonged time",
//   "I reckon it's gonna be a prolonged lengthy time",
//   "I reckon it's gonna be a prolonged prolonged time"
// ]
// test_02:
// const sentence = "palms sweaty knees weak arms heavy";
// const synonyms = {
//   palms: ["hands", "fists"],
//   heavy: ["weighty", "hefty", "burdensome"],
//   weak: ["fragile", "feeble", "frail", "sickly"],
// };
// substituteSynonyms(sentence, synonyms);
// [
//   'hands sweaty knees fragile arms weighty',
//   'hands sweaty knees fragile arms hefty',
//   'hands sweaty knees fragile arms burdensome',
//   'hands sweaty knees feeble arms weighty',
//   'hands sweaty knees feeble arms hefty',
//   'hands sweaty knees feeble arms burdensome',
//   'hands sweaty knees frail arms weighty',
//   'hands sweaty knees frail arms hefty',
//   'hands sweaty knees frail arms burdensome',
//   'hands sweaty knees sickly arms weighty',
//   'hands sweaty knees sickly arms hefty',
//   'hands sweaty knees sickly arms burdensome',
//   'fists sweaty knees fragile arms weighty',
//   'fists sweaty knees fragile arms hefty',
//   'fists sweaty knees fragile arms burdensome',
//   'fists sweaty knees feeble arms weighty',
//   'fists sweaty knees feeble arms hefty',
//   'fists sweaty knees feeble arms burdensome',
//   'fists sweaty knees frail arms weighty',
//   'fists sweaty knees frail arms hefty',
//   'fists sweaty knees frail arms burdensome',
//   'fists sweaty knees sickly arms weighty',
//   'fists sweaty knees sickly arms hefty',
//   'fists sweaty knees sickly arms burdensome'
// ]

// ========================= My Solution (Recursive) =========================
// n: num words in a sentence, m: max num of synonyms for a word
// Time: ~O(m^n), Space: ~O(m^n)
const substituteSynonyms = (sentence, synonyms) => {
  const substitutions = _substituteSynonyms(sentence.split(' '), synonyms);

  return substitutions.map(sub => sub.join(' '));
};

const _substituteSynonyms = (words, synonyms) => {
  if (!words.length) return [[]];

  const suffixes = _substituteSynonyms(words.slice(1), synonyms);
  const prefixes = words[0] in synonyms ? synonyms[words[0]] : [words[0]];
  const substitutions = [];

  for (let suffix of suffixes) {
    for (let syn of prefixes) {
      substitutions.push([syn, ...suffix]);
    }
  }

  return substitutions;
};

// ========================= Alvin's Solution =========================
const substituteSynonyms = (sentence, synonyms) => {
  const words = sentence.split(' ');
  const arrays = generate(words, synonyms);
  return arrays.map(subarray => subarray.join(' '));
};

const generate = (words, synonyms) => {
  if (words.length === 0) return [[]];
  
  const firstWord = words[0];
  const remainingWords = words.slice(1);
  if (firstWord in synonyms) {
    const result = [];
    const subarrays = generate(remainingWords, synonyms);
    for (let synonym of synonyms[firstWord]) {
      result.push(...subarrays.map(subarray => [ synonym, ...subarray ]));
    }
    return result;
  } else {
    const subarrays = generate(remainingWords, synonyms);
    return subarrays.map(subarray => [ firstWord, ...subarray ]);
  };
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #74 linked palindrome ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, linkedPalindrome, that takes in the head of a linked list
// as an argument. The function should return a boolean indicating whether or
// not the linked list is a palindrome. A palindrome is a sequence that is the
// same both forwards and backwards.
//
// test_00:
// const a = new Node(3);
// const b = new Node(2);
// const c = new Node(7);
// const d = new Node(7);
// const e = new Node(2);
// const f = new Node(3);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// 3 -> 2 -> 7 -> 7 -> 2 -> 3
// linkedPalindrome(a); // true
// test_01:
// const a = new Node(3);
// const b = new Node(2);
// const c = new Node(4);
// a.next = b;
// b.next = c;
// 3 -> 2 -> 4
// linkedPalindrome(a); // false
// test_02:
// const a = new Node(3);
// const b = new Node(2);
// const c = new Node(3);
// a.next = b;
// b.next = c;
// 3 -> 2 -> 3
// linkedPalindrome(a); // true
// test_03:
// const a = new Node(0);
// const b = new Node(1);
// const c = new Node(0);
// const d = new Node(1);
// const e = new Node(0);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// 0 -> 1 -> 0 -> 1 -> 0
// linkedPalindrome(a); // true
// test_04:
// const a = new Node(0);
// const b = new Node(1);
// const c = new Node(0);
// const d = new Node(1);
// const e = new Node(1);
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// 0 -> 1 -> 0 -> 1 -> 1
// linkedPalindrome(a); // false
// test_05:
// const a = new Node(5);
// 5
// linkedPalindrome(a); // true
// test_06:
// linkedPalindrome(null); // true

// ========================= Array =========================
// Time: O(n), Space: O(n)
const linkedPalindrome = (head) => {
  const values = [];
  let currNode = head;

  while (currNode !== null) {
    values.push(currNode.val);
    currNode = currNode.next;
  }

  return values.join('') === values.reverse().join('');
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #75 middle value ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, middleValue, that takes in the head of a linked list as an
// argument. The function should return the value of the middle node in the
// linked list. If the linked list has an even number of nodes, then return the
// value of the second middle node.
// You may assume that the input list is non-empty.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// a -> b -> c -> d -> e
// middleValue(a); // c
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = e;
// e.next = f;
// a -> b -> c -> d -> e -> f
// middleValue(a); // d
// test_02:
// const x = new Node('x');
// const y = new Node('y');
// const z = new Node('z');
// x.next = y;
// y.next = z;
// x -> y -> z
// middleValue(x); // y
// test_03:
// const x = new Node('x');
// const y = new Node('y');
// x.next = y;
// x -> y 
// middleValue(x); // y
// test_04:
// const q = new Node('q');
// q
// middleValue(q); // q

// ========================= Array =========================
// Time: O(n), Space: O(n)
const middleValue = (head) => {
  const values = [];
  let currNode = head;

  while (currNode !== null) {
    values.push(currNode.val);
    currNode = currNode.next;
  }

  return values[Math.floor(values.length / 2)];
};

// ========================= 2 Pointers =========================
// Time: O(n), Space: O(1)
const middleValue = (head) => {
  let fast = head;
  let slow = head;

  while (fast.next !== null && fast !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow.val;
}

// [[[[[[[[[[[[[[[[[[[[[[[[[ #76 linked list cycle ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, linkedListCycle, that takes in the head of a linked list as
// an argument. The function should return a boolean indicating whether or not
// the linked list contains a cycle.
//
// test_00:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// a.next = b;
// b.next = c;
// c.next = d;
// d.next = b; // cycle
//         _______
//       /        \
// a -> b -> c -> d 
// linkedListCycle(a);  // true
// test_01:
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// const u = new Node('u');
// q.next = r;
// r.next = s;
// s.next = t;
// t.next = u;
// u.next = q; // cycle
//    ________________
//  /                 \
// q -> r -> s -> t -> u 
// linkedListCycle(q);  // true
// test_02
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// a.next = b;
// b.next = c;
// c.next = d;
// a -> b -> c -> d 
// linkedListCycle(a);  // false
// test_03:
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// const u = new Node('u');
// q.next = r;
// r.next = s;
// s.next = t;
// t.next = u;
// u.next = t; // cycle
//                   __
//                 /   \
// q -> r -> s -> t -> u 
// linkedListCycle(q);  // true
// test_04:
// const p = new Node('p');
// p
// linkedListCycle(p); // false
// test_05:
// linkedListCycle(null); // false

// ========================= Set =========================
// Time: O(n), Space: O(n)
const linkedListCycle = (head) => {
  const visited = new Set();
  let currNode = head;

  while (currNode !== null) {
    if (visited.has(currNode.val)) return true;
    visited.add(currNode.val);
    currNode = currNode.next;
  }

  return false;
};

// ========================= 2 Pointers =========================
// Time: O(n), Space: O(1)
const linkedListCycle = (head) => {
  let fast = head;
  let slow = head;
  let firstIteration = true;

  while (fast !== null && fast.next !== null) {
    if (fast === slow && !firstIteration) return true;
    
    fast = fast.next.next;
    slow = slow.next;
    firstIteration = false;
  }

  return false;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #77 lowest common ancestor ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, lowestCommonAncestor, that takes in the root of a binary
// tree and two values. The function should return the value of the lowest common
// ancestor of the two values in the tree.
// You may assume that the tree values are unique and the tree is non-empty.
// Note that a node may be considered an ancestor of itself.
// Example Tree:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//      a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
//
// test_00
// lowestCommonAncestor(a, 'd', 'h'); // b
// test_01
// lowestCommonAncestor(a, 'd', 'g'); // b
// test_02
// lowestCommonAncestor(a, 'g', 'c'); // a
// test_03
// lowestCommonAncestor(a, 'b', 'g'); // b
// test_04
// lowestCommonAncestor(a, 'f', 'c'); // c
// example tree
// const l = new Node('l');
// const m = new Node('m');
// const n = new Node('n');
// const o = new Node('o');
// const p = new Node('p');
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// l.left = m;
// l.right = n;
// n.left = o;
// n.right = p;
// o.left = q;
// o.right = r;
// p.left = s;
// p.right = t;
//        l
//     /     \
//    m       n
//         /    \
//         o     p
//        / \   / \
//       q   r s   t
// test_05
// lowestCommonAncestor(l, 'r', 'p'); // n
// test_06
// lowestCommonAncestor(l, 'm', 'o'); // l
// test_07
// lowestCommonAncestor(l, 't', 'q'); // n
// test_08
// lowestCommonAncestor(l, 's', 'p'); // p

// ========================= My Solution (DFS) =========================
// Time: O(n), Space: O(n)
const lowestCommonAncestor = (root, val1, val2) => {
  const ancestry = buildAncestry(root);

  const ancestors1 = new Set(val1);
  const ancestors2 = new Set(val2);
  let ancestor1 = ancestry[val1];
  let ancestor2 = ancestry[val2];

  while (ancestor1 !== null || ancestor2 !== null) {
    ancestors1.add(ancestor1);
    ancestors2.add(ancestor2);

    if (ancestors1.has(ancestor2)) return ancestor2;
    if (ancestors2.has(ancestor1)) return ancestor1;

    ancestor1 = ancestry[ancestor1];
    ancestor2 = ancestry[ancestor2];
  }
};

const buildAncestry = (root) => {
  const ancestry = { [root.val]: null };
  const stack = [root];

  while (stack.length) {
    const node = stack.pop();
    if (node.left) {
      ancestry[node.left.val] = node.val;
      stack.push(node.left);
    }
    if (node.right) {
      ancestry[node.right.val] = node.val;
      stack.push(node.right);
    }
  }

  return ancestry;
};

// ========================= Alvin's Solution (DFS) =========================
// Time: O(n), Space: O(n)
const lowestCommonAncestor = (root, val1, val2) => {
  const path1 = findPath(root, val1);
  const path2 = findPath(root, val2);
  const set2 = new Set(path2);
  
  for (let val of path1) {
    if (set2.has(val)) return val;
  }
};

const findPath = (root, targetVal) => {
  if (root === null) return null;
  
  if (root.val === targetVal) return [ root.val ];

  const leftPath = findPath(root.left, targetVal);
  if (leftPath !== null) {
    leftPath.push(root.val);
    return leftPath;
  }
  
  const rightPath = findPath(root.right, targetVal);
  if (rightPath !== null) {
    rightPath.push(root.val);
    return rightPath;
  }  
  
  return null;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #78 flip tree ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, flipTree, that takes in the root of a binary tree. The
// function should flip the binary tree, turning left subtrees into right
// subtrees and vice-versa. This flipping should occur in-place by modifying the
// original tree. The function should return the root of the tree.
//
// test_00
// const a = new Node("a");
// const b = new Node("b");
// const c = new Node("c");
// const d = new Node("d");
// const e = new Node("e");
// const f = new Node("f");
// const g = new Node("g");
// const h = new Node("h");
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//      a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
// flipTree(a); 
//       a
//    /    \
//   c      b
//  /     /   \
// f     e    d
//     /  \
//    h    g
// test_01
// const u = new Node("u");
// const t = new Node("t");
// const s = new Node("s");
// const r = new Node("r");
// const q = new Node("q");
// const p = new Node("p");
// u.left = t;
// u.right = s;
// s.right = r;
// r.left = q;
// r.right = p;
//     u
//  /    \
// t      s
//         \
//         r
//        / \
//        q  p
// flipTree(u);
//           u
//        /    \
//       s      t
//      /
//     r
//    / \
//   p  q
// test_02
// const l = new Node("l");
// const m = new Node("m");
// const n = new Node("n");
// const o = new Node("o");
// const p = new Node("p");
// const q = new Node("q");
// const r = new Node("r");
// const s = new Node("s");
// const t = new Node("t");
// l.left = m;
// l.right = n;
// n.left = o;
// n.right = p;
// o.left = q;
// o.right = r;
// p.left = s;
// p.right = t;
//        l
//     /     \
//    m       n
//         /    \
//         o     p
//        / \   / \
//       q   r s   t
// flipTree(l);
//             l
//         /      \
//        n        m
//      /  \
//    p     o
//  / \    / \
// t   s  r   q
// test_03
// const n = new Node("n");
// const y = new Node("y");
// const c = new Node("c");
// n.left = y;
// n.right = c;
//       n
//     /   \
//    y     c
// flipTree(n);
//       n
//     /   \
//    c     y

// ========================= Recursive =========================
// Time: O(n), Space: O(n)
const flipTree = (root) => {
  if (!root) return root;

  const left = flipTree(root.left);
  const right = flipTree(root.right);
  root.left = right;
  root.right = left;

  return root;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #79 lefty nodes ]]]]]]]]]]]]]]]]]]]]]]]]] 
// Write a function, leftyNodes, that takes in the root of a binary tree. The
// function should return an array containing the left-most value on every level
// of the tree. The array must be ordered in a top-down fashion where the root
// is the first element.
//
// test_00
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//      a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
// leftyNodes(a); // [ 'a', 'b', 'd', 'g' ]
// test_01
// const u = new Node('u');
// const t = new Node('t');
// const s = new Node('s');
// const r = new Node('r');
// const q = new Node('q');
// const p = new Node('p');
// u.left = t;
// u.right = s;
// s.right = r;
// r.left = q;
// r.right = p;
//     u
//  /    \
// t      s
//         \
//         r
//        / \
//        q  p
// leftyNodes(u); // [ 'u', 't', 'r', 'q' ]
// test_02
// const l = new Node('l');
// const m = new Node('m');
// const n = new Node('n');
// const o = new Node('o');
// const p = new Node('p');
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// l.left = m;
// l.right = n;
// n.left = o;
// n.right = p;
// o.left = q;
// o.right = r;
// p.left = s;
// p.right = t;
//        l
//     /     \
//    m       n
//         /    \
//         o     p
//        / \   / \
//       q   r s   t
// leftyNodes(l); // [ 'l', 'm', 'o', 'q' ]
// test_03
// const n = new Node('n');
// const y = new Node('y');
// const c = new Node('c');
// n.left = y;
// n.right = c;
//       n
//     /   \
//    y     c
// leftyNodes(n); // [ 'n', 'y' ]
// test_04
// const i = new Node('i');
// const n = new Node('n');
// const s = new Node('s');
// const t = new Node('t');
// i.right = n;
// n.left = s;
// n.right = t;
//       i
//        \
//         n
//        / \
//       s   t
// leftyNodes(i); // [ 'i', 'n', 's' ]
// test_05
// leftyNodes(null); // [ ]

// ========================= BFS =========================
// Time: O(n^2), Space: O(n)
const leftyNodes = (root) => {
  const queue = [{ node: root, level: 0 }];
  const levels = [];

  while (queue.length && root) {
    const { node, level } = queue.shift();
    if (!levels[level]) levels[level] = node.val;

    if (node.left) queue.push({ node: node.left, level: level + 1 });
    if (node.right) queue.push({ node: node.right, level: level + 1 });
  }

  return levels;
};

// ========================= Alvin's Solution (DFS) =========================
// Time: O(n), Space: O(n)
const leftyNodes = (root) => {
  const values = [];
  
  const traverse = (node, level) => {
    if (node === null) return;
    
    if (values[level] === undefined) values.push(node.val);
    
    traverse(node.left, level + 1);
    traverse(node.right, level + 1);
  };
  
  traverse(root, 0);
  return values;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #80 can color ]]]]]]]]]]]]]]]]]]]]]]]]] !!I
// Write a function, canColor, that takes in an object representing the adjacency
// list of an undirected graph. The function should return a boolean indicating
// whether or not it is possible to color nodes of the graph using two colors in
// such a way that adjacent nodes are always different colors.
// For example, given this graph:
// x-y-z
// It is possible to color the nodes by using red for x and z, 
// then use blue for y. So the answer is true.
// For example, given this graph:
//     q
//    / \
//   s - r
// It is not possible to color the nodes without making two 
// adjacent nodes the same color. So the answer is false.
//
// test_00:
// canColor({
//   x: ["y"],
//   y: ["x","z"],
//   z: ["y"]
// }); // -> true
// test_01:
// canColor({
//   q: ["r", "s"],
//   r: ["q", "s"],
//   s: ["r", "q"]
// }); // -> false
// test_02:
// canColor({
//   a: ["b", "c", "d"],
//   b: ["a"],
//   c: ["a"],
//   d: ["a"],
// }); // -> true
// test_03:
// canColor({
//   a: ["b", "c", "d"],
//   b: ["a"],
//   c: ["a", "d"],
//   d: ["a", "c"],
// }); // -> false
// test_04:
// canColor({
//   h: ["i", "k"],
//   i: ["h", "j"],
//   j: ["i", "k"],
//   k: ["h", "j"],
// }); // -> true
// test_05:
// canColor({
//   z: []
// }); // -> true
// test_06:
// canColor({
//   h: ["i", "k"],
//   i: ["h", "j"],
//   j: ["i", "k"],
//   k: ["h", "j"],
//   q: ["r", "s"],
//   r: ["q", "s"],
//   s: ["r", "q"]
// }); // -> false

// ========================= Alvin's Solution (DFS) =========================
// Time: O(n^2), Space: O(n)
const canColor = (graph) => {
  const coloring = {};
  
  for (let node in graph) {
    if (!(node in coloring)) {
      if (!valid(graph, node, coloring, false)) {
        return false;
      }
    }
  }
  
  return true;
};

const valid = (graph, node, coloring, currentColor) => {
  if (node in coloring) return currentColor === coloring[node];
  
  coloring[node] = currentColor;
  
  for (let neighbor of graph[node]) {
    if (!valid(graph, neighbor, coloring, !currentColor)) {
      return false;
    }
  }
  
  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #81 tolerant teams ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, tolerantTeams, that takes in an array of rivalries as an
// argument. A rivalry is a pair of people who should not be placed on the same
// team. The function should return a boolean indicating whether or not it is
// possible to separate people into two teams, without rivals being on the same
// team. The two teams formed do not have to be the same size.
//
// test_00:
// tolerantTeams([
//   ['philip', 'seb'],
//   ['raj', 'nader']
// ]); // -> true
// test_01:
// tolerantTeams([
//   ['philip', 'seb'],
//   ['raj', 'nader'],
//   ['raj', 'philip'],
//   ['seb', 'raj']
// ]); // -> false
// test_02:
// tolerantTeams([
//   ['cindy', 'anj'],
//   ['alex', 'matt'],
//   ['alex', 'cindy'],
//   ['anj', 'matt'],
//   ['brando', 'matt']
// ]); // -> true
// test_03:
// tolerantTeams([
//   ['alex', 'anj'],
//   ['alex', 'matt'],
//   ['alex', 'cindy'],
//   ['anj', 'matt'],
//   ['brando', 'matt']
// ]); // -> false
// test_04:
// tolerantTeams([
//   ['alan', 'jj'],
//   ['betty', 'richard'],
//   ['jj', 'simcha'],
//   ['richard', 'christine']
// ]); // -> true
// test_05:
// tolerantTeams([
//   ['alan', 'jj'],
//   ['betty', 'richard'],
//   ['jj', 'simcha'],
//   ['richard', 'christine']
// ]); // -> true
// test_06:
// tolerantTeams([
//   ['alan', 'jj'],
//   ['jj', 'richard'],
//   ['betty', 'richard'],
//   ['jj', 'simcha'],
//   ['richard', 'christine']
// ]); // -> true
// test_07:
// tolerantTeams([
//   ['alan', 'jj'],
//   ['betty', 'richard'],
//   ['betty', 'christine'],
//   ['jj', 'simcha'],
//   ['richard', 'christine']
// ]); // -> false

// ========================= Depth First =========================
// e = number of rivalries, n = number of people
// Time: O(e), Space: O(n)
const tolerantTeams = (rivalries) => {
  const graph = buildGraph(rivalries);
  const teams = {};
  
  for (let player in graph) {
    if (!(player in teams)) {
      if (!setTeams(graph, teams, player, true)) return false;
    }
  }

  return true;
};

const buildGraph = (rivalries) => {
  const graph = {};

  for (let pair of rivalries) {
    const [ player1, player2 ] = pair;

    if (!(player1 in graph)) graph[player1] = [];
    if (!(player2 in graph)) graph[player2] = [];
    graph[player1].push(player2);
    graph[player2].push(player1);
  }

  return graph;
};

const setTeams = (graph, teams, player, whichTeam) => {
  if (player in teams) return teams[player] === whichTeam;

  teams[player] = whichTeam;

  for (let rival of graph[player]) {
    if (!setTeams(graph, teams, rival, !whichTeam)) return false;
  }

  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #82 rare routing ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, rareRouting, that takes in a number of cities (n) and a two
// dimensional array where each subarray represents a direct road that connects
// a pair of cities. The function should return a boolean indicating whether or
// not there exists a unique route for every pair of cities. A route is a
// sequence of roads that does not visit a city more than once.
// Cities will be numbered 0 to n - 1.
// You can assume that all roads are two-way roads. This means if there is a
// road between A and B, then you can use that road to go from A to B or go from
// B to A.
// For example, given these roads:
// 0 --- 1
// | \
// |  \
// |   \
// 2    3
// There is a unique route for between every pair of cities.
// So the answer is true.
// For example, given these roads:
// 0 --- 1
// | \
// |  \
// |   \
// 2 -- 3
// There are two routes that can be used to travel from city 1 to city 2:
// - first route:  1, 0, 2
// - second route: 1, 0, 3, 2 
// The answer is false, because routes should be unique.
//
// test_00:
// rareRouting(4, [
//   [0, 1],
//   [0, 2],
//   [0, 3]
// ]); // -> true
// test_01:
// rareRouting(4, [
//   [0, 1],
//   [0, 2],
//   [0, 3],
//   [3, 2]
// ]); // -> false
// test_02:
// rareRouting(6, [
//   [1, 2],
//   [5, 4],
//   [3, 0],
//   [0, 1],
//   [0, 4],
// ]); // -> true
// test_03:
// rareRouting(6, [
//   [1, 2],
//   [4, 1],
//   [5, 4],
//   [3, 0],
//   [0, 1],
//   [0, 4],
// ]); // -> false
// test_04:
// rareRouting(4, [
//   [0, 1],
//   [3, 2],
// ]); // -> false

// ========================= Depth First =========================
// Time: O(n^2), Space: O(n)
const rareRouting = (n, roads) => {
  const graph = buildGraph(roads);
  const visited = new Set();
  const traversable = traverse(graph, 0, visited, null);

  return traversable && visited.size === n;
};

const buildGraph = (roads) => {
  const graph = {};

  for (let pair of roads) {
    const [ city1, city2 ] = pair;

    if (!(city1 in graph)) graph[city1] = [];
    if (!(city2 in graph)) graph[city2] = [];
    graph[city1].push(city2);
    graph[city2].push(city1);
  }

  return graph;
};

const traverse = (graph, city, visited, lastCity) => {
  if (visited.has(city)) return false;

  visited.add(city);
  for (let neighbor of graph[city]) {
    if (lastCity !== neighbor) {
      if (!traverse(graph, neighbor, visited, city)) return false;
    }
  }

  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #83 max increasing subsequence ]]]]]]]]]]]]]]]]]]]]]]]]] !I
// Write a function, maxIncreasingSubseq, that takes in an array of numbers as
// an argument. The function should return the length of the longest subsequence
// of strictly increasing numbers.
// A subsequence of an array can be created by deleting any elements of the
// array, while maintaining the relative order of elements.
//
// test_00:
// const numbers = [4, 18, 20, 10, 12, 15, 19];
// maxIncreasingSubseq(numbers); // -> 5
// test_01:
// const numbers = [12, 9, 2, 5, 4, 32, 90, 20];
// maxIncreasingSubseq(numbers); // -> 4
// test_02:
// const numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70];
// maxIncreasingSubseq(numbers); // -> 5
// test_03:
// const numbers = [7, 14, 10, 12];
// maxIncreasingSubseq(numbers); // -> 3
// test_04:
// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21];
// maxIncreasingSubseq(numbers); // -> 21
// test_05:
// const numbers = [
//   1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
//   104,
// ];
// maxIncreasingSubseq(numbers); // -> 23
// test_06:
// const numbers = [
//   1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
//   17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
// ];
// maxIncreasingSubseq(numbers); // -> 27

// ========================= Depth First =========================
// Time: O(n^2), Space: O(n^2)
const maxIncreasingSubseq = (numbers, i = 0, lastNum = -Infinity, memo = {}) => {
  const key = i + '-' + lastNum;
  if (key in memo) return memo[key];
  if (i === numbers.length) return 0;

  const options = [];
  const withoutFirst = maxIncreasingSubseq(numbers, i + 1, lastNum, memo);
  options.push(withoutFirst);

  const firstNum = numbers[i];
  if (firstNum > lastNum) {
    const withFirst = 1 + maxIncreasingSubseq(numbers, i + 1, firstNum, memo);
    options.push(withFirst);
  }

  memo[key] = Math.max(...options);
  return memo[key];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #84 positioning plants ]]]]]]]]]]]]]]]]]]]]]]]]]
// You've been hired to plant flowers in a garden with n different positions.
// There are m different flower types. The prices of flowers types vary depending
// on which position they are planted. Your bosses are picky, they tell you to
// never plant two of the same flower type right next to each other. What is the
// minimum cost we need to plant a flower in each position of the garden?
// Write a function, positioningPlants, that takes in a 2D array with dimensions
// n * m. Each row of the array represents the costs of the flower types at that
// position. This means that costs[i][j] represents the cost of planting flower
// type j at position i. For example:
// Given these costs,
// costs = [
//   [4, 3, 7],
//   [6, 1, 9],
//   [2, 5, 3]
// ]
// The costs of plants at position 1 are $6, $1, and $9.
// The cost of planting flower type 0 at position 1 is $6.
// The cost of planting flower type 2 at position 1 is $9.
// The function should return the minimum cost of planting flowers without placing the same flower type in adjacent positions.
//
// test_00:
// positioningPlants([
//   [4, 3, 7],
//   [6, 1, 9],
//   [2, 5, 3]
// ]); // -> 7, by doing 4 + 1 + 2.
// test_01:
// positioningPlants([
//   [12, 14, 5],
//   [6, 3, 2]
// ]); // -> 8
// test_02:
// positioningPlants([
//   [12, 14, 5],
//   [6, 3, 2],
//   [4, 2, 7],
//   [4, 8, 4],
//   [1, 13, 5],
//   [8, 6, 7],
// ]); // -> 23
// test_03:
// positioningPlants([
//   [12, 14, 5, 13],
//   [6, 3, 20, 3],
//   [24, 12, 7, 2],
//   [4, 80, 45, 3],
//   [104, 13, 5, 14],
//   [38, 19, 7, 6],
//   [12, 2, 1, 2],
// ]); // -> 26
// test_04:
// positioningPlants([
//   [12, 14, 50, 12],
//   [6, 3, 20, 3],
//   [24, 12, 7, 2],
//   [4, 80, 45, 3],
//   [104, 13, 5, 14],
//   [38, 19, 7, 6],
//   [1, 20, 1, 2],
//   [13, 12, 5, 13],
//   [60, 32, 20, 3],
//   [24, 12, 7, 2],
//   [4, 80, 44, 1],
//   [104, 13, 5, 14],
//   [38, 19, 76, 6],
//   [12, 23, 12, 20],
//   [1, 3, 1, 1],
//   [1, 2, 12, 5],
// ]); // -> 74
// test_05:
// positioningPlants([
//   [12, 14, 50, 12, 13],
//   [6, 3, 20, 3, 16],
//   [24, 12, 7, 2, 74],
//   [4, 80, 45, 3, 100],
//   [104, 13, 5, 14, 3],
//   [38, 19, 7, 6, 24],
//   [1, 20, 1, 2, 31],
//   [13, 12, 5, 13, 9],
//   [60, 32, 20, 3, 2],
//   [24, 12, 7, 2, 42],
//   [4, 80, 44, 1, 23],
//   [104, 13, 5, 14, 28],
//   [38, 19, 76, 6, 12],
//   [12, 23, 12, 20, 13],
//   [1, 3, 1, 1, 50],
//   [1, 2, 12, 5, 36],
//   [6, 2, 3, 12, 20],
//   [4, 6, 4, 11, 15],
// ]); // -> 75

// ========================= Depth First =========================
// Time: O(nm), Space: O(nm)
const positioningPlants = (costs, pos = 0, type = null, memo = {}) => {
  const key = pos + '-' + type;
  if (key in memo) return memo[key];
  if (pos === costs.length) return 0;

  const options = [];
  for (let i = 0; i < costs[pos].length; i++) {
    if (i !== type) {
      options.push(costs[pos][i] + positioningPlants(costs, pos + 1, i, memo));
    }
  }

  memo[key] = Math.min(...options);
  return memo[key];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #85 breaking boundaries ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, breakingBoundaries, that takes in 5 arguments: a number of
// rows (m), a number of columns (n), a number of moves (k), a starting row (r),
// and a starting column (c). Say you were situated in a grid with dimensions
// m * n. If you had to start at position (r,c), in how many different ways could
// you move out of bounds if you could take at most k moves. A single move is
// moving one space up, down, left, or right. During a path you may revisit a
// position.
// For example:
// Given m, n, k, r, c:
// 3, 4, 2, 0, 0
// This input asks us to count the numbers of ways
// to move out of bounds in a 3 by 4 grid, starting at
// position (0, 0) if we could take at most 2 moves.
// The answer is 4 because of these 4 distinct ways:
//  1. left
//  2. up
//  3. right, up
//  4. down, left
// The function should return a number representing how many ways you can move
// out of bounds.
//
// test_00:
// breakingBoundaries(3, 4, 2, 0, 0); // -> 4
// test_01:
// breakingBoundaries(2, 2, 2, 1, 1); // -> 6
// test_02:
// breakingBoundaries(3, 4, 3, 0, 0); // -> 11
// test_03:
// breakingBoundaries(4, 4, 5, 2, 1); // -> 160
// test_04:
// breakingBoundaries(5, 6, 9, 2, 5); // -> 11635
// test_05:
// breakingBoundaries(6, 6, 12, 3, 4); // -> 871065
// test_06:
// breakingBoundaries(6, 6, 15, 3, 4); // -> 40787896
// test_07:
// breakingBoundaries(6, 8, 16, 2, 1); // -> 137495089

// ========================= Depth First =========================
// Time: O(nmk), Space: O(nmk)
const breakingBoundaries = (m, n, k, r, c, memo = {}) => {
  const key = k + '-' + r + '-' + c;
  if (key in memo) return memo[key];
  if (r < 0 || r === m) return 1;
  if (c < 0 || c === n) return 1;
  if (k === 0) return 0;
  
  let numMoves = 0;
  numMoves += breakingBoundaries(m, n, k - 1, r - 1, c, memo);
  numMoves += breakingBoundaries(m, n, k - 1, r + 1, c, memo);
  numMoves += breakingBoundaries(m, n, k - 1, r, c - 1, memo);
  numMoves += breakingBoundaries(m, n, k - 1, r, c + 1, memo);
  
  memo[key] = numMoves;
  return memo[key];
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #86 merge sort ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, mergeSort, that takes in an array of numbers as an argument.
// The function should return return a new array containing elements of the
// original array sorted in ascending order. Your function must implement the
// merge sort algorithm.
//
// test_00
// const numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40];
// mergeSort(numbers);
// // -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 
// test_01
// const numbers = [7, -30, -4, -1, 12, 0, 20];
// mergeSort(numbers);
// // -> [ -30, -4, -1, 0, 7, 12, 20 ] 
// test_02
// const numbers = [8, 7, 6, 5, 4, 3, 2, 1, 0];
// mergeSort(numbers);
// // -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] 
// test_03
// const numbers = [ 
//   72, 42, 16, 81, 84, 17,  2, 81, 22, 79, 86, 38, 
//   77, 80, 81, 70, 81, 80, 35, 21, 89, 38, 57, 28, 
//    4, 17, 50, 38, 68, 82, 22, 76, 45, 40, 67, 94, 
//   37, 27, 81, 53, 36, 18, 28, 60, 45, 74, 40, 29, 
//   18,  6, 28, 57, 42, 60, 64, 12, 78, 97, 96,  1, 
//   20, 20, 61, 67, 82, 10, 63, 71, 39, 52, 37, 69, 
//   37, 24, 66, 74, 15, 92, 49, 31, 56, 67, 50, 57, 
//   79,  0, 21, 56, 82, 22,  4, 20, 91, 72, 58, 93, 
//   99, 14, 42, 91 
// ];
// mergeSort(numbers);
// // -> [ 
// //    0,  1,  2,  4,  4,  6, 10, 12, 14, 15, 16, 17, 
// //   17, 18, 18, 20, 20, 20, 21, 21, 22, 22, 22, 24, 
// //   27, 28, 28, 28, 29, 31, 35, 36, 37, 37, 37, 38, 
// //   38, 38, 39, 40, 40, 42, 42, 42, 45, 45, 49, 50, 
// //   50, 52, 53, 56, 56, 57, 57, 57, 58, 60, 60, 61, 
// //   63, 64, 66, 67, 67, 67, 68, 69, 70, 71, 72, 72, 
// //   74, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81, 81, 
// //   81, 81, 82, 82, 82, 84, 86, 89, 91, 91, 92, 93, 
// //   94, 96, 97, 99 
// // ]
// test_04
// const numbers = new Array(95000).fill(7);
// mergeSort(numbers);
// // -> [7, 7, 7, 7, 7, ...]
// test_05
// const numbers = new Array(120000).fill(7);
// mergeSort(numbers);
// // -> [7, 7, 7, 7, 7, ...]

// ========================= Merge Sort =========================
// Time: O(n*log(n)), Space: O(n)
const mergeSort = (nums) => {
  if (nums.length < 2) return nums;
  
  const middle = Math.floor(nums.length / 2);
  const left = mergeSort(nums.slice(0, middle));
  const right = mergeSort(nums.slice(middle));
  
  return merge(left, right);
};

const merge = (left, right) => {
  const mergedArray = [];
  let leftIdx = 0;
  let rightIdx = 0;
  
  while (leftIdx < left.length && rightIdx < right.length) {
    let leftNum = left[leftIdx];
    let rightNum = right[rightIdx];
    
    if (leftNum < rightNum) {
      mergedArray.push(leftNum);
      leftIdx++;
    } else {
      mergedArray.push(rightNum);
      rightIdx++;
    }
  }
  
  while (leftIdx < left.length) {
    mergedArray.push(left[leftIdx]);
    leftIdx++;
  }
  
  while (rightIdx < right.length) {
    mergedArray.push(right[rightIdx]);
    rightIdx++;
  }
  
  return mergedArray;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #87 combine intervals ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, combineIntervals, that takes in an an array of intervals as
// an argument. Each interval is an array containing a pair of numbers
// representing a start and end time. Your function should combine overlapping
// intervals and return an array containing the combined intervals.
// For example:
// Given two intervals:
// [1, 4] and [3, 7]
// The intervals overlap and
// should be combined into:
// [1, 7]
// You may return the combined intervals in any order.
// You can assume that the input array contains at least one interval and all intervals are valid with start < end.
//
// test_00
// const intervals = [
//   [1, 4],
//   [12, 15],
//   [3, 7],
//   [8, 13],
// ];
// combineIntervals(intervals);
// // -> [ [1, 7], [8, 15] ]
// test_01
// const intervals = [
//   [6, 8],
//   [2, 9],
//   [10, 12],
//   [20, 24],
// ];
// combineIntervals(intervals);
// // -> [ [2, 9], [10, 12], [20, 24] ]
// test_02
// const intervals = [
//   [3, 7],
//   [5, 8],
//   [1, 5],
// ];
// combineIntervals(intervals);
// // -> [ [1, 8] ]
// test_03
// const intervals = [
//   [3, 7],
//   [10, 13],
//   [5, 8],
//   [27, 31],
//   [1, 5],
//   [12, 16],
//   [20, 22],
// ];
// combineIntervals(intervals);
// // -> [ [1, 8], [10, 16], [20, 22], [27, 31] ]
// test_04
// const intervals = [
//   [3, 7],
//   [10, 13],
//   [5, 8],
//   [27, 31],
//   [1, 5],
//   [12, 16],
//   [20, 32],
// ];
// combineIntervals(intervals);
// // -> [ [1, 8], [10, 16], [20, 32] ]
// test_05
// const intervals = [
//   [64, 70],
//   [50, 55],
//   [62, 65],
//   [12, 50],
//   [72, 300000],
// ];
// combineIntervals(intervals);
// // -> [ [12, 55], [62, 70], [72, 300000] ]

// Time: O(n*log(n)), Space: O(n)
const combineIntervals = (intervals) => {
  const sortedIntervals = intervals.sort((a, b) => a[0] - b[0]);
  const combinedIntervals = [sortedIntervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const currInterval = intervals[i]
    const [start, end] = [currInterval[0], currInterval[1]]
    const len = combinedIntervals.length - 1
    const lastInterval = combinedIntervals[len]
    if (start <= lastInterval[1]) {
      lastInterval[1] = end < lastInterval[1] ? lastInterval[1] : end
    } else {
      combinedIntervals.push(currInterval)
    }
  }

  return combinedIntervals;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #88 binary search ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, binarySearch, that takes in a sorted array of numbers and a
// target. The function should return the index where the target can be found
// within the array. If the target is not found in the array, then return -1.
// You may assume that the input array contains unique numbers sorted in
// increasing order.
// Your function must implement the binary search algorithm.
//
// test_00
// binarySearch([0, 1, 2, 3, 4, 5, 6, 7, 8], 6); // -> 6
// test_01
// binarySearch([0, 6, 8, 12, 16, 19, 20, 24, 28], 27); // -> -1
// test_02
// binarySearch([0, 6, 8, 12, 16, 19, 20, 28], 8); // -> 2
// test_03
// binarySearch([0, 6, 8, 12, 16, 19, 20, 24, 28], 28); // -> 8
// test_04
// binarySearch([7, 9], 7); // -> 0
// test_05
// binarySearch([7, 9], 9); // -> 1
// test_06
// binarySearch([7, 9], 12); // -> -1
// test_07
// binarySearch([7], 7); // -> 0
// test_08
// binarySearch([], 7); // -> -1

// ========================= Iterative =========================
// Time: O(log(n)), Space: O(1)
const binarySearch = (numbers, target) => {
  let lo = 0
  let hi = numbers.length - 1;
  
  while (lo <= hi) {
    const mid = Math.floor((lo + hi) / 2);
    const num = numbers[mid];
    if (target < num) {
      hi = mid - 1;
    } else if (target > num) {
      lo = mid + 1;
    } else {
      return mid;
    }
  }

  return -1;
};

// ========================= Recursive =========================
// Time: O(log(n)), Space: O(log(n))
const binarySearch = (numbers, target) => {
  if (!numbers.length) return -1;

  const midIdx = Math.floor(numbers.length / 2);
  const num = numbers[midIdx];
  
  if (num === target) {
    return midIdx;
  } else if (num < target) {
    const rightSearch = binarySearch(numbers.slice(midIdx + 1), target);
    return rightSearch === -1 ? -1 : midIdx + rightSearch + 1;
  } else {
    return binarySearch(numbers.slice(0, midIdx), target);
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #89 binary search tree includes ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, binarySearchTreeIncludes, that takes in the root of a binary
// search tree containing numbers and a target value. The function should return
// a boolean indicating whether or not the target is found within the tree.
// A Binary Search Tree is a binary tree where all values within a node's left
// subtree are smaller than the node's value and all values in a node's right
// subtree are greater than or equal to the node's value.
// Your solution should have a best case runtime of O(log(n)).
// tree a
// const a = new Node(12);
// const b = new Node(5);
// const c = new Node(18);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(19);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      12
//    /   \
//   5     18
//  / \     \
// 3   9     19
//
// test_00:
// binarySearchTreeIncludes(a, 9); // -> true
// test_01:
// binarySearchTreeIncludes(a, 15); // -> false
// test_02:
// binarySearchTreeIncludes(a, 1); // -> false
// test_03:
// binarySearchTreeIncludes(a, 12); // -> true
// tree q
// const q = new Node(54);
// const r = new Node(42);
// const s = new Node(70);
// const t = new Node(31);
// const u = new Node(50);
// const v = new Node(72);
// const w = new Node(47);
// const x = new Node(90);
// q.left = r;
// q.right = s;
// r.left = t;
// r.right = u;
// s.right = v;
// u.left = w;
// v.right = x;
//       54
//     /    \
//    42     70
//   / \      \
// 31   50     72
//     /        \
//    47         90
// test_04:
// binarySearchTreeIncludes(q, 55); // -> false
// test_05:
// binarySearchTreeIncludes(q, 47); // -> true
// test_06:
// binarySearchTreeIncludes(q, 49); // -> false
// test_07:
// binarySearchTreeIncludes(q, 70); // -> true
// test_08:
// binarySearchTreeIncludes(q, 100); // -> false

// ========================= Iterative =========================
// Best Case (Balanced Tree; Minimal Height)
// Time: O(log(n)), Space: O(1)
// Worst Case (Maximum Height)
// Time: O(n), Space: O(1)
const binarySearchTreeIncludes = (root, target) => {
  let current = root;

  while (current !== null) {
    if (current.val === target) return true;
    if (target > current.val) {
      current = current.right;
    } else {
      current = current.left;
    }
  }

  return false;
};

// ========================= Recursive =========================
// Best Case (Balanced Tree; Minimal Height)
// Time: O(log(n)), Space: O(log(n))
// Worst Case (Maximum Height)
// Time: O(n), Space: O(n)
const binarySearchTreeIncludes = (root, target) => {
  if (root === null) return false;
  if (root.val === target) return true;

  if (target > root.val) {
    return binarySearchTreeIncludes(root.right, target);
  } else {
    return binarySearchTreeIncludes(root.left, target);
  }
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #90 is binary search tree ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, isBinarySearchTree, that takes in the root of a binary tree.
// The function should return a boolean indicating whether or not the tree
// satisfies the binary search tree property.
// A Binary Search Tree is a binary tree where all values within a node's left
// subtree are smaller than the node's value and all values in a node's right
// subtree are greater than or equal to the node's value.
//
// test_00:
// const a = new Node(12);
// const b = new Node(5);
// const c = new Node(18);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(19);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      12
//    /   \
//   5     18
//  / \     \
// 3   9     19
// isBinarySearchTree(a); // -> true
// test_01:
// const a = new Node(12);
// const b = new Node(5);
// const c = new Node(18);
// const d = new Node(3);
// const e = new Node(15);
// const f = new Node(19);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      12
//    /   \
//   5     18
//  / \     \
// 3   15     19
// isBinarySearchTree(a); // -> false
// test_02:
// const a = new Node(12);
// const b = new Node(5);
// const c = new Node(19);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(19);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      12
//    /   \
//   5     19
//  / \     \
// 3   9     19
// isBinarySearchTree(a); // -> true
// test_03:
// const a = new Node(12);
// const b = new Node(5);
// const c = new Node(10);
// const d = new Node(3);
// const e = new Node(9);
// const f = new Node(19);
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
//      12
//    /   \
//   5     10
//  / \     \
// 3   9     19
// isBinarySearchTree(a); // -> false
// test_04:
// const q = new Node(54);
// const r = new Node(42);
// const s = new Node(70);
// const t = new Node(31);
// const u = new Node(50);
// const v = new Node(72);
// const w = new Node(47);
// const x = new Node(90);
// q.left = r;
// q.right = s;
// r.left = t;
// r.right = u;
// s.right = v;
// u.left = w;
// v.right = x;
//       54
//     /    \
//    42     70
//   / \      \
// 31   50     72
//     /        \
//    47         90
// isBinarySearchTree(q); // -> true

// ========================= In Order DF Traversal =========================
// Time: O(n), Space: O(n)
const isBinarySearchTree = (root) => {
  const values = [];
  inOrderTraversal(root, values);
  return isSorted(values);
};

const inOrderTraversal = (root, values) => {
  if (root === null) return null;
  inOrderTraversal(root.left, values);
  values.push(root.val);
  inOrderTraversal(root.right, values);
};

const isSorted = (values) => {
  for (let i = 0; i < values.length - 1; i++) {
    if (values[i] > values[i + 1]) return false;
  }
  return true;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #91 post order ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, postOrder, that takes in the root of a binary tree. The
// function should return an array containing the post-ordered values of the tree.
// Post-order traversal is when nodes are recursively visited in the order:
// left child, right child, self.
//
// test_00:
// const x = new Node('x');
// const y = new Node('y');
// const z = new Node('z');
// x.left = y;
// x.right = z;
//       x
//    /    \
//   y      z
// postOrder(x);
// ['y', 'z', 'x']
// test_01:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.left = f;
// c.right = g;
//      a
//    /    \
//   b      c
//  / \    / \
// d   e  f   g
// postOrder(a);
// [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
// test_02:
// const a = new Node('a');
// const b = new Node('b');
// const c = new Node('c');
// const d = new Node('d');
// const e = new Node('e');
// const f = new Node('f');
// const g = new Node('g');
// const h = new Node('h');
// a.left = b;
// a.right = c;
// b.left = d;
// b.right = e;
// c.right = f;
// e.left = g;
// e.right = h;
//      a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
// postOrder(a);
// [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
// test_03:
// const l = new Node('l');
// const m = new Node('m');
// const n = new Node('n');
// const o = new Node('o');
// const p = new Node('p');
// const q = new Node('q');
// const r = new Node('r');
// const s = new Node('s');
// const t = new Node('t');
// l.left = m;
// l.right = n;
// n.left = o;
// n.right = p;
// o.left = q;
// o.right = r;
// p.left = s;
// p.right = t;
//        l
//     /     \
//    m       n
//         /    \
//         o     p
//        / \   / \
//       q   r s   t
// postOrder(l);
// [ 'm', 'q', 'r', 'o', 's', 't', 'p', 'n', 'l' ] 
// test_04:
// postOrder(null);
// []

// ========================= Post Order DF Traversal =========================
// Time: O(n), Space: O(n)
const postOrder = (root) => {
  const values = [];
  postOrderTraversal(root, values);
  return values;
};

const postOrderTraversal = (root, values) => {
  if (root === null) return null;
  postOrderTraversal(root.left, values);
  postOrderTraversal(root.right, values);
  values.push(root.val);
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #92 build tree in post ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, buildTreeInPost, that takes in an array of in-ordered values
// and an array of post-ordered values for a binary tree. The function should
// build a binary tree that has the given in-order and post-order traversal
// structure. The function should return the root of this tree.
// You can assume that the values of inorder and postorder are unique.
//
// test_00
// buildTreeInPost(
//   [ 'y', 'x', 'z' ],
//   [ 'y', 'z', 'x' ] 
// );
//       x
//    /    \
//   y      z
// test_01
// buildTreeInPost(
//   [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
//   [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
// );
//      a
//    /    \
//   b      c
//  / \    / \
// d   e  f   g
// test_02
// buildTreeInPost(
//   [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
//   [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
// );
//      a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
// test_03
// buildTreeInPost(
//   ['m', 'n'],
//   ['m', 'n']
// );
//       n
//     /
//    m
// test_04
// buildTreeInPost(
//   ['n', 'm'],
//   ['m', 'n']
// );
//     n
//      \
//       m

// ========================= Recursive =========================
// Time: O(n^2), Space: O(n^2)
const buildTreeInPost = (inOrder, postOrder) => {
  if (!inOrder.length) return null;
  const rootVal = postOrder[postOrder.length - 1];
  const root = new Node(rootVal);
  const idx = inOrder.indexOf(rootVal);
  const leftInOrder = inOrder.slice(0, idx)
  const leftPostOrder = postOrder.slice(0, idx);
  const rightInOrder = inOrder.slice(idx + 1);
  const rightPostOrder = postOrder.slice(idx, -1);
  root.left = buildTreeInPost(leftInOrder, leftPostOrder);
  root.right = buildTreeInPost(rightInOrder, rightPostOrder);
  return root;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #93 build tree in pre ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, buildTreeInPre, that takes in an array of in-ordered values
// and an array of pre-ordered values for a binary tree. The function should
// build a binary tree that has the given in-order and pre-order traversal
// structure. The function should return the root of this tree.
// You can assume that the values of inorder and preorder are unique.
//
// test_00
// buildTreeInPre(
//   [ 'z', 'y', 'x' ],
//   [ 'y', 'z', 'x' ] 
// );
//       y
//    /    \
//   z      x
// test_01
// buildTreeInPre(
//   [ 'y', 'z', 'x' ],
//   [ 'y', 'x', 'z' ] 
// );
//       y
//        \
//         x
//        / 
//       z
// test_02
// buildTreeInPre(
//   [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
//   [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
// );
//       a
//    /    \
//   b      c
//  / \      \
// d   e      f
//    / \
//    g  h
// test_03
// buildTreeInPre(
//   [ 't', 'u', 's', 'q', 'r', 'p' ],
//   [ 'u', 't', 's', 'r', 'q', 'p' ] 
// );
//     u
//  /    \
// t      s
//         \
//         r
//        / \
//        q  p
// test_04
// buildTreeInPre(
//   [ 'm', 'l', 'q', 'o', 'r', 'n', 's', 'p', 't' ],
//   [ 'l', 'm', 'n', 'o', 'q', 'r', 'p', 's', 't' ] 
// );
//        l
//     /     \
//    m       n
//         /    \
//         o     p
//        / \   / \
//       q   r s   t

// ========================= Recursive (Slicing) =========================
// Time: O(n^2), Space: O(n^2)
const buildTreeInPre = (inOrder, preOrder) => {
  if (!inOrder.length) return null;
  const rootVal = preOrder[0];
  const root = new Node(rootVal);
  const idx = inOrder.indexOf(rootVal);
  const leftInOrder = inOrder.slice(0, idx);
  const rightInOrder = inOrder.slice(idx + 1);
  const leftPreOrder = preOrder.slice(1, idx + 1);
  const rightPreOrder = preOrder.slice(idx + 1);
  root.left = buildTreeInPre(leftInOrder, leftPreOrder);
  root.right = buildTreeInPost(rightInOrder, rightPreOrder);
  return root;
};

// ========================= Recursive (In-Place) =========================
// Time: O(n), Space: O(n)
const buildTreeInPre = (
  inOrder, 
  preOrder, 
  inOrderStart = 0, 
  inOrderEnd = inOrder.length - 1,
  preOrderStart = 0,
  preOrderEnd = preOrder.length - 1
  ) => {
    if (inOrderEnd < inOrderStart) return null;
    const rootVal = preOrder[preOrderStart];
    const root = new Node(rootVal);
    const idx = inOrder.indexOf(rootVal);
    const leftSize = idx - inOrderStart;
    root.left = buildTreeInPre(
      inOrder,
      preOrder,
      inOrderStart,
      idx - 1,
      preOrderStart + 1,
      preOrderStart + leftSize
    );
    root.right = buildTreeInPre(
      inOrder, 
      preOrder, 
      idx + 1, 
      inOrderEnd, 
      preOrderStart + leftSize + 1, 
      preOrderEnd
    );
    return root;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #94 lexical order ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, lexicalOrder, that takes in 2 words and an alphabet string
// as an argument. The function should return true if the first word should
// appear before the second word if lexically-ordered according to the given
// alphabet order. If the second word should appear first, then return false.
// Note that the alphabet string may be any arbitrary string.
// Intuitively, Lexical Order is like "dictionary" order:
// You can assume that all characters are lowercase a-z.
// You can assume that the alphabet contains all 26 letters.
//
// test_00:
// const alphabet = "abcdefghijklmnopqrstuvwxyz";
// lexicalOrder("apple", "dock", alphabet); // -> true
// test_01:
// const alphabet = "abcdefghijklmnopqrstuvwxyz";
// lexicalOrder("apple", "ample", alphabet); // -> false
// test_02:
// const alphabet = "abcdefghijklmnopqrstuvwxyz";
// lexicalOrder("app", "application", alphabet); // -> true
// test_03:
// const alphabet = "abcdefghijklmnopqrstuvwxyz";
// lexicalOrder("backs", "backdoor", alphabet); // -> false
// test_04:
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// lexicalOrder("zoo", "dinner", alphabet); // -> true
// test_05:
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// lexicalOrder("leaper", "leap", alphabet); // -> false
// test_06:
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// lexicalOrder("backs", "backdoor", alphabet); // -> true
// test_07:
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// lexicalOrder("semper", "semper", alphabet); // -> true

// ========================= Iterative =========================
// Time: O(min(n, m)), Space: O(1)
const lexicalOrder = (word1, word2, alphabet) => {
  let i = 0;

  while (i < Math.min(word1.length, word2.length)) {
    const char1 = word1[i];
    const char2 = word2[i];
    const idx1 = alphabet.indexOf(char1);
    const idx2 = alphabet.indexOf(char2);
    if (idx1 < idx2) {
      return true;
    } else if (idx1 === idx2) {
      i++;
    } else {
      return false;
    }
  }

  return word1.length <= word2.length;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #95 detect dictionary ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, detectDictionary, that takes in a dictionary of words and
// an alphabet string. The function should return a boolean indicating whether
// or not all words of the dictionary are lexically-ordered according to the
// alphabet.
// You can assume that all characters are lowercase a-z.
// You can assume that the alphabet contains all 26 letters.
//
// test_00:
// const dictionary = ["zoo", "tick", "tack", "door"];
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// detectDictionary(dictionary, alphabet); // -> true
// test_01:
// const dictionary = ["zoo", "tack", "tick", "door"];
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// detectDictionary(dictionary, alphabet); // -> false
// test_02:
// const dictionary = ["zoos", "zoo", "tick", "tack", "door"];
// const alphabet = "ghzstijbacdopnfklmeqrxyuvw";
// detectDictionary(dictionary, alphabet); // -> false
// test_03:
// const dictionary = ["miles", "milestone", "proper", "process", "goal"];
// const alphabet = "mnoijpqrshkltabcdefguvwzxy";
// detectDictionary(dictionary, alphabet); // -> true
// test_04:
// const dictionary = ["miles", "milestone", "pint", "proper", "process", "goal"];
// const alphabet = "mnoijpqrshkltabcdefguvwzxy";
// detectDictionary(dictionary, alphabet); // -> true
// test_05:
// const dictionary = ["miles", "milestone", "pint", "proper", "process", "goal", "apple"];
// const alphabet = "mnoijpqrshkltabcdefguvwzxy";
// detectDictionary(dictionary, alphabet); // -> false

// ========================= Iterative =========================
// n: num words, k: length of longest word
// Time: O(nk), Space: O(1)
const detectDictionary = (dictionary, alphabet) => {
  for (let i = 0; i < dictionary.length - 1; i++) {
    const word1 = dictionary[i];
    const word2 = dictionary[i + 1];
    const ordered = lexicalOrder(word1, word2, alphabet);
    if (!ordered) return false;
  }
  return true;
};

const lexicalOrder = (word1, word2, alphabet) => {
  let i = 0;

  while (i < Math.min(word1.length, word2.length)) {
    const char1 = word1[i];
    const char2 = word2[i];
    const idx1 = alphabet.indexOf(char1);
    const idx2 = alphabet.indexOf(char2);
    if (idx1 < idx2) {
      return true;
    } else if (idx1 === idx2) {
      i++;
    } else {
      return false;
    }
  }

  return word1.length <= word2.length;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #96 topological order ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, topologicalOrder, that takes in an object representing the
// adjacency list for a directed-acyclic graph. The function should return an
// array containing the topological-order of the graph.
// The topological ordering of a graph is a sequence where "parent nodes" appear
// before their "children" within the sequence.
//
// test_00:
// topologicalOrder({
//   a: ["f"],
//   b: ["d"],
//   c: ["a", "f"],
//   d: ["e"],
//   e: [],
//   f: ["b", "e"],
// }); // -> ['c', 'a', 'f', 'b', 'd', 'e']
// test_01:
// topologicalOrder({
//   h: ["l", "m"],
//   i: ["k"],
//   j: ["k", "i"],
//   k: ["h", "m"],
//   l: ["m"],
//   m: [],
// }); // -> ['j', 'i', 'k', 'h', 'l', 'm']
// test_02:
// topologicalOrder({
//   q: [],
//   r: ["q"],
//   s: ["r"],
//   t: ["s"],
// }); // -> ['t', 's', 'r', 'q']
// test_03:
// topologicalOrder({
//   v: ["z", "w"],
//   w: [],
//   x: ["w", "v", "z"],
//   y: ["x"],
//   z: ["w"],
// }); // -> ['y', 'x', 'v', 'z', 'w']

// ========================= Topological Order =========================
// n: num nodes, e: num edges
// Time: O(n+e), Space: O(n)
const topologicalOrder = (graph) => {
  const numParents = {};
  for (let node in graph) {
    numParents[node] = 0;
  }
  for (let node in graph) {
    for (let neighbor of graph[node]) {
      numParents[neighbor]++;
    }
  }
  
  const topMost = [];
  for (let node in numParents) {
    if (numParents[node] === 0) topMost.push(node);
  }

  const ordered = [];
  while (topMost.length) {
    const node = topMost.pop();
    ordered.push(node);
    for (let neighbor of graph[node]) {
      numParents[neighbor]--;
      if (numParents[neighbor] === 0) topMost.push(neighbor);
    }
  }
  return ordered;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #97 safe cracking ]]]]]]]]]]]]]]]]]]]]]]]]]
// Oh-no! You forgot the number combination that unlocks your safe. Luckily, you
// knew that you'd be forgetful so you previously wrote down a bunch of hints
// that can be used to determine the correct combination. Each hint is a pair of
// numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not
// necessarily immediately before y).
// The keypad on the safe has digits 0-9. You can assume that the hints will
// generate exactly one working combination and that a digit can occur zero or
// one time in the answer.
// Write a function, safeCracking, that takes in an array of hints as an argument
// and determines the combination that will unlock the safe. The function should
// return a string representing the combination.
//
// test_00:
// safeCracking([
//   [7, 1],
//   [1, 8],
//   [7, 8],
// ]); // -> '718'
// test_01:
// safeCracking([
//   [3, 1],
//   [4, 7],
//   [5, 9],
//   [4, 3],
//   [7, 3],
//   [3, 5],
//   [9, 1],
// ]); // -> '473591'
// test_02:
// safeCracking([
//   [2, 5],
//   [8, 6],
//   [0, 6],
//   [6, 2],
//   [0, 8],
//   [2, 3],
//   [3, 5],
//   [6, 5],
// ]); // -> '086235'
// test_03:
// safeCracking([
//   [0, 1],
//   [6, 0],
//   [1, 8],
// ]); // -> '6018'
// test_04:
// safeCracking([
//   [8, 9],
//   [4, 2],
//   [8, 2],
//   [3, 8],
//   [2, 9],
//   [4, 9],
//   [8, 4],
// ]); // -> '38429'

// ========================= Topological Order =========================
// n: num nodes, e: num edges
// Time: O(n+e), Space: O(n)
const safeCracking = (hints) => {
  const graph = buildGraph(hints);
  const numParents = {};
  for (let node in graph) {
    numParents[node] = 0;
  }
  for (let node in graph) {
    for (let neighbor of graph[node]) {
      numParents[neighbor]++;
    }
  }

  const topMost = [];
  for (let node in numParents) {
    if (numParents[node] === 0) topMost.push(node);
  }

  const combination = '';
  while (topMost.length) {
    const current = topMost.pop();
    combination += current;
    for (let neighbor of graph[current]) {
      numParents[neighbor]--;
      if (numParents[neighbor] === 0) topMost.push(neighbor);
    }
  }

  return combination;
};

const buildGraph = (pairs) => {
  const graph = {};
  
  for (let pair of pairs) {
    const node1 = pair[0];
    const node2 = pair[1];
    if (node1 in graph) {
      graph[node1].push(node2);
    } else {
      graph[node1] = [node2];
    }
    if (!(node2 in graph)) {
      graph[node2] = [];
    }
  }

  return graph;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #98 string search ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, stringSearch, that takes in a grid of letters and a string
// as arguments. The function should return a boolean indicating whether or not
// the string can be found in the grid as a path by connecting horizontal or
// vertical positions. The path can begin at any position, but you cannot reuse
// a position more than once in the path.
// You can assume that all letters are lowercase and alphabetic.
//
// test_00:
// const grid = [
//   ['e', 'y', 'h', 'i', 'j'],
//   ['q', 'x', 'e', 'r', 'p'],
//   ['r', 'o', 'l', 'l', 'n'],
//   ['p', 'r', 'x', 'o', 'h'],
//   ['a', 'a', 'm', 'c', 'm']
// ];
// stringSearch(grid, 'hello'); // -> true
// test_01:
// const grid = [
//   ['e', 'y', 'h', 'i', 'j'],
//   ['q', 'x', 'e', 'r', 'p'],
//   ['r', 'o', 'l', 'l', 'n'],
//   ['p', 'r', 'x', 'o', 'h'],
//   ['a', 'a', 'm', 'c', 'm']
// ];
// stringSearch(grid, 'proxy'); // -> true
// test_02:
// const grid = [
//   ['e', 'y', 'h', 'i', 'j'],
//   ['q', 'x', 'e', 'r', 'p'],
//   ['r', 'o', 'l', 'l', 'n'],
//   ['p', 'r', 'x', 'o', 'h'],
//   ['a', 'a', 'm', 'c', 'm']
// ];
// stringSearch(grid, 'rolling'); // -> false
// test_03:
// const grid = [
//   ['e', 'y', 'h', 'i', 'j'],
//   ['q', 'x', 'e', 'r', 'p'],
//   ['r', 'o', 'l', 'l', 'n'],
//   ['p', 'r', 'x', 'o', 'h'],
//   ['a', 'a', 'm', 'z', 'm']
// ];
// stringSearch(grid, 'zoo'); // -> false
// test_04:
// const grid = [
//   ['q', 'w', 'h', 'i', 'j'],
//   ['q', 'e', 'r', 'o', 'p'],
//   ['h', 'y', 't', 'x', 'z'],
//   ['k', 'o', 'm', 'o', 'p']
// ];
// stringSearch(grid, 'qwerty'); // -> true
// test_05:
// const grid = [ 
//   [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
//   [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
//   [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
//   [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
//   [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
//   [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
//   [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
//   [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
//   [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
//   [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
// ];
// stringSearch(grid, 'paprika'); // -> true
// test_06:
// const grid = [
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
//     [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
// ];
// stringSearch(grid, 'sssssssh'); // -> false

// ========================= Depth First =========================
// r: num rows, c: num cols, s: length of string
// Time: O(s^(rc)), Space: O(rc) 
// Alvin says the time complexity is O(3^(rc)), but I disagree
const stringSearch = (grid, s) => {
  const visited = new Set();
  for (let row = 0; row < grid.length; row++) {
    for (let col = 0; col < grid[0].length; col++) {
      if (grid[row][col] === s[0]) {
        if (traverseWord(grid, row, col, s, 0, visited)) return true;
      }
    }
  }
  return false;
};

const traverseWord = (grid, row, col, s, i, visited) => {
  if (i === s.length - 1) return true;
  visited.add(row + '-' + col);
  
  const deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]];
  for (let delta of deltas) {
    const [deltaY, deltaX] = delta;
    const y = row + deltaY;
    const x = col + deltaX;
    const validY = y >= 0 && y < grid.length;
    const validX = x >= 0 && x < grid[0].length;
    if (validY && validX && grid[y][x] === s[i + 1] && !visited.has(y + '-' + x)) {
      if (traverseWord(grid, y, x, s, i + 1, visited)) return true;
    }
  }
  return false;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #99 token replace ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, tokenReplace, that takes in an object of tokens and a string.
// The function should return a new string where tokens are replaced.
// Tokens are enclosed in a pair of '$'. You can assume that the input string is
// properly formatted. Tokens should be replaced from left to right in the string
// (see test_05).
//
// test_00:
// const tokens = {
//   '$LOCATION$': 'park',
//   '$ANIMAL$': 'dog',
// };
// tokenReplace('Walk the $ANIMAL$ in the $LOCATION$!', tokens); 
// -> 'Walk the dog in the park!'
// test_01:
// const tokens = {
//   '$ADJECTIVE$': 'quick',
//   '$VERB$': 'hopped',
//   '$DIRECTION$': 'North'
// };
// tokenReplace('the $ADJECTIVE$ fox $VERB$ $ADJECTIVE$ly $DIRECTION$ward', tokens); 
// -> 'the quick fox hopped quickly Northward'
// test_02:
// const tokens = {
//   '$greeting$': 'hey programmer',
// };
// tokenReplace('his greeting is always $greeting$.', tokens); 
// -> 'his greeting is always hey programmer.'
// test_03:
// const tokens = {
//   '$A$': 'lions',
//   '$B$': 'tigers',
//   '$C$': 'bears',
// };
// tokenReplace('$A$$B$$C$, oh my.', tokens); 
// -> 'lionstigersbears, oh my.'
// test_04:
// const tokens = {
//   '$A$': 'lions',
//   '$B$': 'tigers',
//   '$C$': 'bears',
// };
// tokenReplace('$B$', tokens); 
// -> 'tigers'
// test_05:
// const tokens = {
//   '$second$': 'beta',
//   '$first$': 'alpha',
//   '$third$': 'gamma',
// };
// tokenReplace('$first$second$third$', tokens); 
// -> 'alphasecondgamma'

// ========================= 2 Pointers =========================
// Time: O(n), Space: O(n)
const tokenReplace = (s, tokens) => {
  let replaced = '';

  let i = 0;
  let j = 1;
  while (i < s.length) {
    if (s[i] !== '$') {
      replaced += s[i];
      i++;
      j = i + 1;
    } else if (s[j] !== '$') {
      j++;
    } else {
      const token = s.slice(i, j + 1);
      replaced += tokens[token];
      i = j + 1;
      j = i + 1;
    }
  }

  return replaced;
};

// [[[[[[[[[[[[[[[[[[[[[[[[[ #100 token transform ]]]]]]]]]]]]]]]]]]]]]]]]]
// Write a function, tokenTransform, that takes in an object of tokens and a
// string. In the object, the replacement values for a token may reference other
// tokens. The function should return a new string where tokens are replaced with
// their fully evaluated string values.
// Tokens are enclosed in a pair of '$'.
// You may assume that their are no circular token dependencies.
//
// test_00:
// const tokens = {
//   '$LOCATION$': '$ANIMAL$ park',
//   '$ANIMAL$': 'dog',
// };
// tokenTransform('Walk the $ANIMAL$ in the $LOCATION$!', tokens);
// -> 'Walk the dog in the dog park!'
// test_01:
// const tokens = {
//   '$ADJECTIVE_1$': "quick",
//   '$ADJECTIVE_2$': "eager",
//   '$ADVERBS$': "$ADJECTIVE_1$ly and $ADJECTIVE_2$ly",
//   '$VERB$': "hopped $DIRECTION$",
//   '$DIRECTION$': "North",
// };
// tokenTransform("the $ADJECTIVE_1$ fox $ADVERBS$ $VERB$ward", tokens);
// -> 'the quick fox quickly and eagerly hopped Northward'
// test_02:
// const tokens = {
//   '$B$': "epicly $C$",
//   '$A$': "pretty $B$ problem $D$",
//   '$D$': "we have",
//   '$C$': "clever",
// };
// tokenTransform("What a $A$ here!", tokens);
// -> 'What a pretty epicly clever problem we have here!'
// test_03:
// const tokens = {
//   '$1$': "a$2$",
//   '$2$': "b$3$",
//   '$3$': "c$4$",
//   '$4$': "d$5$",
//   '$5$': "e$6$",
//   '$6$': "f!",
// };
// tokenTransform("$1$ $1$ $1$ $1$ $1$ $1$ $4$ $4$", tokens);
// -> 'abcdef! abcdef! abcdef! abcdef! abcdef! abcdef! def! def!'
// test_04:
// const tokens = {
//   '$0$': "$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$$1$",
//   '$1$': "$2$$2$$2$$2$$2$$2$$2$$2$$2$",
//   '$2$': "$3$$3$$3$$3$$3$$3$$3$",
//   '$3$': "$4$$4$$4$$4$$4$$4$",
//   '$4$': "$5$$5$$5$$5$$5$",
//   '$5$': "$6$$6$$6$$6$",
//   '$6$': "$7$$7$$7$",
//   '$7$': "$8$$8$",
//   '$8$': "",
// };
// tokenTransform("z$0$z$0$z$0$z$0$z$0$z$0$z", tokens);
// -> 'zzzzzzz'

// ========================= 2 Pointers & Recursion =========================
// n: length of the longest string, m: num tokens
// Time: O(n^m), Space: O(n^m)
const tokenTransform = (s, tokens) => {
  let replaced = '';

  let i = 0;
  let j = 1;
  while (i < s.length) {
    if (s[i] !== '$') {
      replaced += s[i];
      i++;
      j = i + 1;
    } else if (s[j] !== '$') {
      j++;
    } else {
      const token = s.slice(i, j + 1);
      const finalValue = tokenTransform(tokens[token], tokens);
      replaced += finalValue;
      i = j + 1;
      j = i + 1;
    }
  }

  return replaced;
};