var http = require('http');
var url = require('url');
var fileSystem = require('fs');

var userCount = 0

http.createServer(function (req, res) {
  
  console.log('New Connection');
  userCount++;

  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.write('Hello World\n');
  res.write('You are the user # ' + userCount + ' !!!! CONGRATS!!!!\n');

  // var read_stream = fileSystem.createReadStream('myfile.txt');
  // read_stream.on('data', writeCallback);
  // read_stream.on('close', closeCallback);

  // function writeCallback('data'){
  // 	res.write('data');
  // }

  // function closeCallback(){
  // 	res.end();
  // }

  res.end();


}).listen(8080, '127.0.0.1');
console.log('Server running at http://127.0.0.1:8080/');
