module.exports = {
    rootDir: './education-game',
    testMatch: [
        '<rootDir>/src/__tests__/*.test.js',
        '<rootDir>/src/__tests__/*.test.jsx',
    ],
    roots: [
        '<rootDir>/src/__tests__/*.test.js'
    ],
    preset: 'ts-jest',
    testEnvironment: 'node',
    transform: {
        '^.+\\.ts?$': 'ts-jest',
        "^.+\\.(js|jsx)$": "babel-jest",
    },
    transformIgnorePatterns: ['./node_modules/'],

}