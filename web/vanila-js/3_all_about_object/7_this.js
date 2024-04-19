/**
 * This
 *
 * JS는 Lexical Scope를 사용하므로 상위 스코프가 정의 시점에 결정.
 * 하지만 this 키워드는 바인딩이 객체가 생성되는 시점에 결정
 */

const testFunction = function () {
  return this;
};

console.log(testFunction());
console.log(testFunction() === global);
console.log("----------------------------");

const wy = {
  name: "장원영",
  year: 2004,
  sayHello: function () {
    return `${this.name}입니다.`;
  },
};

console.log(wy.sayHello());

function Person(name, year) {
  this.name = name;
  this.year = year;

  this.sayHello = function () {
    return `${this.name}입니다.`;
  };
}

const wy2 = new Person("장원영", 2004);
console.log(wy2.sayHello());

Person.prototype.dance = function () {
  return `${this.name}이 춤춥니다.`;
};
console.log(wy2.dance());
console.log("--------------");

Person.prototype.dance = function () {
  function dance2() {
    return `${this.name}이 춤춥니다.`;
  }

  return dance2();
};
console.log(wy2.dance());
console.log("----------------------------");

/**
 * this가 가르키는 것의 조건
 *
 * 1) 일반 함수 호출할 땐 this가 최상위 객체를 가리킨다.
 * 2) 메소드로 호출할 땐 호출된 객체를 가리킨다.
 * 3) new 키워드를 사용해서 객체를 생성했을 땐 객체를 가리킨다.
 */

/**
 * 1) apply() -> arguments를 리스트로 입력해야한다.
 * 2) call() -> ,기준으로 arguments를 순서대로 넘겨준다.
 * 3) bind() -> call 문법으로 바인드 시킨 함수를 반환해준다.
 */

function returnName() {
  return this.name;
}

console.log(returnName());

const wy3 = {
  name: "장원영",
};
console.log(returnName.call(wy3));
console.log(returnName.apply(wy3));
console.log("----------------------------");

function multiply(x, y, z) {
  return `${this.name} / 계산값 : ${x * y * z}`;
}

console.log(multiply.call(wy3, 3, 4, 5));
console.log(multiply.apply(wy3, [3, 4, 5]));
console.log("----------------------------");

const laterFunc = multiply.bind(wy3, 3, 4, 5);
console.log(laterFunc);
console.log(laterFunc());
