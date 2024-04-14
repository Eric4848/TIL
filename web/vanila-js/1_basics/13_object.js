/**
 * Object / 객체
 */

// key : value pair
let wy = {
  name: "장원영",
  group: "아이브",
  dance: function () {
    // return "장원영이 춤을 춥니다";
    return `${this.name}이 춤을 춥니다`;
  },
};

console.log(wy);
console.log(wy.name);
console.log(wy["name"]);
const key = "name";
console.log(wy[key]);
console.log(wy.dance());
console.log("--------------");

const nameKey = "name";
const nameValue = "장원영";

const groupKey = "group";
const groupValue = "아이브";

const wy2 = {
  [nameKey]: nameValue,
  [groupKey]: groupValue,
  dance: function () {
    reutrn`${this.name}이 춤을 춥니다`;
  },
};
console.log("----------------------------");

/**
 * 객체의 특징
 *
 * 1) const로 선언하면 객체 자체를 변경할 수는 없다
 * 2) 객체 안의 property나 method는 변경할 수 있다
 */

// wy2 = {};

wy2[groupKey] = "newJeans";
console.log(wy2);

wy2["englishName"] = "Jang Won Young";
console.log(wy2);
console.log("----------------------------");

// 모든 key 다 가져오기
console.log(Object.keys(wy));
console.log("--------------");

// 모든 value 다 가져오기
console.log(Object.values(wy));
console.log("----------------------------");

// 편의기능
const name = "장원영";
const wy3 = { name };
console.log(wy3);
