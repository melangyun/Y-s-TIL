let startTime = process.uptime();
const Worker = require("worker_threads");
let jobSize = 100000;

doSomething(); // event loop 가 처리해야 할 CPU 하드한 작업

let entTime = process.uptime();
console.log(Worker.threadId + " thread time : " + (entTime - startTime));
// 스레드 생성 시간 + doSomething
// 처리하는데 걸리는 시간.

function doSomething() {
    let data;
    for (let i = 0; i < jobSize; i += 1) {
        data += i;
    }
}
