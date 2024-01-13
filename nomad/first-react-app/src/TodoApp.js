import { useState } from "react";

function TodoApp() {
  const [toDo, setTodo] = useState("");
  const [toDos, setTodos] = useState([]);
  const onChange = (event) => setTodo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault(); // form에서 button을 누를 시 새로고침이 이루어지는데 이를 막는 함수
    if (toDo === "") {
      return;
    }
    setTodos((currentArray) => [toDo, ...currentArray]);
    setTodo("");
  };
  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input
          onChange={onChange}
          value={toDo}
          type='text'
          placeholder='Write your todo'
        />
        <button>Add To Do</button>
      </form>
      <hr />
      {toDos.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </div>
  );
}

export default TodoApp;
