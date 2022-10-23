const n = [-1, 2, 5, 2, -2, 9, 10, 7];

const selectionSort = (n) => {
  let minIdx,
    temp,
    len = n.length;
  for (let i = 0; i < len; i++) {
    minIdx = i;
    for (let j = i + 1; j < len; j++) {
      if (n[j] < n[minIdx]) {
        minIdx = j;
      }
    }
    temp = n[i];
    n[i] = n[minIdx];
    n[minIdx] = temp;
  }
  return n;
};

console.log(selectionSort(n));
