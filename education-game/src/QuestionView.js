import React from 'react';
import {useState} from 'react';
import correctLogo from './images/Correct.svg'
import incorrectLogo from './images/Incorrect.svg'
import './index.css'

function QuestionView(props) {
    const [userAnswer, setUserAnswer] = useState(0);
    const handleSubmit = (event) => {
        event.preventDefault();

        const correctAnswerNum = parseFloat(props.question.answer);
        if ((userAnswer >= correctAnswerNum * 0.99) && (userAnswer <= correctAnswerNum * 1.01)) {
            props.onCorrectChange(2, props.question.id);
        } else {
            props.onCorrectChange(1, props.question.id);
        }
    }

    return (<div className="">
        <div>
            <div>
                Question
            </div>
            <div>
                <p>
                    {props.question.text}
                </p>
            </div>
        </div>
        <form className="" onSubmit={handleSubmit}>
            <label className="test">
                Answer
            </label>
            <input
                className="test"
                id="answer"
                type="number"
                placeholder="0"
                value={userAnswer}
                onChange={(e) => setUserAnswer(parseFloat(e.target.value))}
                disabled={props.question.visible === 2}/>
            <button type="submit"> Submit</button>
        </form>
        {(props.question.visible === 2) ? <img
            src={correctLogo}
            className="answerIcon"
            alt="You got the answer correct"/> : (props.question.visible === 1) ? <img
            src={incorrectLogo}
            className="answerIcon"
            alt="You got the answer incorrect"/> : <p className="text-white">Not Completed Yet</p>}
    </div>);
};
export default QuestionView

