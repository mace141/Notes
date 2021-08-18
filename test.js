const bSearch = (arr, target) => {
  let len = arr.length;
  let midpoint = Math.floor(len / 2);
  let left = arr.slice(0, midpoint);
  let right = arr.slice(midpoint, len);

  if (len == 0) {
      return -1;
  }

  if (arr[midpoint] == target) {
      return midpoint;
  } else if (arr[midpoint] > target) {
      return bSearch(left, target);
  } else {
      return left.length + bSearch(right, target);
  }
};

console.log(bSearch([0, 6, 8, 12, 16, 19, 20, 24, 28], 27));