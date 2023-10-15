// gets necessary information using API

class Recipe {
    constructor(id, name, imageURL) {
        this.id = id;
        this.title = name;
        this.image = imageURL;
    }
}
/**
 * Takes input to autocomplete ingredients. Returns array of recipe objects
 * @param {String} searchString 
 * @returns {Recipe[]}
 */

const getRecipes = async (ingredientString) => {
    const ApiURL = `${window.location.origin}/api/getrecipes?ingredients=${ingredientString}`
    const response = await fetch(ApiURL)
    const JSONarray = await response.json()
    let recipes = []
    for (const recipeObj of JSONarray) {
        const recipe = new Recipe(recipeObj.id, recipeObj.title, recipeObj.image)
        recipes.push(recipe)
    }
    console.log(recipes)
    return recipes
}

console.log("API Access loaded")