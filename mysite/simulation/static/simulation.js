


const onSubmission = async () => {
    //clear list
    document.getElementById("recipeList").innerHTML = ""
    const ingredients = document.getElementById("ingredients").value
    const ingredientsString = ingredients.split(/[ ,]+/).join(',')
    console.log("Retrieving recipes with following ingredients: " + ingredientsString)
    const recipes = await getRecipes(ingredientsString)
    console.log(recipes)
    for (const recipe of recipes) {
        const listItem = document.createElement("li")
        const recipeImage = document.createElement("img")
        recipeImage.src = recipe.image
        recipeImage.width = 100
        recipeImage.height = 100
        const recipeLabel = document.createElement("label")
        recipeLabel.textContent = recipe.title
        listItem.appendChild(recipeImage)
        listItem.appendChild(recipeLabel)
        recipeList.appendChild(listItem)
    }
}

document.getElementById("submit").addEventListener("click", evt => {
    console.log("Submitted!")
    onSubmission()
})