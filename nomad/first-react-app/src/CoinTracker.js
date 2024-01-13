import { useEffect, useState } from "react";

function CoinTracker() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [money, setMoney] = useState(0);
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
  }, []);
  const onChange = (event) => setMoney(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (money === 0) {
      return;
    }
  };
  return (
    <div>
      <h1>The Coins {loading ? "" : `(${coins.length})`}</h1>
      {loading ? (
        <strong>Loading..</strong>
      ) : (
        <select>
          {coins.map((coin, index) => (
            <option>
              {coin.name} ({coin.symbol}): ${coin.quotes.USD.price} USD /{" "}
              {(coin.quotes.USD.price / coins[0].quotes.USD.price).toFixed(3)} btc
            </option>
          ))}
        </select>
      )}

      {/* <ul>
        {coins.map((coin, index) => (
          <li key={coin.rank}>
            {coin.name} ({coin.symbol}): ${coin.quotes.USD.price} USD
          </li>
        ))}
      </ul> */}
    </div>
  );
}

export default CoinTracker;
