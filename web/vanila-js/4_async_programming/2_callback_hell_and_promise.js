/**
 * Callback
 */

function waitAndRun() {
  setTimeout(() => {
    console.log("End");
  }, 2000);
}

waitAndRun();

function waitAndRun2() {
  setTimeout(() => {
    console.log("1st callback end");
    setTimeout(() => {
      console.log("2nd callback end");
      setTimeout(() => {
        console.log("3rd callback end");
      }, 2000);
    }, 2000);
  }, 2000);
}

waitAndRun2();

/**
 * Promise
 */

const timeoutPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Done");
  }, 2000);
});

timeoutPromise.then((res) => {
  console.log(res);
});

const getPromise = (seconds) =>
  // resolve -> 성공 시 반환 => then / reject -> 실패 시 반환 => catch
  new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Done");
    }, seconds * 1000);
  });

getPromise(1)
  .then((res) => {
    console.log(res);

    return getPromise(1);
  })
  .then((res) => {
    console.log(res);
  });

// 동시에 진행, 가장 오래걸리는 것 기준으로 반환
Promise.all([getPromise(1), getPromise(2), getPromise(1)]).then((res) => {
  console.log(res);
});
