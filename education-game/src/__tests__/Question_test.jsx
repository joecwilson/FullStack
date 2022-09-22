import {render, screen, cleanup} from "@testing-library/react";
// Importing the jest testing library
import '@testing-library/jest-dom'
import QuestionView from "../QuestionView";

afterEach(() => {
    cleanup();
})

describe("QuestionView", () => {

    test("Starts with no image", () => {
        const questionBase = {id: 1, question_text: "test 1", answer: 1, visible: 0}
        render(<QuestionView
            question={questionBase}
        />)
        expect(screen.getByRole("heading")).toHaveTextContent("Question")
    })
})