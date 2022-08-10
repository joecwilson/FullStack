import React, { Component } from 'react';
import Header from './Header.js'
import QuestionGroupView from "./QuestionGroupView";

export default function App(){
    return(
        <div>
            <Header></Header>
            <QuestionGroupView></QuestionGroupView>
        </div>
    )
}