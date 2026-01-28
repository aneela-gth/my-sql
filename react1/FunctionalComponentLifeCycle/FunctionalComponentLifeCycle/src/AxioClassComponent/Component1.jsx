import React from "react";
import axios from "axios";

export class Component1 extends React.Component {
  constructor() {
    super();
    this.state = {
      users: []
    };
  }

  componentDidMount() {
    console.log("componentDidMount - API call");

    axios.get("https://jsonplaceholder.typicode.com/todos")
      .then((res) => {
        this.setState({
          users: res.data
        });
      })
      .catch((err) => console.error(err));
  }

  render() {
    return (
      <div>
        <ul>
          {this.state.users.map((user) => (
            <li key={user.id}>{user.title}</li>
          ))}
        </ul>
      </div>
    );
  }
}
