const {
    createProxyMiddleware
} = require('http-proxy-middleware');

module.exports = function (app) {
    app.use(createProxyMiddleware('/api/weather', {
        'target': 'https://wis.qq.com/',
        'changeOrigin': true,
        'pathRewrite': {
            '/api/weather/common': '/weather/common'
        }
    }))
}