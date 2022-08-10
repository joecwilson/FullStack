import React from 'react';


export default function QuestionPreview(first_question,group_title){

    return(
        <div>
            <h2>
                {group_title}
            </h2>
            <p>
                {first_question}
            </p>
            <button>
                Do this group
            </button>
        </div>
    )
}