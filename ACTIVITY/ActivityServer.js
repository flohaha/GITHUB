
var express = require('express');
var app = express();
var url = require('url');
var fs = require('fs');

app.get('/activity/help',function(req,res){   ///^\/activity\/(.*)/

  	res.send( 'Tell me what you like I tell you where you go' ) ;

});

app.get('/activity',function(req,res){   ///^\/activity\/(.*)/

	//var count_a = len(req.query['a1']) ;

	var a1 = req.query['a1'] ;
  	var a2 = req.query['a2'] ;
  	var a3 = req.query['a3'] ; 
  	var max = req.query['max'] ; 

  	var mysql      = require('mysql');
	var connection = mysql.createConnection({
	  host     : 'mysqldbonaws.ckro9mlzh1au.us-west-2.rds.amazonaws.com',
	  user     : 'fhatt',
	  password : '17flo0481',
	  database : 'myfirstawsdb'
	});
	 
	connection.connect();

	console.log('Connected to RDS');

	fs.readFile('sql_test.txt', 'utf8', function (err,data) {
  		if (err) {
    	return console.log(err);
  		}

  	var query = data.replace(/(\r\n|\n|\r)/gm," ")
  	query = 'call destination_recommender.Activity("%'+a1+'%","%'+a2+'%","%'+a3+'%",'+max+')'

  	console.log(query);

  	connection.query(query, function(err, rows, fields) {
		if (err) throw err;
		
		console.log('Data received from Db:\n');

		//console.log(rows[0]);

		var json_string = ''
		for (var i = 0; i < rows[0].length; i++) {
		  json_string = json_string + '{ "Rank":"' + i + '" , "Destination":"' + rows[0][i].Desti_input + '" },';

		};

		json_string = json_string.slice(0, -1);

		//json_string = '{ "firstName":"John" , "lastName":"Doe" },{ "firstName":"Anna" , "lastName":"Smith" }'

		console.log(json_string);

		json_string = '{ "reco" : [' +
				json_string +
			']}';

		console.log(json_string);
 
		var json = JSON.parse(json_string);
		console.log(json.reco);
		
		res.json(json);


		});
	 
	connection.end();	

	});

});


app.listen(3000);
console.log("Server runninng on port 3000");
