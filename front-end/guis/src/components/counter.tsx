import React, {useState} from 'react';

import { RouteComponentProps } from '@reach/router'

const Counter: React.FC<RouteComponentProps> = () => {

  const [counter, setCounter] = useState(0)

  return(
    <div>
      <h1>Click Button</h1>
      <p>You've clicked the button {counter} times!</p>
      <button onClick={() => {
        setCounter(counter + 1)
      }}>
        Click me
      </button>
    </div>
  )
}

export default Counter