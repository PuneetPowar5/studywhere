const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function (App) {
  App.use(
    "/api/getRoom",
    createProxyMiddleware({
      target: "http://localhost:5000/",
      changeOrigin: true,
    })
  );
};
