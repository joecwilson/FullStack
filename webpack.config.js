const path = require('path');

module.exports = {
    entry: './education-game/src/index.js',  // path to our input file
    output: {
        filename: 'index-bundle.js',  // output bundle file name
        path: path.resolve(__dirname, './static'),  // path to our Django static directory
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: {presets: ["@babel/preset-env", "@babel/preset-react"]}
            },
            {
                test: /\.css$/i,
                include: path.resolve(__dirname, 'education-game/src'),
                use: ['style-loader', 'css-loader', 'postcss-loader'],
            },
            {
                test: /\.(png|jp(e*)g|svg|gif)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: 'images/[hash]-[name].[ext]',
                        },
                    },
                ],
            },
        ]
    },
};
