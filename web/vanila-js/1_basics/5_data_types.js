/**
 * Data Types
 *
 * 여섯개의 Primitive Type
 * 한개의 Object Type
 *
 * 1) Number (숫자)
 * 2) String (문자열)
 * 3) Boolean (참거짓)
 * 4) undefined (미정)
 * 5) null (비어있음)
 * 6) Symbol (심볼)
 *
 * 7) Object (객체)
 *      Function
 *      Array
 *      Object
 */

// 1. Number
const age = 27;
const tempature = -10;
const pi = 3.14;
const inf = Infinity;
const ninf = -Infinity;

console.log(typeof age);
console.log(typeof tempature);
console.log(typeof pi);
console.log(typeof inf);
console.log(typeof ninf);
console.log("----------------------------");

// 2. String
const myName = "Eric";
console.log(typeof myName);

/**
 * Escaping Character
 * 1) newline -> \n
 * 2) tab -> \t
 * 3) back slash -> \\
 *
 * Template Literal
 * ``사이에 원하는 문자열 그대로 사용
 * ${}사이에 변수 사용 가능
 */
const ive = "아이브\n장원영";
console.log(ive);
const newJeans = `뉴진스
하니`;
console.log(newJeans);
const group = "아이브";
console.log(`${group} 장원영`);
console.log("----------------------------");

// 3. Boolean
const isTure = true;
const isFalse = false;
console.log(typeof isTure);
console.log(typeof isFalse);
console.log("----------------------------");

// 4. undefined - 변수 초기화 하지 않은경우, 지양해야 한다
let undef;
console.log(undef);
console.log(typeof undef);
console.log("----------------------------");

// 5. null - 값이 없는 경우, 값이 없음을 개발자가 지정
let nul = null;
console.log(nul);
console.log(typeof nul);
console.log("----------------------------");

// 6. Symbole - 유일한 값 생성, 함수를 호출하여 사용
const test1 = "1";
const test2 = "2";
console.log(test1 === test2);
const test3 = "1";
console.log(test1 === test3);

const symbol1 = Symbol("1");
const symbol2 = Symbol("1");
console.log(symbol1 === symbol2);
console.log("----------------------------");

// 7. Object - Map, key:value pair
const dictionary = {
  red: "빨간색",
  orange: "주황색",
  yellow: "노란색",
};
console.log(dictionary);
console.log(dictionary["red"]);
console.log(dictionary["orange"]);
console.log(dictionary["yellow"]);
console.log(typeof dictionary);

// Array - 값을 리스트로 나열
const iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"];
console.log(iveMembers);
console.log(typeof iveMembers);
