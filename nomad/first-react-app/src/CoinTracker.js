import { useEffect, useState } from "react";

function CoinTracker() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  const [money, setMoney] = useState(0);
  const [can, setCan] = useState(0);
  const [selected, setSelected] = useState(0);
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json())
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
  }, []);

  const onSubmit = (event) => {
    event.preventDefault();
    if (money === 0) {
      return;
    }
    setCan((money / coins[selected].quotes.USD.price).toFixed(5));
  };

  return (
    <div>
      <h1>The Coins {loading ? "" : `(${coins.length})`}</h1>
      {loading ? (
        <strong>Loading..</strong>
      ) : (
        <select
          onChange={(e) => {
            setSelected(e.target.selectedIndex)
            if (can !== 0){
              setCan(0)
            }
          }}
        >
          {coins.map((coin, index) => (
            <option key={index}>
              {coin.name} ({coin.symbol}): ${coin.quotes.USD.price} USD / {" "}
              {(coin.quotes.USD.price / coins[0].quotes.USD.price).toFixed(3)} btc
            </option>
          ))}
        </select>
      )}
      <hr />
      <form onSubmit={onSubmit}>
        <input
          onChange={(event) => setMoney(event.target.value)}
          value={money}
          type='number'
          placeholder='How much do you have?'
        />
        <button>confirm</button>
      </form>
      {can === 0 ? null : <div>you can buy {can} {coins[selected].name}s</div>}
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
