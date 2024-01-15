import PropTypes from "prop-types";
import { Link } from "react-router-dom";

function Movie({ id, title, medium_cover_image, rating, summary, genres }) {
  return (
    <div>
      <h2>
        {/* <Link to={`/movie/${id}`}>
          {title}
        </Link> */}
        <Link to={`/movierecommend/movie/${id}`}>
          {title}
        </Link>
      </h2>
      <img src={medium_cover_image} />
      <br></br>
      <strong>Stars : {rating}</strong>
      <p>{summary}</p>
      <ul>
        {genres.map((g) => (
          <li key={g}>{g}</li>
        ))}
      </ul>
    </div>
  );
}

Movie.propTypes = {
  id: PropTypes.number.isRequired,
  title: PropTypes.string.isRequired,
  medium_cover_image: PropTypes.string.isRequired,
  rating: PropTypes.number.isRequired,
  summary: PropTypes.string.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Movie;
