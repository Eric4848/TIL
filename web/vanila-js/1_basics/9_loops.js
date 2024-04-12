/**
 * Loops
 *
 * 1) for
 * 2) while
 */
// For
for (let i = 0; i < 10; i++) {
  console.log(i);
}
console.log("--------------");
for (let i = 10; i > 0; i--) {
  console.log(i);
}
console.log("--------------");
for (let i = 0; i < 3; i++) {
  for (let j = 3; j > 0; j--) {
    console.log(i, j);
  }
}
console.log("--------------");
let square = "";
let L = 6;

for (let i = 0; i < L; i++) {
  for (let j = 0; j < L; j++) {
    square += "*";
  }
  square += "\n";
}
console.log(square);
console.log("----------------------------");

// for ... in
const wy = {
  name: "장원영",
  year: 2004,
  group: "아이브",
};

for (let key in wy) {
  console.log(key);
  console.log(wy[key]);
}
console.log("--------------");
// array의 경우 idx반환
const iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"];

for (let key in iveMembers) {
  console.log(key);
  console.log(iveMembers[key]);
}
console.log("----------------------------");

// for ... of -> 값 반환

for (let value of iveMembers) {
  console.log(value);
}
// While
let number = 0;
while (number < 10) {
  console.log(number);
  number++;
}
console.log("--------------");
console.log(number);
console.log("----------------------------");

// do ... while -> 사실상 사용하지 않음
number = 0;
do {
  console.log(number);
  number++;
} while (number < 10);
console.log("--------------");
console.log(number);
console.log("----------------------------");

// break
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
console.log("----------------------------");

// continue
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}
