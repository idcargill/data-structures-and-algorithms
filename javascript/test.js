const arr = [2, 4, 6];

const newArr = [];
for (let num in arr) {
  newArr.push(Math.pow(2, num));
}

// console.log(newArr);

const ar = ['c', 'b', 'U', 'a'];

// ar.forEach((n) => console.log(n.charCodeAt()));

const dirtyArr = [1, 2, 3, 'cat', 4, 5];

dirtyArr.forEach((i) => {
  if (typeof i !== 'number') {
    console.log(i);
  }
});
