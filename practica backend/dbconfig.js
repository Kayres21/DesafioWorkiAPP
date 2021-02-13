const pgp = require("pg-promise")();
const datos =  require('../practica backend/constant')

pgp.pg.defaults.ssl = require;
pgp.pg.defaults.ssl.rejectUnauthorized = false;
const db = pgp("postgres://"+ datos.USER + ":" + datos.PASSWORD + "@" + datos.SERVER + ":" + datos.PORT_DB + "/" +datos.DATABASE)

module.exports = {
    db: db
}