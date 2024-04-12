/**
 * function -> 함수
 *
 * 함수에서 입력받는 값에 대한 정의를 Parameter라고 한다
 * 실제 입력하는 값은 argument라고 한다
 */

/**
 * DRY
 * D -> Don't
 * R -> Repeat
 * Y -> Yourself
 */

function calculate() {
  console.log((((2 * 10) / 2) % 3).toString());
}

calculate();
console.log("--------------");

function calculate2(number) {
  console.log((((number * 10) / 2) % 3).toString());
}

calculate2(4);
calculate2(5);
console.log("--------------");

function multiply(x, y) {
  console.log(x * y);
}

multiply(3, 4);

function multiply(x, y = 10) {
  console.log(x * y);
}

multiply(3, 4);
multiply(3);
console.log("----------------------------");

// 반환 받기
function multiply2(x, y) {
  return x * y;
}

const result1 = multiply2(3, 4);
console.log(result1);
console.log("----------------------------");

// Arrow 함수
const multiply3 = (x, y) => {
  return x * y;
};
console.log(multiply3(4, 5));

const multiply4 = (x, y) => x * y;
console.log(multiply4(4, 5));

const chain = (x) => (y) => (z) => `x: ${x} y: ${y} x:${z}`;
console.log(chain(1)(2)(3));

function chain2(x) {
  return function (y) {
    return function (z) {
      return `x: ${x} y: ${y} z: ${z}`;
    };
  };
}
console.log(chain2(4)(5)(6));
console.log("----------------------------");

const multiplyThree = function (x, y, z) {
  console.log(arguments);
  return x * y * z;
};
console.log(multiplyThree(4, 5, 6));

const multiplyAll = function (...arguments) {
  return Object.values(arguments).reduce((a, b) => a * b, 1);
};
console.log(multiplyAll(3, 4, 5, 6, 7, 8, 9));
console.log("----------------------------");

// immediatel invoked function
(function (x, y) {
  console.log(x * y);
})(2, 3);
