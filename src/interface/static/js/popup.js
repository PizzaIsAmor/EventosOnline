var popup = document.getElementById("popup");

document.getElementById("popup-close").addEventListener("click", function(event) {
    event.preventDefault();
    popup.classList.add("esconder");
    popup.classList.remove("popup");
});