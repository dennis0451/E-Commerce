let searched;
// event listener for search button
const searchButton = document.getElementById('searchForm');
if(searchButton){
searchButton.addEventListener('submit',(event)=>{
    event.preventDefault()

    const searchInput = document.getElementById('product')
    console.log(searchInput.value)
     
    axios.get("products", { params: { query: searchInput.value } })
      .then((response) => {
        console.log('response?');
        console.log(response);
        last = document.getElementById("search_bar");
        newImage = document.createElement("img");
        newImage.src = response.data.url;
        last.appendChild(newImage);
      });
    console.log(searchInput.value)
})
}


function outOfStock(){
    alert('This item is out of stock. Please consider our other items.')
    console.log('works')
}
