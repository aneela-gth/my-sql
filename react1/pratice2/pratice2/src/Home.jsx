function Home({ onOk }) {
  return (
    <div className="card">
      <h1>Welcome</h1>
      <p>Click OK to apply</p>
      <button className="btn" onClick={onOk}>OK</button>
    </div>
  );
}

export default Home;

