function verify() {
    let content = document.getElementById("content").value;
    let a = parseInt(document.getElementById("a").value);
    let b = parseInt(document.getElementById("b").value);
    let c = parseInt(document.getElementById("c").value);
    console.log("\n\n a, b, c: ", a, b, c)

    let low, high
    if (a < b) {
        low = a;
        high = b;
    } else {
        low = b;
        high = a;
    }

    if (c >= low && c <= high) {
        result = " С принадлежит заданному диапазону"
        document.getElementById("result").value = messageText + result;
        check = true;
    } else {
        result = " С не принадлежит заданному диапазону"
        document.getElementById("result").value = messageText + result;
        check = false;
    }
    console.log("\n\nresult: ", result)
}

function send() {
    if (check) {
        document.getElementById('result').value = result;
        document.getElementById("result").innerText
        document.getElementById("UserEnter").submit();
    } else {
        alert("Есть недостатки. Повторите ввод")
    }
}

function verify_send() {
    verify();
    send();
}



let messageText = document.getElementById("result").innerText
let result;
let check = false;



const elementA = document.getElementById("a");
elementA.addEventListener('keyup', verify);
const elementB = document.getElementById("b");
elementB.addEventListener('keyup', verify);
const elementC = document.getElementById("c");
elementC.addEventListener('keyup', verify);

const verifyAll = document.getElementById("verify");
verifyAll.addEventListener('click', verify)

const elementSend = document.getElementById("send");
elementSend.addEventListener('click', send)
