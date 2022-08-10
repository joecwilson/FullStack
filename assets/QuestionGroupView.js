import React from 'react';
import QuestionPreview from "./QuestionPreview";

export default function QuestionGroupView(){
     const questionGroups= [
        {
            id: 0,
            first_question: "What is 2+2",
            group_title: "Basic Questions",
        },
        {
            id:1,
            first_question: "What year is it",
            group_title: "Trivia",
        },
        {
            id:2,
            first_question: "When does Eu4 start",
            group_title: "Paradox",
        },
        {
            id:3,
            first_question: "How many turns is Civ",
            group_title: "4x Stragety",
        },
        {
            id:4,
            first_question: "What day of the month is UT Moov-in",
            group_title: "UT Austin",
        },
         {
            id:5,
            first_question: "How much debt were they in in the PDXCON grand campaign",
            group_title: "PDXCON",
        },
    ]
     const listItems = questionGroups.map(group =>
        <div key={group.id}>
            <h2>
                {group.group_title}
            </h2>
            <p>
                {group.first_question}
            </p>
            <button>
                Do this group
            </button>
        </div>
      );

    return(
        <div className="grid-container">
            {listItems}
        </div>
    )
}