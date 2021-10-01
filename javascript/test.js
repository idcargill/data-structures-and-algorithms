let arr = ["Cat", "zebra", "fish", "apple"];

let newArr = arr.sort();

// console.log(newArr);

arr.sort();
// console.log(arr);

let numArr = [1, 4, 100, 12, 2, 13];

// numArr.forEach((i) => {
//   console.log(i.toString().length);
// });

// function Meeting(dayOfWeek, start, end) {
//   this.dayOfWeek = dayOfWeek;
//   this.start = start;
//   this.end = end;
// }
// const meetings = [
//   new Meeting("Monday", "0900", "1000"),
//   new Meeting("Wednesday", "1300", "1500"),
//   new Meeting("Tuesday", "1145", "1315"),
//   new Meeting("Wednesday", "0930", "1000"),
//   new Meeting("Monday", "0900", "0945"),
//   new Meeting("Friday", "1200", "1345"),
// ];

// console.log(week);

// 13==================================================
function Meeting(dayOfWeek, start, end) {
  this.dayOfWeek = dayOfWeek;
  this.start = start;
  this.end = end;
}
const meetings = [
  new Meeting("Monday", "0900", "1000"),
  new Meeting("Wednesday", "1300", "1500"),
  new Meeting("Tuesday", "1145", "1315"),
  new Meeting("Wednesday", "0930", "1000"),
  new Meeting("Monday", "0900", "0945"),
  new Meeting("Friday", "1200", "1345"),
];

const week = {
  Sunday: 0,
  Monday: 1,
  Tuesday: 2,
  Wednesday: 3,
  Thursday: 4,
  Friday: 5,
  Saturday: 6,
};

const sortSchedule = (arr) => {
  arr.sort((a, b) => {
    // Same Day Same Time
    if (week[a.dayOfWeek] === week[b.dayOfWeek] && +a.start === +b.start) {
      if (+a.end - +a.start < +b.end - +b.start) {
        return -1;
      }
      if (+a.end - +a.start > +b.end - +b.start) {
        return 1;
      } else {
        return 0;
      }
    }
    // Same Day
    if (week[a.dayOfWeek] === week[b.dayOfWeek]) {
      if (+a.end - +a.start < +b.end - +b.start) {
        return -1;
      }
      if (+a.end - +a.start > +b.end - +b.start) {
        return 1;
      } else {
        return 0;
      }
    }
    // Day Time
    if (week[a.dayOfWeek] < week[b.dayOfWeek]) {
      if (+a.start < +b.start) {
        return -1;
      }
      if (+a.start > +b.start) {
        return 1;
      } else {
        return 0;
      }
    }
    // Day B first
    // if (week[a.dayOfWeek] > week[b.dayOfWeek]) {
    //   if (+a.start < +b.start) {
    //     return -1;
    //   }
    //   if (+a.start > +b.start) {
    //     return 1;
    //   } else {
    //     return 0;
    //   }
    // }
  });
  return arr;
};

console.log(sortSchedule(meetings));
