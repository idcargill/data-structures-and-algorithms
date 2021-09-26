
// const snorlaxData = {
//   stats: [
//     {
//       stat: {
//         url: 'https://pokeapi.co/api/v2/stat/6/',
//         name: 'speed',
//       },
//       effort: 5,
//       baseStat: 30,
//     },
//     {
//       stat: {
//         url: 'https://pokeapi.co/api/v2/stat/5/',
//         name: 'special-defense',
//       },
//       effort: 2,
//       baseStat: 110,
//     },
//     {
//       stat: {
//         url: 'https://pokeapi.co/api/v2/stat/4/',
//         name: 'special-attack',
//       },
//       effort: 9,
//       baseStat: 65,
//     },
//   ],
//   name: 'snorlax',
//   weight: 4600,
// };



// const getBaseStatGreaterThan = (arr, minBaseStat) => {
//   return arr.stats.filter((stats) => stats.baseStat > minBaseStat);
// };

// console.log(getBaseStatGreaterThan(snorlaxData, 50));


// ===== 8 


const characters = [
  {
    name: 'Eddard',
    spouse: 'Catelyn',
    children: ['Robb', 'Sansa', 'Arya', 'Bran', 'Rickon'],
    house: 'Stark',
  },
  {
    name: 'Jon',
    spouse: 'Lysa',
    children: ['Robin'],
    house: 'Arryn',
  },
  {
    name: 'Cersei',
    spouse: 'Robert',
    children: ['Joffrey', 'Myrcella', 'Tommen'],
    house: 'Lannister',
  },
  {
    name: 'Daenarys',
    spouse: 'Khal Drogo',
    children: ['Drogon', 'Rhaegal', 'Viserion'],
    house: 'Targaryen',
  },
  {
    name: 'Mace',
    spouse: 'Alerie',
    children: ['Margaery', 'Loras'],
    house: 'Tyrell',
  },
  {
    name: 'Sansa',
    spouse: 'Tyrion',
    house: 'Stark',
  },
  {
    name: 'Jon',
    spouse: null,
    house: 'Snow',
  },
];

function noChildren(person) {
  if (person.children) {
    return true;
  } else {
    return person
  }

}
    

// console.log(noChildren(characters));

console.log(characters.filter(noChildren));
