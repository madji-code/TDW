chevron = document.querySelector('.container-inline > .chevron-down-solid');
create = document.querySelector('.container-connexion > .create');
container_connexion = document.querySelector('.container-connexion');
container_inline = document.querySelector('.container-inline');



chevron.addEventListener('click', () => {
    if (chevron.style.transform === "" || chevron.style.transform === "rotate(0deg)"){
        chevron.style.transform = "rotate(180deg)";
        container_connexion.style = "background-color: lightgreen; border: 2px solid black";
        container_inline.style = "border: 0; border-radius: 0;"
        create.style.display = "inline";
    } else {
        chevron.style.transform = "rotate(0deg)";
        container_connexion.style = "background-color: none; border: (255, 255, 255, 0))";
        container_inline.style = "border: 2px solid black; border-radius: 5em;"
        create.style.display = "none";
    }
});