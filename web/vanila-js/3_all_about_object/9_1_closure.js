/**
 * Closure
 *
 * A closure is a combination of a function and the lexcial
 * environment within which that function was declared.
 *
 * 클로저는 어떤 함수와 해당 함수가 선언된 렉시컬 환경의 조합
 *
 * 상위 함수보다 하위 함수가 더 오래 살아있는 경우
 */

function getNumber() {
  var number = 5;

  function innerGetNumber() {
    return number;
  }

  return innerGetNumber();
}

// console.log(number);
console.log(getNumber());
console.log("----------------------------");

function getNumber() {
  var number = 5;

  function innerGetNumber() {
    return number;
  }

  return innerGetNumber;
}

const runner = getNumber();

console.log(runner);
console.log(runner());

/**
 * 1) 데이터 캐싱
 */

function cacheFunction(newNumb) {
  // 아래 계산이 매우 오래걸린다는 가정할 때
  var number = 10 * 10;

  // return number * newNumb

  function innerCacheFunction(newNumb) {
    return number * newNumb;
  }

  return innerCacheFunction;
}

const runner2 = cacheFunction();
console.log(runner2(10));
console.log(runner2(20));
console.log("--------------");

function cacheFunction2() {
  var number = 99;

  function increment() {
    number++;
    return number;
  }

  return increment;
}

const runner3 = cacheFunction2();
console.log(runner3());
console.log(runner3());
console.log(runner3());
console.log(runner3());
console.log(runner3());
console.log(runner3());
console.log("----------------------------");

/**
 * 정보 은닉
 */

function Idol(name, year) {
  this.name = name;

  var _year = year;

  this.sayNameAndYear = function () {
    return `${_year}에 태어난 ${this.name}입니다.`;
  };
}

const wy = new Idol("장원영", 2004);
console.log(wy._year);
console.log(wy.sayNameAndYear());
