const triangle = (n) => {
  let str = "";
  for (let i = 1; i <= n; i++) {
    for (let j = n - 1; j >= i; j--) {
      str += " ";
    }
    for (let k = 1; k <= i; k++) {
      str += "*";
    }
    for (let l = 1; l <= i - 1; l++) {
      str += "*";
    }

    str += "\n";
  }
  return str;
};
console.log(triangle(10));
