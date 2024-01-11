import Button from "./Button";
import styles from "./App.module.css";
import { useState, useEffect } from "react";

// function App() {
//   return (
//     <div>
//       <h1 className={styles.title}>Welcome back!!!!!</h1>
//       <Button text={"continue"} />
//     </div>
//   )
// }
// export default App;

function App() {
  console.log("rendered");
  const [counter, setCounter] = useState(0);
  const [keyword, setKeyword] = useState("");
  const onClick = () => setCounter((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);
  // const runOnlyOnce = () => {
  //   console.log("Run only once")
  // }
  // useEffect(runOnlyOnce, [])

  useEffect(() => {
    console.log("Call The API...");
  }, []);
  useEffect(() => {
    console.log("Search", keyword)
  }, [keyword])
  return (
    <div>
      <input
        value={keyword}
        onChange={onChange}
        type='text'
        placeholder='Search here'
      />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me!</button>
    </div>
  );
}
export default App;
