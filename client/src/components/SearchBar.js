import { Input, InputGroup, InputLeftAddon, Button } from '@chakra-ui/react'
import { useState } from 'react'

const SearchBar = () => {
	const [input, setInput] = useState('Search subreddit')

	const handleInputChange = (e) => setInput(e.target.value)

	return (
		<InputGroup size='sm'>
	    <InputLeftAddon children='r/' />
	    <Input value={input} onChange={handleInputChange} />
		<Button h='1.75rem' size='sm'>
          Search
        </Button>	  	
        </InputGroup>
	)
}

export default SearchBar