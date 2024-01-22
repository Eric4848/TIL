import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./routes/Home";
import Detail from "./routes/Detail";

function Main() {
  return (
    <Router>
      <Routes>
        <Route
          path='/'
          element={<Home />}
        ></Route>
        <Route
          path='/movie/:id'
          element={<Detail />}
        />
      </Routes>
    </Router>
  );
}

export default Main;