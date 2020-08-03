var data =
var banner_vue = new Vue({
  delimiters: ['[[', ']]'],
  el: '#banner',
  data: {
  },
});
var topline_vue = new Vue({
  delimiters: ['[[', ']]'],
  el: '#topline',
  data: {
    topline_json:topline_json,
    time_series_us_json: time_series_us_json,
  },
});
var data_list_vue = new Vue({
  delimiters: ['[[', ']]'],
  el: '#data-list',
  data: {
    us_satistics_json: us_satistics_json,
    world_statistics_json: world_statistics_json,
  },
});
var infomation_hub_vue = new Vue({
  delimiters: ['[[', ']]'],
  el: '#information-hub',
  data: {
  },
});
var footer_vue = new Vue({
  delimiters: ['[[', ']]'],
  el: '#footer',
  data: {
  },
});
