let pk = document.getElementById("pk").innerText
console.log("pk:", pk)
document.getElementById("pk").hidden = 1


a_collection = document.querySelectorAll('a')
for (let index = 0; index < a_collection.length; index++) {
    console.log(a_collection[index].id)
    if (a_collection[index].id === pk)
        a_collection[index].className = 'nav-link active'
}
