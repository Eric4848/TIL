/**
 * Using function to create objects
 */

function IdolModel(name, year) {
  //console.log(new.target)   // 함수로 선언한 지 사용한 지 확인
  // 생성자를 빼먹었을 때 추가하여 생성
  if (!new.target) {
    return new IdolModel(name, year);
  }
  this.name = name;
  this.year = year;

  this.dance = function () {
    return `${this.name}이 춤을 춥니다`;
  };
}

const wy = new IdolModel("장원영", 2004);
console.log(wy);
console.log(wy.dance());
console.log("--------------");

const wy2 = IdolModel("장원영", 2004);
console.log(wy2);
console.log("--------------");

console.log(global.name);

const IdolModelArrow = (name, year) => {
  this.name = name;
  this.year = year;
};
console.log("----------------------------");

const wy3 = new IdolModelArrow("장원영", 2004); // new 생성자는 Arrow function에선 사용 불가
