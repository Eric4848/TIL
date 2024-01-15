import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import TodoApp from './TodoApp';
import CoinTracker from './CoinTracker';
import MovieApp from './MovieApp';
import Main from './Main';
import AppMain from './AppMain';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <React.StrictMode>
    // <App />
    // <TodoApp />
    // <CoinTracker />
    // <MovieApp />
    // <Main />
    <AppMain />
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals