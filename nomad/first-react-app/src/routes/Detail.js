import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Detail() {
  const { id } = useParams();
  const [now, setNow] = useState([]);
  const getDetail = async () => {
    const json = await (await fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)).json();
    console.log(json);
    setNow(json.data.movie);
  };
  useEffect(() => {
    getDetail();
    console.log(now);
  }, []);
  return (
    <div>
      <h1>Detail</h1>
      {now ? (
        <div>
          <h3>{now.title_long}</h3>
          <strong>{now.like_count} Likes</strong>
          <br />
          <img src={`${now.large_cover_image}`} />
          <p>{now.description_full}</p>
        </div>
      ) : null}
    </div>
  );
}

export default Detail;
