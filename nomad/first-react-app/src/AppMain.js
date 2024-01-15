import App from "./App";
import TodoApp from "./TodoApp";
import CoinTracker from "./CoinTracker";
import AppHome from "./AppHome";
import Home from "./routes/Home";
import Detail from "./routes/Detail";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function AppMain(){
  return (
    <Router>
      <Routes>
        <Route
        path="/"
        element={<AppHome />}>
        </Route>
        <Route
        path="/showhide/"
        element={<App />}>
        </Route>
        <Route
        path="/todo/"
        element={<TodoApp />}>
        </Route>
        <Route
        path="/cointracker/"
        element={<CoinTracker />}>
        </Route>
        <Route
        path="/movierecommend/"
        element={<Home />}>
        </Route>
        <Route
        path="/movierecommend/movie/:id"
        element={<Detail />}>
        </Route>
      </Routes>
    </Router>
  )
}

export default AppMain