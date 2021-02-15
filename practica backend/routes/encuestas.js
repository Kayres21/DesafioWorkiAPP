const express = require('express');
const router = express.Router();
const db = require('../dbconfig');

router.use(express.urlencoded({ extended: true }));
router.use(express.json());



const encuentasRango = `SELECT count(TABLA_FINAL.RANGO_FILTRADO) FROM (SELECT *,
  CASE WHEN TO_TIMESTAMP( $1, 'YYYY/MM/DD HH24:MI:SS') > TO_TIMESTAMP(RANGO.FECHAS, 'YYYY/MM/DD HH24:MI:SS') AND TO_TIMESTAMP(RANGO.FECHAS, 'YYYY/MM/DD HH24:MI:SS') > TO_TIMESTAMP($2, 'YYYY/MM/DD HH24:MI:SS') THEN TRUE
  ELSE FALSE
  END AS RANGO_FILTRADO 
  FROM 
  (SELECT audit -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'last_login' AS FECHAS,
     CASE WHEN audit -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'last_login' = '' THEN FALSE
     WHEN audit -> '5c7dd876-39e4-425b-86bd-6a43adcf95d5' ->>'last_login' IS NULL THEN FALSE
     ELSE TRUE
     END
  AS FILTRO FROM users 
  ) AS RANGO WHERE RANGO.FILTRO = TRUE ) AS TABLA_FINAL WHERE  TABLA_FINAL.RANGO_FILTRADO = TRUE
   `

  const encuentasNombre = ` SELECT count(name) FROM users WHERE lower(name) LIKE  $1`

router.post('/rango', function(req, res) { 
  db.db.any(encuentasRango, [req.body.tiempoSuperior, req.body.tiempoInferior])
  .then(function (data) {
      console.log("DATA:", data);
      res.send(data)
  })
  .catch(function (error) {
      console.log("ERROR:", error);
  });
});

router.get('/nombre/:nombre', function(req, res) { 
  const filtro = req.params.nombre + '%'
  db.db.any(encuentasNombre, filtro)
  .then(function (data) {
      console.log("DATA:", data);
      res.send(data)
  })
  .catch(function (error) {
      console.log("ERROR:", error);
  });
});

router.get('/', function(req, res) { 
  db.db.any("SELECT * FROM users", filtro)
  .then(function (data) {
      console.log("DATA:", data);
      res.send(data)
  })
  .catch(function (error) {
      console.log("ERROR:", error);
  });
});




module.exports = router;
