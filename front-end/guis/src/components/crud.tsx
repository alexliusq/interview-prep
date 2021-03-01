/** @jsxImportSource @emotion/react */
import React, {useState} from 'react';
// import { jsx, css } from '@emotion/react';
import { RouteComponentProps } from "@reach/router";



type Person = {
  firstName: string,
  lastName: string
}
interface PersonListItemProps {
  person: Person,
  highlighted?: boolean,
  onSelectPerson(person: Person | null): any
};

const PersonListItem: React.FC<PersonListItemProps>
  = ({person, highlighted, onSelectPerson}) => {

  const {firstName, lastName} = person;
  
  const onClick = () => {
    if (highlighted) {
      onSelectPerson(null)
    } else {
      onSelectPerson(person);
    }
  }

  return (
    <ul
      css={{
        paddingInlineStart: '0px',
        backgroundColor: highlighted ? 'lightblue' : 'white'
      }}
      onClick={onClick}
    >
      {lastName}, {firstName}
    </ul>
  )
}


let start_persons = ['Hans Emil', 'Max Mustermann', 'Roman Tisch']
  .map(person => {
    const [firstName, lastName] = person.split(' ');
    return {
      firstName,
      lastName
    };
  });

const CRUD: React.FC<RouteComponentProps> =  () => {

  const [allPersons, setAllPersons] = useState(start_persons)
  const [prefix, setPrefix] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [selectedPerson, setSelectedPerson] = useState<Person | null>(null);

  const onFilterChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    let value = e.target.value;
    setPrefix(value)
  }

  const onFirstNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFirstName(e.target.value)
  }

  const onLastNameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setLastName(e.target.value)
  }

  const onAddPerson = (e: React.MouseEvent) => {
    e.preventDefault();
    setAllPersons([...allPersons, {firstName, lastName}]);
    setFirstName('');
    setLastName('');
  }

  const onSelectPerson = (person: Person | null) => {
    setSelectedPerson(person);
  }

  let displayPersons = allPersons;

  if (prefix) {
    displayPersons = displayPersons.filter(person => {
      let lowercased = prefix.toLowerCase()
      return person.lastName.toLowerCase().startsWith(lowercased)
    });
  }

  return (
    <div
      css={{
        display: 'flex',
        width: '100%',
        justifyContent: 'center'
      }}
    >
      <div>
        <div
          css={{
            marginTop: '20px',
            display: 'flex',
            maxWidth:'500px',
            justifyContent: 'space-between'
          }}
        >
          <div
            css={{
              width: '300px'
            }}
          >
            <label>
              Filter prefix:
              <input
                css={{
                  marginLeft: '10px'
                }}
                value={prefix}
                onChange={onFilterChange}
              />
            </label>
            {
              displayPersons.map(person => {
                if (
                  selectedPerson &&
                  selectedPerson.firstName === person.firstName &&
                  selectedPerson.lastName === person.lastName
                  ) {
                    return (
                      <PersonListItem highlighted={true}
                      person={person} onSelectPerson={onSelectPerson}/>
                    )
                }

                return <PersonListItem person={person} onSelectPerson={onSelectPerson}/>
              })
            }
          </div>
          <div
            css={{
              width: '200px',
              paddingTop: '30px'
            }}
          >
            <label
              css={{
                display: 'block'
              }}
            >
              First:
              <input
                css={{
                  marginLeft: '10px'
                }}
                value={firstName}
                onChange={onFirstNameChange}
              />
            </label>
            <label
              css={{
                display: 'block',
                marginTop: '10px'
              }}
            >
              Last:
              <input
                css={{
                  marginLeft: '10px'
                }}
                value={lastName}
                onChange={onLastNameChange}
              />
            </label>
          </div>
      </div>
      <div
        css={{
          display: 'flex',
          justifyContent: 'flex-start',
          width: '100%',
          '& > *': {
            marginRight: '10px'
          }
        }}
      >
        <button
          onClick={onAddPerson}
        >create</button>
        <button>update</button>
        <button>delete</button>
      </div>
      </div>
    </div>
  )
}

export default CRUD;