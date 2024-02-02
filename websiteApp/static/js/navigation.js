let inner_text = document.getElementById("pk").innerText
console.log("inner_text:", inner_text)
document.getElementById("pk").hidden = 1

a_collection = document.getElementsByClassName("nav-link")
for (let index = 0; index < a_collection.length; index++) {
    console.log('')
    console.log(a_collection[index])
    if (a_collection[index].id === inner_text){
        a_collection[index].className = 'nav-link active'
        console.log(a_collection[index].id)
        }

    // let nav_item_list = a_collection[index].href.split('/')
    // let last_nav_item = nav_item_list[nav_item_list.length-2]
    // console.log(nav_item_list)
    //     if (last_nav_item === inner_text){
    //     a_collection[index].className = 'nav-link active'
    //     console.log(a_collection[index].id)
    //     }
}

