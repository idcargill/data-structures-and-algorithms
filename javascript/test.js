const arr = [2, 4, 6];

const newArr = [];
for (let num in arr) {
  newArr.push(Math.pow(2, num));
}

console.log(newArr);
