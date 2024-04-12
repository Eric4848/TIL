/**
 * Hoisting
 */
console.log("Hello");
console.log("World");
console.log("----------------------------");

/**
 * Hoisting이란?
 *
 * 모든 변수 선언문이 코드의 최상단으로 이동되는 것 처럼 실행되는 현상
 *
 * var -> undefined로 표시
 * let, const -> 발생하지만 initialize하라 알려줌
 */

console.log(name);
var name = "Eric";
console.log(name);

console.log(myName);
let myName = "Eric";
