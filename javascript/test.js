// const nums = [1, 5, 10, 20, 30];

// const calculateAverage = (arr) => {
//   const initialValue = { count: 0, sum: 0 };
//   const totals = arr.reduce((acc, num) => {
//     acc.count = acc.count + 1;
//     acc.sum = acc.sum + num;
//     return acc;
//   }, initialValue);
//   return totals.sum / totals.count;
// };

// console.log(calculateAverage(nums));

// let y = nums.reduce((acc, val) => acc + val);

// console.log(y);

// const numbers = [1, 2, 13, 64, 45, 56, 17, 8];

// const isPrime = (value) => {
//   for (let i = 2; i < value; i++) {
//     if (value % i === 0) {
//       return false;
//     }
//   }
//   return value > 1;
// };

// const countPrimeNumbers = (arr) => {
//   return arr.reduce((acc, num) => {
//     if (isPrime(num)) {
//       acc = acc + 1;
//     }
//     return acc;
//   }, 0);
// };

// console.log(countPrimeNumbers(numbers));

// const snorlaxData = {
//   stats: [
//     {
//       stat: {
//         url: "https://pokeapi.co/api/v2/stat/6/",
//         name: "speed",
//       },
//       effort: 5,
//       baseStat: 30,
//     },
//     {
//       stat: {
//         url: "https://pokeapi.co/api/v2/stat/5/",
//         name: "special-defense",
//       },
//       effort: 2,
//       baseStat: 110,
//     },
//     {
//       stat: {
//         url: "https://pokeapi.co/api/v2/stat/4/",
//         name: "special-attack",
//       },
//       effort: 9,
//       baseStat: 65,
//     },
//   ],
//   name: "snorlax",
//   weight: 4600,
// };

// const extractStat = (statName, arr) => {
//   return arr.reduce((acc, item) => {
//     if (item.stat.name === statName) {
//       console.log(item);
//       acc = item;
//     }
//     return acc;
//   }, {});
// };

// console.log(extractStat("special-attack", snorlaxData.stats));

// 11

const characters = [
  {
    name: "Eddard",
    spouse: "Catelyn",
    children: ["Robb", "Sansa", "Arya", "Bran", "Rickon"],
    house: "Stark",
  },
  {
    name: "Jon",
    spouse: "Lysa",
    children: ["Robin"],
    house: "Arryn",
  },
  {
    name: "Cersei",
    spouse: "Robert",
    children: ["Joffrey", "Myrcella", "Tommen"],
    house: "Lannister",
  },
  {
    name: "Daenarys",
    spouse: "Khal Drogo",
    children: ["Drogon", "Rhaegal", "Viserion"],
    house: "Targaryen",
  },
  {
    name: "Mace",
    spouse: "Alerie",
    children: ["Margaery", "Loras"],
    house: "Tyrell",
  },
  {
    name: "Sansa",
    spouse: "Tyrion",
    house: "Stark",
  },
  {
    name: "Jon",
    spouse: null,
    house: "Snow",
  },
];

const checkChildren = (obj) => {
  let regex = /a/gi;
  if (!obj.children) {
    return false;
  }
  let results = obj.children.filter((child) => {
    // console.log(child);
    if (child.match(regex)) {
      console.log(child);
      return true;
    }
  });
  return results;
};

const extractChildren = (arr) => {
  let regex = /a/gi;
  let childArr = arr.filter((fam) => fam.children);
  return childArr.reduce((acc, fam) => {
    if (!fam.children) {
      return false;
    }
    fam.children.forEach((child) => {
      if (!child) {
        return false;
      }
      if (child.match(regex)) {
        acc.push(child);
        // console.log(acc);
      }
    });
    return acc;
  }, []);
};

// console.log(extractChildren(characters));

// 06
// 1
const people = [
  {
    name: "lloyd",
    age: 32,
    shoeSize: 12,
  },
  {
    name: "jamie",
    age: 21,
    shoeSize: 8,
  },
];

const getNames = (arr) => {
  return arr.map((person) => {
    let len = person.name.length - 1;
    let name = [...person.name];
    let word = "";
    name.forEach((l, idx) => {
      let letter = name[len - idx];
      word = word + letter;
    });
    return word;
  });
};

console.log(getNames(people));
