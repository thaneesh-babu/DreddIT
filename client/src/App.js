import "./App.css";
import SearchBar from "./components/SearchBar";

function App() {
  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <h1>DreddIT</h1>
      </div>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "50vh",
        }}
      >
        <SearchBar />
      </div>
    </div>
  );
}

export default App;
