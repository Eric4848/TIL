/**
 * Async / Await
 */

const getPromise = (seconds) =>
  new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Done");
    }, seconds * 1000);
  });
// reject는 try...catch를 활용하여 사용 가능
async function runner() {
  const result1 = await getPromise(1); // Promise로 만든 함수로만 await 가능
  console.log(result1);
}

runner();
console.log("End");
