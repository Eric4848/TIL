/**
 * copy by value -> 값에 의한 전달
 * copy by reference -> 참조에 의한 전달
 *
 * 1) 기본적으로 모든 primitive값은 copy by value
 * 2) 객체는 copy by reference
 */

let original = "안녕하세요";
let clone = original;

console.log(original);
console.log(clone);
console.log("--------------");

clone += " 장원영 입니다";
console.log(original);
console.log(clone);
console.log("----------------------------");

let originalObj = {
  name: "장원영",
  group: "아이브",
};
let cloneObj = originalObj;

console.log(originalObj);
console.log(cloneObj);
console.log("--------------");

originalObj["group"] = "뉴진스";
console.log(originalObj);
console.log(cloneObj);
console.log("----------------------------");

console.log(original === clone);
console.log(originalObj === cloneObj);
console.log("----------------------------");
/**
 * Spread Operator
 */

const wy = {
  name: "장원영",
  group: "아이브",
};
const wy2 = {
  ...wy,
};

console.log(wy === wy2);
