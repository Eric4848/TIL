/**
 * Getter and Setter
 */

class IdolModel {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  /**
   * Getter
   *
   * 1) 데이터를 가공해서 새로운 데이터를 반환할 때
   * 2) private한 값을 반환할 때
   */
  get nameAndYear() {
    return `${this.name}-${this.year}`;
  }

  /**
   * Setter
   */
  set setName(name) {
    this.name = name;
  }
}

const wy = new IdolModel("장원영", 2004);
console.log(wy);
console.log(wy.nameAndYear);
console.log("--------------");
wy.setName = "원영";
console.log(wy);
console.log("----------------------------");

class IdolModel2 {
  #name;
  year;

  constructor(name, year) {
    this.#name = name;
    this.year = year;
  }

  get name() {
    return this.#name;
  }

  set name(name) {
    this.#name = name;
  }
}

const wy2 = new IdolModel2("장원영", 2004);
console.log(wy2);
console.log(wy2.name);
console.log("--------------");

wy2.name = "원영";
console.log(wy2.name);
