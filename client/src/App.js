import "./App.css";
import { Heading } from "@chakra-ui/react";
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
        <Heading>DreddIT</Heading>
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
