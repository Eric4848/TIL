/**
 * Protytype
 */

const testObj = {};

// __proto__ -> 모든 객체에 존재하는 프롶러티
// class 강의 중 상속에서 부모 클래스에 해당되는 값
console.log(testObj.__proto__);
console.log("----------------------------");

function IdolModel(name, year) {
  this.name = name;
  this.year = year;
}

console.log(IdolModel.prototype);

console.dir(IdolModel.prototype, {
  showHidden: true,
});
console.log("--------------");

// circular reference
console.log(IdolModel.prototype.constructor === IdolModel);
console.log(IdolModel.prototype.constructor.prototype === IdolModel.prototype);
console.log("----------------------------");

const wy = new IdolModel("장원영", 2004);

console.log(wy.__proto__);
console.log(wy.__proto__ === IdolModel.prototype);
console.log(testObj.__proto__ === Object.prototype);
console.log("--------------");

console.log(IdolModel.__proto__ === Function.__proto__);
console.log(Function.prototype.__proto__ === Object.prototype);
console.log(IdolModel.prototype.__proto__ === Object.prototype);
console.log("----------------------------");

console.log(wy.toString());
console.log(Object.prototype.toString());
console.log("----------------------------");

function IdolModel2(name, year) {
  this.name = name;
  this.year = year;

  this.sayHello = function () {
    return `${this.name}이 인사합니다.`;
  };
}

const wy2 = new IdolModel2("장원영", 2004);
const yj2 = new IdolModel2("안유진", 2003);

console.log(wy2.sayHello());
console.log(yj2.sayHello());
console.log(wy2.sayHello === yj2.sayHello);

console.log(wy2.hasOwnProperty("sayHello"));
console.log("--------------");

function IdolModel3(name, year) {
  this.name = name;
  this.yaer = year;
}

IdolModel3.prototype.sayHello = function () {
  return `${this.name}이 인사합니다.`;
};

const wy3 = new IdolModel3("장원영", 2004);
const yj3 = new IdolModel3("안유진", 2003);

console.log(wy3.sayHello());
console.log(yj3.sayHello());
console.log(wy3.sayHello === yj3.sayHello);

console.log(wy3.hasOwnProperty("sayHello"));
console.log("--------------");

IdolModel3.sayStaticHello = function () {
  return "Static Method";
};

console.log(IdolModel3.sayStaticHello());
console.log("----------------------------");

/**
 * Overriding
 */

function IdolModel4(name, year) {
  this.name = name;
  this.year = year;

  // override 시킨다
  this.sayHello = function () {
    return "Instance Method";
  };
}

IdolModel4.prototype.sayHello = function () {
  return "Prototype Method";
};

const wy4 = new IdolModel4("장원영", 2004);
console.log(wy4.sayHello());
console.log("----------------------------");

/**
 * getPrototypeOf, setPrototypeOf
 *
 * 인스턴스의 __proto__ 변경 vs 함수의 prototype 변경
 */

function IdolModel(name, year) {
  this.name = name;
  this.year = year;
}

IdolModel.prototype.sayHello = function () {
  return `${this.name}가 인사합니다.`;
};

function FemaleIdolModel(name, year) {
  this.name = name;
  this.year = year;

  this.dance = function () {
    return `${this.name}가 춤춥니다.`;
  };
}

const riz = new IdolModel("리즈", 2004);
const rei = new FemaleIdolModel("레이", 2004);

console.log(riz.__proto__);
console.log(riz.__proto__ === IdolModel.prototype);
console.log(Object.getPrototypeOf(riz) === IdolModel.prototype);
console.log("--------------");

console.log(riz.sayHello());
console.log(rei.dance());
//console.log(rei.sayHello());   // 불가능
console.log(Object.getPrototypeOf(rei) === FemaleIdolModel.prototype);
console.log("--------------");

Object.setPrototypeOf(rei, IdolModel.prototype);
console.log(rei.sayHello());
console.log(rei.constructor === FemaleIdolModel);
console.log(rei.constructor === IdolModel);
console.log("--------------");

console.log(Object.getPrototypeOf(rei) === FemaleIdolModel.prototype);
console.log(Object.getPrototypeOf(rei) === IdolModel.prototype);
console.log(FemaleIdolModel.prototype === IdolModel.prototype);
console.log("--------------");

FemaleIdolModel.prototype = IdolModel.prototype;

const es = new FemaleIdolModel("이서", 2007);
console.log(Object.getPrototypeOf(es) === FemaleIdolModel.prototype);
console.log(FemaleIdolModel.prototype === IdolModel.prototype);
