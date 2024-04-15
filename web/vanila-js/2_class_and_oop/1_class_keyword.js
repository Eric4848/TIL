/**
 * Class Keyword
 */

class IdolModel {
  // constructor에서 사용 시 정의하지 않아도 된다
  name;
  year;

  // constructor => 생성자
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  // method
  sayName() {
    return `${this.name}입니다.`;
  }
}

const wy = new IdolModel("장원영", 2004);
console.log(wy);
const yj = new IdolModel("안유진", 2003);
console.log(yj);
const ge = new IdolModel("가을", 2002);
console.log(ge);
const rei = new IdolModel("레이", 2004);
console.log(rei);
const liz = new IdolModel("리즈", 2004);
console.log(liz);
const ls = new IdolModel("이서", 2007);
console.log(ls);
console.log("--------------");

console.log(wy.name);
console.log(wy.year);
console.log("--------------");

console.log(wy.sayName());
console.log(yj.sayName());
console.log("--------------");

console.log(typeof IdolModel);
console.log(typeof wy);
