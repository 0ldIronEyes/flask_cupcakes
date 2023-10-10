
async function showInitisalCupcakes()
{
    const response = await axios.get("http://localhost:5000/api/cupcakes")
    for (let cupcake of response.data.cupcakes)
    {
        let cupcakeHTML =createCupcakeHTML(cupcake);
        $("#cupcake-list").append(cupcakeHTML)
    }
}


function createCupcakeHTML(cupcake) {
    return `<div data-cupcake-id=${cupcake.id}}>
    <img src = ${cupcake.image} alt= cupcake>
    <li>
       Flavor: ${cupcake.flavor} | Size : ${cupcake.size} | Rating : ${cupcake.rating}
       <button class="delete-button"> DELETE</button>
    </li>
    </div>`;

}

$("#cupcake-form").on("submit", async function(evt) {
    evt.preventDefault();
    let flavor = $("form-flavor").val();
    let size = $("form-size").val();
    let rating = $("form-rating").val();

    let cupcakeResponse = await axios.post("http://localhost:5000/api/cupcakes",
     {flavor, rating, size, image});

    let newCupcake = $(createCupcakeHTML(cupcakeResponse.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $("#cupcake-form").trigger("reset");

});


$("#cupcake-list").on("click", "delete-button",async function(evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");

    await axios.delete*(`"http://localhost:5000/api/cupcakes/${cupcakeId}`);
    $cupcake.remove();
} )

$(showInitialCupcakes);