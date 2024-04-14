/**
 * Array Functions
 */

let iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"];

console.log(iveMembers);

// push()
iveMembers.push("Eric");
console.log(iveMembers);
console.log("----------------------------");

// pop()
console.log(iveMembers.pop());
console.log(iveMembers);
console.log("----------------------------");

// shift() -> 좌측을 pop
console.log(iveMembers.shift());
console.log(iveMembers);
console.log("----------------------------");

// unshift() - 좌측에 push
console.log(iveMembers.unshift("장원영"));
console.log(iveMembers);
console.log("----------------------------");

//splice() -> 시작위치, 삭제할 갯수 / 원본 변경
console.log(iveMembers.splice(1, 3));
console.log(iveMembers);
console.log("----------------------------");

// concat() -> 새로운 array 생성 / 원본 유지
iveMembers = ["장원영", "안유진", "가을", "레이", "리즈", "이서"];
console.log(iveMembers.concat("Eric"));
console.log(iveMembers);
console.log("----------------------------");

//slice() -> 이상, 미만 삭제 (idx 기준) / 원본 유지
console.log(iveMembers.slice(0, 3));
console.log(iveMembers);
console.log("----------------------------");

// spread operator => ... -> 각 요소별로 실행 / 새로운 array 생성
let iveMembers2 = [...iveMembers];
console.log(iveMembers2);

let iveMembers3 = [iveMembers];
console.log(iveMembers3);

let iveMembers4 = iveMembers;
console.log(iveMembers4);

console.log(iveMembers4 === iveMembers);
console.log(iveMembers2 === iveMembers);
console.log("----------------------------");

// join()
console.log(iveMembers.join());
console.log(typeof iveMembers.join());
console.log("--------------");

console.log(iveMembers.join("/"));
console.log(iveMembers.join(", "));
console.log("----------------------------");

// sort() -> 오름차순 정렬
iveMembers.sort();
console.log(iveMembers);
console.log("--------------");

// reverse() -> 내림차순
console.log(iveMembers.reverse());
console.log("----------------------------");

// a, b를 비교하여
// a를 b보다 나중에 정렬하려면 0보다 큰 숫자를 반환
// a를 b보다 먼저 정렬하려면 0보다 작은 숫자를 반환
// 원래 순서를 그대로 두려면 0을 반환
let numbers = [1, 9, 7, 5, 3];
console.log(numbers);
numbers.sort((a, b) => {
  return a > b ? 1 : -1;
});
console.log(numbers);
console.log("--------------");

numbers.sort((a, b) => {
  return a > b ? -1 : 1;
});
console.log(numbers);
console.log("----------------------------");

// map() -> 원본 유지
console.log(iveMembers.map((x) => x));
console.log("--------------");

console.log(iveMembers.map((x) => `아이브:${x}`));
console.log("--------------");

console.log(
  iveMembers.map((x) => {
    if (x === "장원영") {
      return `아이브: ${x}`;
    } else {
      return x;
    }
  })
);
console.log("----------------------------");

// filter() -> 함수 조건에 해당하는 값들 전부 반환
numbers = [1, 8, 7, 6, 3];

console.log(numbers.filter((x) => true));
console.log(numbers.filter((x) => false));
console.log(numbers.filter((x) => x % 2 === 0));
console.log(numbers.filter((x) => x % 2 === 1));
console.log("----------------------------");

// find() -> 가장 먼저 합수 조건에 해당하는 값 반환
console.log(numbers.find((x) => x % 2 === 0));
console.log(numbers.find((x) => x % 2 === 1));
console.log("----------------------------");

// findIndex() -> find에 해당하는 값의 index 반환
console.log(numbers.findIndex((x) => x % 2 === 0));
console.log("----------------------------");

// reduce() -> reduce((이전까지의 값, 현재 값) => 계산식, 초기값)
console.log(numbers.reduce((p, n) => p + n, 0));

console.log(iveMembers.reduce((p, n) => p + n + "/", ""));
console.log("----------------------------");
