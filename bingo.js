const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host: '127.0.0.1',
    port: 3306,
    user: 'root',
    password: 'isaac',
    database: 'daya',
});

pool.getConnection()
    .then((message) => {
        console.log('connected successfully');})
    .catch((error) => {
        console.log('ERROR!!!:' + error.message);
    });

    module.exports = pool;