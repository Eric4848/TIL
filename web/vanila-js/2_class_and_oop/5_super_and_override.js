/**
 * Super and Override
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  sayHello() {
    return `안녕하세요 ${this.name}입니다.`;
  }
}

class FemaleIdolModel extends IdolModel {
  part;

  constructor(name, year, part) {
    super(name, year); // ->Super(parent) class의 constructor 사용
    this.part = part;
  }

  sayHello() {
    return `안녕하세요 ${this.part}을 맡은 ${this.name}입니다.`;
  }
}

const wy = new FemaleIdolModel("장원영", 2004, "춤");
console.log(wy);
console.log(wy.sayHello());
console.log("--------------");
const wy2 = new IdolModel("장원영", 2004);
console.log(wy2.sayHello());
