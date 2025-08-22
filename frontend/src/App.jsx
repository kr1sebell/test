import { useState } from 'react';

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: 20 }}>
      <h1>Моя ферма</h1>
      <p>Фруктов собрано: {count}</p>
      <button onClick={() => setCount(count + 1)}>Собрать фрукт</button>
    </div>
  );
}
