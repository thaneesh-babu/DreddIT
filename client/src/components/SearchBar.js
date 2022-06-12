import {
  Center,
  Stack,
  Input,
  InputGroup,
  InputLeftAddon,
  Button,
} from "@chakra-ui/react";
import { useState } from "react";
import axios from "axios";

const SearchBar = () => {
  const [input, setInput] = useState("");
  const [postsLimit, setPostsLimit] = useState("")

  const handleInputChange = (e) => setInput(e.target.value)

  const handlePostsLimitChange = (e) => setPostsLimit(e.target.value)

  const postInput = () => {
    var param = {
      data: input,
      noOfPosts: postsLimit
    };
    axios
      .post("http://localhost:5000/input", param)
      .then((response) => console.log(response))
      .catch((err) => console.log(err));
  };

  return (
    <Center bg="red">
      <Stack spacing={4}>
        <InputGroup size="sm">
          <InputLeftAddon children=" r/ " color="white" />
          <Input placeholder="Search subreddit" onChange={handleInputChange} />
          <Input placeholder="No. of posts to analyze" onChange={handlePostsLimitChange}/>
          <Button h="1.75rem" size="sm" bg="lightgreen" onClick={postInput}>
            Search
          </Button>
        </InputGroup>
      </Stack>
    </Center>
  );
};

export default SearchBar;
