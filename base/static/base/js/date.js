document.addEventListener("DOMContentLoaded", () => {
    // Función para obtener el año actual
    const getCurrentYear = () => {
        return new Date().getFullYear();
    }

    // Establecer el año actual en el elemento con id "current-year"
    const currentYearElement = document.querySelector("#current-year");
    if (currentYearElement) {
        currentYearElement.textContent = getCurrentYear();
    }
});