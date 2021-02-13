var express = require('express');
var router = express.Router();
const datos =  require('../constant')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
  console.log("postgres://"+ datos.USER + ":" + datos.PASSWORD + "@" + datos.SERVER + ":" + datos.PORT_DB + "/" +datos.DATABASE )

});

module.exports = router;
