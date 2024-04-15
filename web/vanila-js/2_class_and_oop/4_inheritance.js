/**
 * Inheritance
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

class FemaleIdolModel extends IdolModel {
  dance() {
    return `${this.name}이 춤을 춥니다.`;
  }
}

class MaleIdolModel extends IdolModel {
  sing() {
    return `${this.name}이 노래를 부릅니다.`;
  }
}

const wy = new FemaleIdolModel("장원영", 2004);
console.log(wy);
console.log(wy.name);
console.log(wy.dance());
console.log("--------------");

const jm = new MaleIdolModel("지민", 1995);
console.log(jm);
console.log(jm.year);
console.log(jm.sing());
console.log("----------------------------");

console.log(wy instanceof IdolModel);
console.log(wy instanceof FemaleIdolModel);
console.log(wy instanceof MaleIdolModel);
console.log("--------------");

console.log(jm instanceof IdolModel);
console.log(jm instanceof FemaleIdolModel);
console.log(jm instanceof MaleIdolModel);
