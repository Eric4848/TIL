/**
 * Immutable Object
 */

const wy = {
  name: "장원영",
  year: 2004,
  get age() {
    return new Date().getFullYear() - this.year;
  },
  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};

console.log(wy);
console.log("----------------------------");

/**
 * Extensible
 */
console.log(Object.isExtensible(wy));
wy["position"] = "dancer";
console.log(wy);
console.log("--------------");

Object.preventExtensions(wy);
console.log(Object.isExtensible(wy));
wy.groupName = "아이브";
console.log(wy);
console.log("--------------");

delete wy.position;
console.log(wy);
console.log("----------------------------");

/**
 * Seal
 * configurable -> false
 * 값을 추가, 삭제 불가능
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
console.log(Object.isSealed(wy2));
console.log("--------------");

Object.seal(wy2);
console.log(Object.isSealed(wy2));
console.log("--------------");

wy2["groupName"] = "아이브";
console.log(wy2);
console.log("--------------");

delete wy2.name;
console.log(wy2);
console.log("--------------");

Object.defineProperty(wy2, "name", {
  value: "Eric",
});
console.log(wy2);

Object.defineProperty(wy2, "name", {
  writable: false,
});

console.log(Object.getOwnPropertyDescriptor(wy2, "name"));
console.log("----------------------------");

/**
 * Freezed
 */
const wy3 = {
  name: "장원영",
  year: 2004,
  get age() {
    return new Date().getFullYear() - this.year;
  },
  set age(age) {
    this.year = new Date().getFullYear() - age;
  },
};

console.log(Object.isFrozen(wy3));
console.log("--------------");

Object.freeze(wy3);
console.log(Object.isFrozen(wy3));
console.log("--------------");

wy3.groupName = "아이브";
console.log(wy3);
console.log("--------------");

delete wy3.name;
console.log(wy3);
console.log("--------------");

// console.log(Object.defineProperty(wy3, "name", { value: "Eric" }));   불가능
console.log(Object.getOwnPropertyDescriptor(wy3, "name"));
console.log("--------------");

const wy4 = {
  name: "장원영",
  year: 2004,
  yj: {
    name: "안유진",
    year: 2003,
  },
};
Object.freeze(wy4);

console.log(Object.isFrozen(wy4));
console.log(Object.isFrozen(wy4.yj));
