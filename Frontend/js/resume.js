// set api url
const api_url = "https://nl79fvnogb.execute-api.us-east-1.amazonaws.com/Prod/visitors"

update_counter();

function update_counter() {
    fetch(api_url)
    .then(response => {
        return response.json()
    })
    .then(data => {
        document.getElementById('counter').innerHTML=data
    })
}