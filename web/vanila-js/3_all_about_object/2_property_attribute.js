/**
 * Property Attribute
 *
 * 1) data property -> k-v로 형성된 실질적 값을 가지고 있다
 * 2) accessor property -> 값을 가지고 있지 않지만 다른 값에 영향을 주는 property => getter, setter
 */

const wy = {
  name: "장원영",
  year: 2003,
};

console.log(Object.getOwnPropertyDescriptor(wy, "name"));
console.log(Object.getOwnPropertyDescriptor(wy, "year"));
console.log("--------------");

/**
 * 1) value -> property값
 * 2) writable -> 수정 가능 여부, false시 수정 불가
 * 3) enumerable -> 열거 가능한지 여부, for...in 등 가능하면 true
 * 4) configurable -> property attribute 재정의 가능 여부, false시 삭제, 변경 금지
 */

const wy2 = {
  name: "장원영",
  year: 2004,

  get age() {
    return new Date().getFullYear() - this.year;
  },

  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};
console.log(wy2);
console.log(wy2.age);
console.log("--------------");

wy2.age = 26;
console.log(wy2);
console.log(wy2.age);
console.log(wy2.year);

console.log(Object.getOwnPropertyDescriptor(wy2, "age"));
console.log("----------------------------");

// writable
Object.defineProperty(wy2, "height", { value: 172, writable: true, enumerable: true, configurable: true }); // 미추가 시 default = false
console.log(Object.getOwnPropertyDescriptor(wy2, "height"));

wy2.height = 180;
console.log(wy2);
console.log("--------------");
Object.defineProperty(wy2, "height", {
  writable: false,
});
wy2.height = 172;
console.log(wy2);
console.log(Object.getOwnPropertyDescriptor(wy2, "height"));
console.log("----------------------------");

// enumerable
console.log(Object.keys(wy2));
for (let key in wy2) {
  console.log(key);
}
console.log("--------------");
Object.defineProperty(wy2, "name", { enumerable: false });
console.log(Object.getOwnPropertyDescriptor(wy2, "name"));
console.log(Object.keys(wy2));
console.log(wy2);
console.log(wy2.name);
console.log("----------------------------");

// configurable
Object.defineProperty(wy2, "height", { writable: true, configurable: false });
console.log(Object.getOwnPropertyDescriptor(wy2, "height"));
// Object.defineProperty(wy2, "height", { enumerable: false });   불가능
console.log("--------------");
Object.defineProperty(wy2, "height", { value: 172 });
console.log(Object.getOwnPropertyDescriptor(wy2, "height"));
Object.defineProperty(wy2, "height", { writable: false });
console.log(Object.getOwnPropertyDescriptor(wy2, "height"));
// Object.defineProperty(wy2, "height", { writable: true });   writable false -> true는 불가
