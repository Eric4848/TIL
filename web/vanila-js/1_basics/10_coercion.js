/**
 * 타입 변환
 * Type Conversion
 *
 * 1) 명시적
 * 2) 암묵적
 */

let age = 32;

// 명시적
let stringAge = age.toString();
console.log(typeof stringAge, stringAge);
console.log(typeof parseInt("0"), parseInt("0"));
console.log(typeof parseFloat("0.99"), parseFloat("0.99"));
console.log("----------------------------");

// 암묵적
let test = age + "";
console.log(typeof test, test);

console.log("98" + 2);
console.log(98 + "2");
console.log("98" * 2);
console.log("98" - 2);
console.log("----------------------------");

//Boolean 타입으로 변환
console.log(!"x");
console.log(!!"x");
console.log("--------------");

console.log(!"");
console.log(!!"");
console.log("--------------");

console.log(!0);
console.log(!!0);
console.log("--------------");

console.log(!"0");
console.log(!0);
console.log("--------------");

console.log(!undefined);
console.log(!!undefined);
console.log("--------------");

console.log(!null);
console.log(!!null);
console.log("--------------");

console.log(!{});
console.log(!!{});
console.log("--------------");

console.log(![]);
console.log(!![]);
console.log("----------------------------");
