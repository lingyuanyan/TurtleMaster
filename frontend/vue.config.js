// frontend/vue.config.js
module.exports = {
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://127.0.0.1:5000/',
        ws: true,
        changeOrigin: true
      }
    }
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: './dist/',
  // assetsDir must match Django's STATIC_URL
  assetsDir: 'static',
  css: {
    loaderOptions: {
      sass: {
        additionalData: `@import "~@/assets/styles/main.scss";`
      }
    }
  }
}