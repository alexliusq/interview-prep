/** @jsx jsx */
import React from 'react';
import { jsx, css } from '@emotion/react';
import { RouteComponentProps } from "@reach/router";


interface PersonListItemProps {
  firstName: string,
  lastName: string
};

const PersonListItem: React.FC<PersonListItemProps>
  = ({firstName, lastName}) => {

  return (
    <ul>
      {lastName}, {firstName}
    </ul>
  )
}

const CRUD: React.FC<RouteComponentProps> =  () => {
  return (
    <div
      css={{

      }}
    >
      <p>yolo</p>
    </div>
  )
}

export default CRUD;