/* JS général de l'application */

let theme = localStorage.getItem('theme');
const changeThemeToDark = () => {
    document.documentElement.setAttribute("theme", "dark") 
    localStorage.setItem("theme", "dark") 
}

const changeThemeToLight = () => {
    document.documentElement.setAttribute("theme", "light") 
    localStorage.setItem("theme", 'light') 
}

if(theme) {
    let test = localStorage.getItem('theme');
    if(test === 'dark') {
        changeThemeToDark()
    } else {
        changeThemeToLight()
    }
}

// Chercher l'élément permettant le switch de thème
const checkbox = document.getElementById("switch");

// Appliquer le changement
checkbox.addEventListener('click', () => {
    let theme = localStorage.getItem('theme'); 
    if (theme ==='dark'){
        changeThemeToLight()
    }else{
        changeThemeToDark()
    }   
});

