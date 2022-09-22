module.exports = {
    rootDir: './education-game',
    testMatch: [
        '<rootDir>/education-game/src/__tests__/*.test.js',
        '<rootDir>/education-game/src/__tests__/*.test.jsx',
    ],
    roots: [
        '<rootDir>/education-game/src/__tests__/*.test.js'
    ],
    preset: 'ts-jest',
    testEnvironment: 'node',
    transform: {
        '^.+\\.ts?$': 'ts-jest',
        "^.+\\.(js|jsx)$": "babel-jest",
    },
    transformIgnorePatterns: ['./node_modules/'],

}