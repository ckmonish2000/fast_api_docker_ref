

function App() {

  const click = () => {
    fetch('http://localhost:5001')
      .then(v => v.json())
      .then(v => { console.log(v) })
      .catch(err => console.log(err))
  }

  return (
    <div className="App">
      <button onClick={click}>tests</button>
    </div>
  );
}

export default App;
