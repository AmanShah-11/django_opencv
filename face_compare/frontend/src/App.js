import logo from './logo.svg';
import React from "react"
import { Component } from "react"
import './App.css';
import {
  Button
  // Modal,
  // ModalHeader,
  // ModalBody,
  // ModalFooter,
  // Form,
  // FormGroup,
  // Input,
  // Label
} from "reactstrap";

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

  render(){
    return(
      <main className="content">
        <h1 className="text-black text-uppercase text-center my-4 mt-5">Video Detection Security System</h1>
        <div className="col-md-6 col-sm-10 mx-auto p-0">
          <Button className="btn btn-primary" size="lg" color="primary" block>Log In</Button>
        </div>
      </main>
    )
  }
}

export default App;
