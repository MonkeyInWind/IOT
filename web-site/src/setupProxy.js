const {
    createProxyMiddleware
} = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(createProxyMiddleware('/api/weather', {
        "target": "http://t.weather.itboy.net",
        "changeOrigin": true
    }))
}