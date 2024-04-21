/**
 * Async theory
 */

function longWork() {
  const now = new Date();

  /**
   * milliseconds since epoch
   * 1970년 1월 1일부터 현재 순간까지의 시간을 ms로 반환
   */

  const milliseconds = now.getTime();
  const afterTwoSeconds = milliseconds + 2 * 1000;

  while (new Date().getTime() < afterTwoSeconds) {}

  console.log("Done");
}

console.log("Hello");
longWork();
console.log("World");
console.log("----------------------------");

function longWork2() {
  setTimeout(() => {
    console.log("Done");
  }, 2000);
}

console.log("Hello");
longWork2();
console.log("World");
