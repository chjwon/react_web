import React, {useState} from "react";
import "./App.css"
import axios from "axios";

function App() {
  const [test, setTest] = useState(0)
  const [testNumber, setTestNumber] = useState("")
  const [testResult, setTestResult] = useState("")

  const BACKEND_URL = "http://127.0.0.1:8000"

  const reset = () => {
    setTest(0)
    setTestNumber("")
    setTestResult("")
  }
 
  const makeTestRequest = () => {
    if (test === 1) {
      // Uncomment when backend ready await axios.post('https://httpbin.org/post', { answer: 42 }
      try {
        const array_data = JSON.parse(testNumber)
        axios.post(BACKEND_URL + "/heartdisease/data", {data : array_data}).then((r) => {
          console.log(r)
          setTestResult(r.data.result)})
      }
      catch {
        setTestResult("Invalid data result")
      }
    }
    else if (test === 2) {
      try {
        const array_data = JSON.parse(testNumber)
        axios.post(BACKEND_URL + "/diabete/data", {data : array_data}).then((r) => {
          console.log(r)
          setTestResult(r.data.result)})
      }
      catch {
        setTestResult("Invalid data result")
      }
    }
    else {
      console.error("unknown test type")
    }
  }

  return (
    <>
      <div>
        <h1 style={{textAlign : "center"}}> Title </h1>
        {!test &&
        <div style={{display : "flex"}}>
          <div className="box" onClick={() => {setTest(1)}}>
              <h2 style={{marginTop : "25%"}}>Test Heart Disease</h2>
          </div>
          <div className="box" onClick={() => {setTest(2)}}>
              <h2 style={{marginTop : "25%"}}>Test Diabetes</h2>
          </div>
        </div>
        }
        {test !== 0 &&
          <div style={{textAlign : "center"}}>
            <button onClick={() => reset()}>Cancel</button>
            {test === 1 ? 
               <h2>Test Heart Disease</h2> : <h2>Test Diabetes</h2>
            } 
            <h3> Input number here...</h3>
            <input onChange={(e) => {setTestNumber(e.target.value)}} value={testNumber}></input>
            <button onClick={() => makeTestRequest()}>Test!</button>
            {testResult !== "" && 
              <div style={{marginTop : "5%"}}>
                <h2>Result: {testResult}</h2>
              </div>
            }
          </div>
        } 
      </div>
    </>
  );
}

export default App;
