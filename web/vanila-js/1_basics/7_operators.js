/**
 * 산술 연산자
 *
 * 1) 덧셈
 * 2) 뺄셈
 * 3) 곱셈
 * 4) 나눗셈
 * 5) 나머지
 */

console.log(10 + 10);
console.log(10 - 10);
console.log(10 * 10);
console.log(10 / 10);
console.log(10 % 10);
console.log(10 % 3);
console.log("----------------------------");

/**
 * 증가와 감소
 */

let number = 1;
console.log(number);
number++;
console.log(number);
number--;
console.log(number);
console.log("----------------------------");

/**
 * 연산자의 위치
 * 증가, 감소 연산자의 위치에 따라 다른 연산자의 순서 결정
 * 뒤에 있는 경우 나중
 * 앞에 있는 경우 먼저 -> 사실상 사용하지 않음
 */

let result = 1;
console.log(result);

result = number++;
console.log(result, number);

result = ++number;
console.log(result, number);
console.log("----------------------------");

/**
 * 숫자 타입이 아닌 경우
 */
let sample = "99";
console.log(+sample);
console.log(typeof +sample);

console.log(sample);
console.log(typeof sample);

sample = true;
console.log(+sample);
console.log(typeof +sample);

sample = false;
console.log(+sample);
console.log(typeof +sample);

sample = "장원영";
console.log(+sample); // NaN => Not a Number
console.log("----------------------------");

/**
 * 할당 연산자 (assignment operator)
 */
number = 100;
console.log(number);

number += 10;
console.log(number);

number -= 10;
console.log(number);

number *= 10;
console.log(number);

number /= 10;
console.log(number);

number %= 10;
console.log(number);
console.log("----------------------------");

/**
 * 비교 연산자
 *
 * 1) 값의 비교
 * 2) 값과 타입의 비교
 * 3) 대소 비교
 */
// 값 비교
console.log(5 == 5);
console.log(5 == "5");
console.log(0 == "");
console.log(true == 1);
console.log(false == "0");
console.log("--------------");

console.log(5 != 5);
console.log(5 != "5");
console.log(0 != "");
console.log(true != 1);
console.log(false != "0");
console.log("--------------");

// 값과 타입 비교
console.log(5 === 5);
console.log(5 === "5");
console.log(0 === "");
console.log(true === 1);
console.log(false === "0");
console.log("--------------");

console.log(5 !== 5);
console.log(5 !== "5");
console.log(0 !== "");
console.log(true !== 1);
console.log(false !== "0");
console.log("--------------");

// 대소 비교
console.log(1 < 100);
console.log(1 > 100);
console.log(1 <= 100);
console.log(1 >= 1);
console.log("----------------------------");

/**
 * 삼항 조건 연산자 -> 조건 ? 참인경우 : 거짓인 경우
 */
console.log(0 < 10 ? "우측이 크다" : "좌측이 크다");
console.log("----------------------------");

/**
 * 논리 연산자
 *
 * 1) && (and)
 * 2) || (or)
 */

console.log(true && true);
console.log(true && false);
console.log(false && true);
console.log(false && false);
console.log("--------------");

console.log(true || true);
console.log(true || false);
console.log(false || true);
console.log(false || false);
console.log("----------------------------");

/**
 * 단축평가 (short circuit evaluation)
 *
 * &&를 사용했을 때 좌측이 true면 우측 값 반환
 * &&를 사용했을 때 좌측이 false면 좌측 값 반환
 * ||를 사용했을 때 좌측이 true면 좌측 값 반환
 * ||를 사용했을 때 좌측이 false면 우측 값 반환
 */

console.log(true && "아이브");
console.log(false && "아이브");
console.log(true || "아이브");
console.log(false || "아이브");
// 중첩
console.log(true && true && "아이브");
console.log(true && false && "아이브");
console.log("----------------------------");

/**
 * 지수 연산자
 *
 * **
 */
console.log(3 ** 3);
console.log("----------------------------");

/**
 * null 연산자
 *
 * ?? => 좌측이 null이나 undefined인 경우 우측 저장
 */
let name;
console.log(name);

name = name ?? "Eric";
console.log(name);

name = name ?? "아이브";
console.log(name);
