import { Input, InputGroup, InputLeftAddon, Button } from '@chakra-ui/react'

const SearchBar = () => {
	return (
		<InputGroup size='sm'>
	    <InputLeftAddon children='r/' />
	    <Input placeholder='Search subreddit' />
		<Button h='1.75rem' size='sm'>
          Search
        </Button>	  	
        </InputGroup>
	)
}

export default SearchBar