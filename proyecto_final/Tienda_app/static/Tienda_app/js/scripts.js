// Obtén referencias a los botones
// Obtén referencias a los botones
const blogButton = document.getElementById("opcion1");
const tiendaButton = document.getElementById("opcion2");

// Agrega eventos de clic a los botones
blogButton.addEventListener("click", function() {
    // Redirige al usuario a la página del blog
    window.location.href = "templates/blog.html";
});

tiendaButton.addEventListener("click", function() {
    // Redirige al usuario a la página de la tienda
    window.location.href = "templates/tienda.html";
});

