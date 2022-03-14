import { Input, InputGroup, InputLeftAddon, Button } from "@chakra-ui/react";
import { useState } from "react";
import axios from 'axios'

// var script = document.createElement('script');
// script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
// script.type = 'text/javascript';
// document.getElementsByTagName('head')[0].appendChild(script);

const SearchBar = () => {
  const [input, setInput] = useState("");

  const handleInputChange = (e) => setInput(e.target.value);

  const postInput = () => {
    var param = {
      data: input
    }
    axios.post("http://localhost:5000/input", param)
    .then((response) => console.log(response) )
    .catch((err) => console.log(err))
  };

  return (
    <InputGroup size="sm">
      <InputLeftAddon children="r/" />
      <Input placeholder="Search subreddit" onChange={handleInputChange} />
      <Button h="1.75rem" size="sm" onClick={postInput}>
        Search
      </Button>
    </InputGroup>
  );
};

export default SearchBar;
