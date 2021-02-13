const dotenv = require('dotenv');
dotenv.config();


exports.USER = process.env.USER
exports.PASSWORD = process.env.PASSWORD
exports.SERVER = process.env.SERVER
exports.PORT_DB = process.env.PORT_DB
exports.DATABASE = process.env.DATABASE