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
  // todo
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
  // todo
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
// test_01:
// uncompress("4s2b"); // -> 'ssssbb'
// test_02:
// uncompress("2p1o5p"); // -> 'ppoppppp'
// test_03:
// uncompress("3n12e2z"); // -> 'nnneeeeeeeeeeeezz'

const uncompress = (s) => {
  // todo
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
//
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

// [[[[[[[[[[[[[[[[[[[[[[[[[ #7 pairsum ]]]]]]]]]]]]]]]]]]]]]]]]]
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

// [[[[[[[[[[[[[[[[[[[[[[[[[ #8 pair product ]]]]]]]]]]]]]]]]]]]]]]]]]
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
//
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
//
// Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the array.
//
// test_00
// fiveSort([12, 5, 1, 5, 12, 7]);
// // -> [12, 7, 1, 12, 5, 5] 
// test_01
// fiveSort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]);
// // -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5] 
// test_02
// fiveSort([5, 5, 5, 1, 1, 1, 4]);
// // -> [4, 1, 1, 1, 5, 5, 5] 
// test_03
// fiveSort([5, 5, 6, 5, 5, 5, 5]);
// // -> [6, 5, 5, 5, 5, 5, 5] 
// test_04
// fiveSort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]);
// // -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

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