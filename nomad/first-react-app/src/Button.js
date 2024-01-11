import PropTypes from "prop-types";
import styles from "./Button.module.css";

function Button({ text }) {
  return (
    // <button
    //   style={{
    //     color: "white",
    //     backgroundColor: "tomato",
    //   }}
    // >
    
    <button className={styles.btn}>
      {text}
    </button>
  );
}

Button.propTypes = {
  text: PropTypes.string.isRequired,
};
export default Button;
