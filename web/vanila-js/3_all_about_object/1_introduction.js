/**
 * All about objects
 *
 * 객체를 선언할 때 사용할 수 있는 방법들
 * 1) object를 생성해 객체 생성 - 기본 {}
 * 2) class를 인스턴스화해서 생성 - class와 oop
 * 3) function을 사용해서 객체를 생성
 */

// object
const wy = {
  name: "장원영",
  year: "2004",
};

console.log(wy);
console.log("--------------");

// class
class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}
console.log(new IdolModel("장원영", 2004));
console.log("----------------------------");
function IdolFunction(name, year) {
  this.name = name;
  this.year = year;
}
const yj = new IdolFunction("안유진", 2003);
console.log(yj);
