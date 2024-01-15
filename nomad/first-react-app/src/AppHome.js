import { Link } from "react-router-dom";

function AppHome() {
  return (
    <div>
      <h1>React App Pactice</h1>
      <Link to='/showhide'>
        <h3>Show Hide</h3>
      </Link>
      <Link to='/todo'>
        <h3>Todo</h3>
      </Link>
      <Link to='/cointracker'>
        <h3>Coin Tracker</h3>
      </Link>
      <Link to='/movierecommend'>
        <h3>Movie</h3>
      </Link>
    </div>
  );
}

export default AppHome;
