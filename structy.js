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
    if (n % i == 0) return false;
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
    if (s[j] != s[i]) {
      if (j - i == 1) {
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
    if (nums[i] == 5 && nums[j] != 5) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
      j--;
    } else if (nums[j] == 5) {
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
  if (head == null) return false;
  if (head.val == target) return true;

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

  while (currNode != null) {
    if (nodeIdx == index) return currNode.val;
    currNode = currNode.next;
    nodeIdx++;
  }

  return null;
};

// ========================= Recursive =========================
const getNodeValue = (head, index) => { // Time: O(n), Space: O(n)
  if (index == 0) return head.val;
  if (head == null) return null;

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

  while (currNode != null) {
    const nextNode = currNode.next;
    currNode.next = prevNode;
    prevNode = currNode;
    currNode = nextNode;
  }

  return prevNode;
};

// ========================= Recursive =========================
const reverseList = (head, prev = null) => { // Time: O(n), Space: O(n)
  if (head == null) return prev;
  
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

  while (current1 != null && current2 != null) {
    if (count % 2 == 0) {
      tail.next = current2;
      current2 = current2.next;
    } else {
      tail.next = current1;
      current1 = current1.next;
    }
    tail = tail.next;
    count++;
  }

  if (current1 == null) tail.next = current2;
  if (current2 == null) tail.next = current1;

  return head1;
};

// ========================= Recursive =========================
const zipperLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(min(n, m))
  if (head1 == null && head2 == null) return null;
  if (head1 == null) return head2;
  if (head2 == null) return head1;

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

  while (current1 != null && current2 != null) {
    if (current1.val < current2.val) {
      tail.next = current1;
      current1 = current1.next;
    } else {
      tail.next = current2;
      current2 = current2.next;
    }

    tail = tail.next;
  }

  if (current1 == null) tail.next = current2;
  if (current2 == null) tail.next = current1;

  return dummyHead.next;
};

// ========================= Recursive =========================
const mergeLists = (head1, head2) => { // Time: O(min(n, m)), Space: O(min(n, m))
  if (head1 == null && head2 == null) return null;
  if (head1 == null) return head2;
  if (head2 == null) return head1;

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

  while (currNode != null) {
    if (currNode.val != value) return false;
    currNode = currNode.next;
  }

  return true;
};

// ========================= Recursive =========================
const isUnivalueList = (head, prev = head) => { // Time: O(n), Space: O(n)
  if (head == null) return true;

  if (head.val == prev.val) {
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
  
  while (currNode != null) {
    if (currNode.val == prevNode.val) {
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

  while (currNode != null) {
    if (currNode.val == targetVal) {
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
  if (head == null) return null;
  if (head.val == targetVal) return head.next;

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
    if (count == index) {
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
  if (index == 0) {
    const newNode = new Node(value);
    newNode.next = head;
    return newNode;
  }

  if (count == index - 1) {
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
  if (i == values.length) return null;
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
const addLists = (head1, head2) => {
  const sumHead = new Node(null);
  let currNode = sumHead;
  let curr1 = head1;
  let curr2 = head2;
  let carry = 0;

  while (curr1 != null || curr2 != null || carry != 0) {
    let val1 = curr1 == null ? 0 : curr1.val;
    let val2 = curr2 == null ? 0 : curr2.val;
    let sum = val1 + val2 + carry;
    let num = sum % 10;
  
    carry = (sum > 9) ? 1 : 0;

    currNode.next = new Node(num);
    currNode = currNode.next;
    if (curr1 != null) curr1 = curr1.next;
    if (curr2 != null) curr2 = curr2.next;
  }

  return sumHead.next;
};