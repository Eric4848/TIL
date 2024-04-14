/**
 * try ... catch
 *
 * 1) 발생시킬때 -> throw
 * 2) 명시적으로 인지할 때 -> catch
 */

function runner() {
  try {
    console.log("Hello");

    throw new Error("Critical Error!");

    console.log("succes!");
  } catch (e) {
    console.log("---catch---");
    console.log(e);
  } finally {
    console.log("---finally---");
  }
}

runner();
