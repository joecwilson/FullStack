import React, {Component} from 'react';
import Footer from './Footer.js';
import QuestionList from './QuestionList.js';
import './index.css'

class App extends Component {
    render() {
        return (
            <div className="">
                <QuestionList/>
                <Footer/>
            </div>

        )
    }
}

export default App;