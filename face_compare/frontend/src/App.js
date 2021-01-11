import logo from './logo.svg';
import React from "react"
import { Component } from "react"
import './App.css';
import { Button } from "reactstrap";
import axios from "axios"

class App extends React.Component{
  constructor(props){
    super()
    this.state = {
      id: "",
      source_file: "",
      target_file: "",
      loggedin: false,
    }
  }
  handleClick = () => {
    // axios.get("/myapi/allobjects/").then(res => this.setState({loggedin: true}
    console.log("hi")
    axios.get("myapi/allobjects").then(res => this.setState({loggedin: true}))
  };

  handleSubmit = item => {
    // if (item.id) {
    //   axios.put(`/myapi/allobjects/${item.id}/`, item)
    //   return;
    // }
    // axios.post("/myapi/allobjects/", item)
    axios.get("myapi/allobjects").then(res => this.setState({loggedin: true}))
  };

  render(){
    return(
      <main className="content">
        <h1 className="text-black text-uppercase text-center my-4 mt-5">Video Detection Security System</h1>
        <div className="col-md-6 col-sm-10 mx-auto p-0">
          <Button onClick={this.handleClick} className="btn btn-primary" size="lg" color="primary" block>Log In</Button>
        </div>
      </main>
    )
  }
}

export default App;
