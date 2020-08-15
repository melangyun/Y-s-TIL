const http = require("http");
const port = 3000;

const requestHandler = (request, response) => {
    console.log(request.url);
    response.end("hello Node.js Server!");
}

const server = http.createServer(requestHandler);

server.listen(port, (err) => {
    if (err) {
        return console.log("something bad happened\n", err);
    }

    console.log(`server is listening on ${port}`);
})