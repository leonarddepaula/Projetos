function show_rows(objs){

    all_rows_str = []

    for(obj of objs){
        id = obj['id']
        userId = obj['userId']
        title = obj['title']

        obj_str =`
           <tr> 
             <td>${id} </td>
             <td>${userId} </td>
             <td>${title} </td>
           </tr>
        `
        all_rows_str.push(obj_str)
    }
    all_strs = all_rows_str.join(' ')
    table = document.getElementById("registros")
    table.innerHTML = all_strs
}

async function get_items(){
    response = await fetch('https://jsonplaceholder.typicode.com/posts')
    json_obj = await response.json()
    console.log(json_obj)
    show_rows(json_obj)
}
get_items()

