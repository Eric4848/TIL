/**
 * Static Keyword
 */

class IdolModel {
  name;
  year;
  static groupName = "아이브";

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  static returnGroupName() {
    return "아이브";
  }
}

const wy = new IdolModel("장원영", 20004);
console.log(wy);
console.log("--------------");
console.log(IdolModel.groupName);
console.log(IdolModel.returnGroupName());
console.log("----------------------------");

// factory constructor

class IdolModel2 {
  name;
  year;

  constructor(name, year) {
    this.name = name;
    this.year = year;
  }

  static fromObject(object) {
    return new IdolModel2(object.name, object.year);
  }

  static fromList(list) {
    return new IdolModel2(list[0], list[1]);
  }
}

const wy2 = IdolModel2.fromObject({ name: "장원영", year: 2004 });
console.log(wy2);
console.log("--------------");

const wy3 = IdolModel2.fromList(["장원영", 2004]);
console.log(wy3);
