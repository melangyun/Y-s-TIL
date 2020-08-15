const { Worker } = require("worker_threads");
let startTime = process.uptime();
let jobSize = 100000;
let myWorker1, myWorker2;

myWorker1 = new Worker(__dirname + "/worker.js");
// 스래드 생성, 파일 절대 경로를 통해 가리킨 js 파일 작업
myWorker2 = new Worker(__dirname + "/worker.js");

doSomething(); // event loop 가 처리해야 할 CPU 하드한 작업

let entTime = process.uptime();
console.log("main thread time : " + (entTime - startTime));
// 스레드 생성 시간 + doSomething
// 처리하는데 걸리는 시간.

function doSomething() {
    let data;
    for (let i = 0; i < jobSize; i += 1) {
        data += i;
    }
}
