var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;

const URL_IABOT = "http://127.0.0.1:5000/resposta/";
const CONFIANCA_MINIMA = 0.65;

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getResposta = (mensagem) => {
  let dados = "";

  http.get(URL_IABOT + mensagem, (resposta) => {
    resposta.on("data", (pedaco) => {
      dados += pedaco;
    });

    resposta.on("end", () => {
      dados = JSON.parse(dados);
      if (dados.confianca >= CONFIANCA_MINIMA) {
        io.emit('chat message', "🤖 " + dados.resposta);
      } else {
        io.emit('chat message', "🤖 Ainda não sei responder esta pergunta. Você pode encontrar mais informações sobre o IFBA no site https://portal.ifba.edu.br/conquista");
      }
      console.log(dados);
    });
  })
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "👤 " + msg);
    getResposta(msg);
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
