import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
      username: "",
      email: ""
    };
    // Uncomment if using the OLD WAY
    // this.addUser = this.addUser.bind(this);
    // this.handleChange = this.handleChange.bind(this);
  };

  componentDidMount() {
  	this.getUsers();
  };

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <br/>
              <h1 className="title is-1">All Users</h1>
              <hr/><br/>
              <AddUser 
              	addUser={this._addUser} 
              	handleChange={this._handleChange} 
              	username={this.state.username}
              	email={this.state.email}/>
              <br/><br/>
              <UsersList users={this.state.users} />
            </div>
          </div>
        </div>
      </section>
    )
  }

  getUsers() {
  	axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
  	.then((res) => { this.setState({ users: res.data.data.users }); })
  	.catch((err) => { console.log(err); });
  }

  _addUser = (event) => {
    event.preventDefault();
    
    const data = {
      username: this.state.username,
      email: this.state.email
    };

    axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
    .then((res) => { 
      this.getUsers();
      this.setState({ username: "", email: "" }) 
    })
    .catch((err) => { console.log(err); });
  }

  _handleChange = (event) => {
    const data = {};
    data[event.target.name] = event.target.value;
    this.setState(data);
  }

  // THE OLD WAY
  // addUser(event) {
  //   console.log(this);
  // 	event.preventDefault();
  	
  // 	const data = {
  // 		username: this.state.username,
  // 		email: this.state.email
  // 	};

  // 	axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
  // 	.then((res) => { 
  // 		this.getUsers();
  // 		this.setState({ username: "", email: "" }) 
  // 	})
  // 	.catch((err) => { console.log(err); });
  // };

  // handleChange(event) {
  // 	const data = {};
  // 	data[event.target.name] = event.target.value;
  // 	this.setState(data);
  // }
};

ReactDOM.render(
	<App />,
	document.getElementById('root')
);
