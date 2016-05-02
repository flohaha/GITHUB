
var express = require('express');
var app = express();
var url = require('url');

app.get('/activity/help',function(req,res){   ///^\/activity\/(.*)/

  	res.send( 'Tell me what you like I tell you where you go' ) ;

});

app.get('/activity',function(req,res){   ///^\/activity\/(.*)/

	//var count_a = len(req.query['a1']) ;

	var a1 = req.query['a1'] ;
	// if type(a1) == Undefined {
	// 	a1 = ""
	// };


  	var a2 = req.query['a2'] ;
  	var a3 = req.query['a3'] ;  



  	res.send("You like: " + a1 + ',' + a2 + ',' + a3  ) ;

  	var mysql      = require('mysql');
	var connection = mysql.createConnection({
	  host     : 'localhost',
	  user     : 'me',
	  password : 'secret',
	  database : 'my_db'
	});
	 
	connection.connect();
	 
	connection.query('SELECT 1 + 1 AS solution', function(err, rows, fields) {
	  if (err) throw err;
	 
	  console.log('The solution is: ', rows[0].solution);
	});
	 
	connection.end();

	

});


app.listen(3000);
console.log("Server runninng on port 3000");
