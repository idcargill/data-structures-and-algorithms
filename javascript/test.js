const nums = [1, 5, 10, 20, 30];

const calculateAverage = (arr) => {
  return arr.reduce(
    (acc, num, idx) => {
      let item = { count: idx, sum: num };
      let totals = { ...acc, ...item };
      return totals;
    },
    { count: 0, sum: 0 }
  );
};

console.log(calculateAverage(nums));

// let y = nums.reduce((acc, val) => acc + val);

// console.log(y);
