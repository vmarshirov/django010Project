let inner_text = document.getElementById("pk").innerText
console.log("inner_text:", inner_text)
document.getElementById("pk").hidden = 1

a_collection = document.getElementsByClassName("nav-link")
for (let index = 0; index < a_collection.length; index++) {
    console.log(a_collection[index].id)
    if (a_collection[index].id === inner_text)
        a_collection[index].className = 'nav-link active'
}

