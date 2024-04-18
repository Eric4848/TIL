/**
 * Scope
 */

var numberOne = 20;

function levelOne() {
  console.log(numberOne);
}

// levelOne();
console.log("----------------------------");

function levelOne() {
  var numberOne = 40;
  console.log(numberOne);
}

// levelOne();
console.log("----------------------------");

console.log(numberOne);

function levelOne() {
  var numberOne = 40;

  function levelTwo() {
    var numberTwo = 60;

    console.log(`levelTwo numberTwo : ${numberTwo}`);
    console.log(`levelTwo numberOne : ${numberOne}`);
  }

  levelTwo();
  console.log(`levelOne numberOne : ${numberOne}`);
}
levelOne();
// console.log(numberTwo)   // 불가능
console.log("----------------------------");

/**
 * Lexical Scope -> JS
 * 선언된 위치가 상위 스코프를 정한다
 *
 * Dynamic Scope
 * 실행한 위치가 상위 스코프를 정한다
 */

var numberThree = 3;

function functionOne() {
  var numberThree = 100;

  functionTwo();
}

function functionTwo() {
  console.log(numberThree);
}

functionOne();
console.log("----------------------------");

var i = 999;
for (var i = 0; i < 10; i++) {
  console.log(i);
}
console.log(`i in global scope : ${i}`);
console.log("----------------------------");

i = 999;
// block level scope
for (let i = 0; i < 10; i++) {
  console.log(i);
}
console.log(`i in global scope : ${i}`);

/**
 * var은 함수 레벨 스코프만 만들어낸다.
 *
 * let, const는 함수 레벨 스코프와 블록 레벨 스코프를 만들어낸다.
 */
