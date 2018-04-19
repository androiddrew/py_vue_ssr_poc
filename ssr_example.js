const vm = new Vue({
  template: `<div>{{ msg }}</div>`,
  data: {
    msg: 'Vue SSR in Python'
  }
});

function renderApp(app) {

  let html
  // exposed by `vue-server-renderer/basic.js`
  renderVueComponentToString(app, (err, res) => {
    html = res
  })
  return html
}

var result = renderApp(vm)
