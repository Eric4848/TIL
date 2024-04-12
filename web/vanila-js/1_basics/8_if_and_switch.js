/**
 * If and Switch
 */
// If
let number = 5;

if (number % 2 === 0) {
  console.log("number is even");
} else {
  console.log("number is odd");
}

if (number % 2 === 0) {
  console.log("2의 배수");
} else if (number % 3 === 0) {
  console.log("3의 배수");
} else if (number % 4 === 0) {
  console.log("4의 배수");
} else if (number % 5 === 0) {
  console.log("5의 배수");
} else {
  console.log("2~5의 배수가 아님");
}
console.log("----------------------------");

// Switch
const englishDay = "monday";

let koreanDay;

switch (englishDay) {
  case "monday":
    koreanDay = "월요일";
    break;
  case "tuesday":
    koreanDay = "화요일";
    break;
  case "wednesday":
    koreanDay = "수요일";
    break;
  case "thursday":
    koreanDay = "목요일";
    break;
  case "friday":
    koreanDay = "금요일";
    break;
  default:
    koreanDay = "주말";
    break;
}

console.log(koreanDay);
